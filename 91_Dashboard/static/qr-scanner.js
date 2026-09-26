/**
 * Master Studio QR Link Scanner (PWA + Android WebView)
 * ------------------------------------------------------------------
 * Scans the session QR code opened by `quiz_qr.py` on the PC and jumps
 * straight to the Flask quiz session (http://<lan-ip>:5000/quiz/...).
 *
 * Security whitelist: only private/LAN origins on port 5000 with a
 * /quiz path are accepted — anything else (public IPs, https, other
 * ports, /cards decks) is rejected with an Arabic error message.
 *
 * Works offline-safe: the decoder (jsQR, vendored at
 * /static/jsqr.min.js) and this script are both precached by sw.js.
 * When the camera API is unavailable (permission denied, insecure
 * origin, headless), a manual "paste the link" row remains usable.
 */
(function () {
    'use strict';

    /* ---------------------------------------------------------------
     * 1. URL whitelist — private ranges, port 5000, /quiz path only.
     * --------------------------------------------------------------- */
    var QUIZ_LINK_RE = new RegExp(
        '^http://' +
        '(?:localhost|127\\.0\\.0\\.1|' +
        '192\\.168\\.\\d{1,3}\\.\\d{1,3}|' +
        '10\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}|' +
        '172\\.(?:1[6-9]|2\\d|3[01])\\.\\d{1,3}\\.\\d{1,3})' +
        ':5000/quiz(?:/[A-Za-z0-9_\\-./]*)?(?:\\?[^\\s]*)?$',
        ''
    );

    var STATUS = {
        opening: 'تم التقاط الرابط… جارٍ فتح الكويز',
        scanning: 'جارٍ البحث عن الكود…',
        noCamera: 'تعذّر تشغيل الكاميرا. الصق الرابط يدوياً بالأسفل.',
        denied: 'تم رفض إذن الكاميرا. فعّل الإذن من إعدادات الجهاز أو الصق الرابط يدوياً.',
        badLink: 'الكود ليس رابط كوز ماستر ستوديو — تأكد من فتح كود QR الصحيح من الحاسوب.',
        manualBad: 'الرابط غير صالح — يُقبل رابط كوز على المنفذ 5000 فقط.'
    };

    /* ---------------------------------------------------------------
     * 2. DOM handles
     * --------------------------------------------------------------- */
    var overlay = document.getElementById('qr-scanner-overlay');
    if (!overlay) { return; } // Not on the quiz shell page.

    var btnScan = document.getElementById('btn-qr-scan');
    var btnClose = document.getElementById('btn-qr-close');
    var btnManual = document.getElementById('btn-qr-open');
    var manualInput = document.getElementById('qr-manual-input');
    var statusEl = document.getElementById('qr-status');
    var video = document.getElementById('qr-video');

    var mediaStream = null;
    var scanTimer = null;
    var canvas = null;
    var ctx = null;
    var lastRejectAt = 0; // throttle repeated bad-code messages
    var cameraAttempts = 0; // busy-camera auto-retry budget

    function setStatus(msg) {
        if (statusEl) { statusEl.textContent = msg || ''; }
    }

    function isAllowed(url) {
        return typeof url === 'string' && QUIZ_LINK_RE.test(url.trim());
    }

    function openOverlay() {
        overlay.classList.remove('hidden');
        setStatus('');
        if (manualInput) { manualInput.value = ''; }
        startCamera();
        // Icons injected before lucide's initial pass may need a refresh.
        if (window.lucide && typeof window.lucide.createIcons === 'function') {
            try { window.lucide.createIcons(); } catch (e) { /* no-op */ }
        }
    }

    function closeOverlay() {
        overlay.classList.add('hidden');
        stopCamera();
    }

    function stopCamera() {
        if (scanTimer) { clearTimeout(scanTimer); scanTimer = null; }
        if (mediaStream) {
            try {
                mediaStream.getTracks().forEach(function (t) { t.stop(); });
            } catch (e) { /* no-op */ }
            mediaStream = null;
        }
        if (video) { video.srcObject = null; }
    }

    /* ---------------------------------------------------------------
     * 3. Camera capture loop (jsQR decodes one frame per tick)
     * --------------------------------------------------------------- */
    function startCamera() {
        if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
            // Insecure origin (http://LAN in the WebView or PWA): Chromium
            // hides mediaDevices entirely. The native APK catalog runs on
            // file:// which IS a trustworthy origin — send the user there.
            console.warn('[QR] mediaDevices unavailable (secure=' +
                window.isSecureContext + ', origin=' + window.location.origin + ')');
            if (window.__NATIVE__) {
                // Native APK on an http origin: bounce to the file:// catalog
                // (a trustworthy origin where the camera is allowed).
                window.location.replace('file:///android_asset/index.html#scan');
                return;
            }
            setStatus('الكاميرا غير متاحة عبر اتصال http غير آمن — افتح الماسح من صفحة الكاتالوج الرئيسية أو الصق الرابط يدوياً.');
            return;
        }
        navigator.mediaDevices.getUserMedia({
            video: { facingMode: { ideal: 'environment' } },
            audio: false
        }).then(function (stream) {
            cameraAttempts = 0;
            mediaStream = stream;
            if (video) {
                video.srcObject = stream;
                var playPromise = video.play();
                if (playPromise && typeof playPromise.catch === 'function') {
                    playPromise.catch(function () { /* autoplay hint only */ });
                }
            }
            setStatus(STATUS.scanning);
            scheduleTick(150);
        }).catch(function (err) {
            var name = (err && err.name) || 'Unknown';
            console.error('[QR] getUserMedia failed:', name, err && err.message);
            if (name === 'NotAllowedError' || name === 'PermissionDeniedError' ||
                name === 'SecurityError') {
                setStatus(STATUS.denied);
            } else if (name === 'NotReadableError' || name === 'AbortError' ||
                       name === 'TrackStartError') {
                // Camera busy (e.g. still releasing from a previous session):
                // short automatic retries, then fall back to manual paste.
                cameraAttempts += 1;
                if (cameraAttempts <= 3) {
                    setStatus('الكاميرا مشغولة حالياً — إعادة المحاولة…');
                    setTimeout(function () { startCamera(); }, 900);
                } else {
                    setStatus(STATUS.noCamera);
                }
            } else {
                setStatus(STATUS.noCamera);
            }
        });
    }

    function scheduleTick(delay) {
        if (overlay.classList.contains('hidden')) { return; }
        scanTimer = setTimeout(decodeFrame, delay);
    }

    function decodeFrame() {
        if (overlay.classList.contains('hidden')) { stopCamera(); return; }
        if (!video || video.readyState < 2 || !video.videoWidth) {
            scheduleTick(300);
            return;
        }
        if (!window.jsQR) { scheduleTick(500); return; }

        try {
            if (!canvas) {
                canvas = document.createElement('canvas');
                ctx = canvas.getContext('2d', { willReadFrequently: true });
            }
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
            var frame = ctx.getImageData(0, 0, canvas.width, canvas.height);
            var code = window.jsQR(frame.data, frame.width, frame.height, {
                inversionAttempts: 'dontInvert'
            });
            if (code && code.data) {
                handleDecoded(code.data.trim());
                return; // handleDecoded() re-schedules on failure
            }
        } catch (e) {
            // Frame glitch — keep scanning.
        }
        scheduleTick(250);
    }

    function handleDecoded(text) {
        if (isAllowed(text)) {
            setStatus(STATUS.opening);
            stopCamera();
            // Full page navigation so the WebView/Chrome loads the
            // session quiz (same-origin fetch/telemetry to the PC).
            window.location.href = text;
            return;
        }
        var now = Date.now();
        if (now - lastRejectAt > 2500) {
            lastRejectAt = now;
            setStatus(STATUS.badLink);
        }
        scheduleTick(400);
    }

    /* ---------------------------------------------------------------
     * 4. Manual paste fallback (always available, whitelisted too)
     * --------------------------------------------------------------- */
    function openManual() {
        var value = (manualInput && manualInput.value || '').trim();
        if (isAllowed(value)) {
            setStatus(STATUS.opening);
            stopCamera();
            window.location.href = value;
        } else {
            setStatus(STATUS.manualBad);
        }
    }

    /* ---------------------------------------------------------------
     * 5. Wiring
     * --------------------------------------------------------------- */
    if (btnScan) { btnScan.addEventListener('click', openOverlay); }
    if (btnClose) { btnClose.addEventListener('click', closeOverlay); }
    if (btnManual) { btnManual.addEventListener('click', openManual); }
    if (manualInput) {
        manualInput.addEventListener('keydown', function (ev) {
            if (ev.key === 'Enter') { ev.preventDefault(); openManual(); }
        });
    }
    overlay.addEventListener('click', function (ev) {
        if (ev.target === overlay) { closeOverlay(); }
    });
    document.addEventListener('keydown', function (ev) {
        if (ev.key === 'Escape' && !overlay.classList.contains('hidden')) {
            closeOverlay();
        }
    });
    window.addEventListener('pagehide', stopCamera);

    // Deep-link: opening the catalog with #scan auto-launches the scanner
    // (used when the native app redirects here for a secure camera origin).
    if (window.location.hash === '#scan') {
        setTimeout(openOverlay, 60);
    }
})();
