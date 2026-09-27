/**
 * Master Studio PWA bootstrap (D-05 / CSP hardening)
 * ------------------------------------------------------------------
 * This used to be an inline <script> block inside quiz.html. Strict
 * `script-src 'self'` CSP cannot allow inline execution, so the block
 * was externalised verbatim into /static/pwa-boot.js.
 *
 * Responsibilities:
 *   1. Register the root-scope service worker (/sw.js).
 *   2. Capture beforeinstallprompt and show/hide the install banner.
 */
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js', { scope: '/' })
            .then(reg => console.log('Master Studio Root SW registered:', reg.scope))
            .catch(err => console.log('Root SW registration failed:', err));
    });
}

// 1-Tap PWA Installation Prompt
let deferredPrompt = null;
window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    const banner = document.getElementById('pwa-install-banner');
    if (banner) banner.classList.remove('hidden');
    if (typeof lucide !== 'undefined') lucide.createIcons();
});

document.getElementById('btn-pwa-install')?.addEventListener('click', async () => {
    if (deferredPrompt) {
        deferredPrompt.prompt();
        const { outcome } = await deferredPrompt.userChoice;
        deferredPrompt = null;
        document.getElementById('pwa-install-banner')?.classList.add('hidden');
        console.log(`Master Studio PWA install choice: ${outcome}`);
    }
});

document.getElementById('btn-pwa-dismiss')?.addEventListener('click', () => {
    document.getElementById('pwa-install-banner')?.classList.add('hidden');
});
