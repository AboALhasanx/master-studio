/**
 * Master Studio Offline Service Worker (PWA)
 * Enables 100% offline quiz drills, flashcard review, and asset caching.
 */

const CACHE_NAME = 'master-studio-v10';

const PRECACHE_URLS = [
    '/',
    '/quiz',
    '/quiz/bookmarks',
    '/quiz/history',
    '/api/quiz/list',
    '/static/quiz-vault.js',
    '/static/quiz.css',
    '/static/quiz.js',
    '/static/quiz-library.css',
    '/static/quiz-library.js',
    '/static/lucide.min.js',
    '/static/manifest.json',
    '/static/icon-192.png',
    '/static/icon-512.png',
    '/static/sounds/correct.mp3',
    '/static/sounds/wrong.mp3',
    '/static/sounds/completed.mp3',
    '/api/quiz/bundle',
    '/api/quiz/bundle?semester=1',
    // Pre-cache all 6 subject quiz views & data APIs for 100% offline access
    '/quiz/01_Cyber_Security/Quiz_01_Cybersecurity_Foundations',
    '/api/quiz/01_Cyber_Security/Quiz_01_Cybersecurity_Foundations',
    '/quiz/02_English_Language/Quiz_01_Grammar_and_Tenses',
    '/api/quiz/02_English_Language/Quiz_01_Grammar_and_Tenses',
    '/quiz/03_Data_Mining/Quiz_01_Introduction_to_Data_Mining',
    '/api/quiz/03_Data_Mining/Quiz_01_Introduction_to_Data_Mining',
    '/quiz/04_Advanced_Software_Eng/Quiz_01_Software_Crisis',
    '/api/quiz/04_Advanced_Software_Eng/Quiz_01_Software_Crisis',
    '/quiz/05_Soft_Computing/Quiz_01_Soft_Computing_Foundations',
    '/api/quiz/05_Soft_Computing/Quiz_01_Soft_Computing_Foundations',
    '/quiz/05_Soft_Computing/Quiz_02_Fuzzy_Logic_Systems',
    '/api/quiz/05_Soft_Computing/Quiz_02_Fuzzy_Logic_Systems'
];
// Install: Resilient pre-cache (individual add prevents single-failure aborts)
self.addEventListener('install', (event) => {
    self.skipWaiting();
    event.waitUntil(
        caches.open(CACHE_NAME).then(async (cache) => {
            for (const url of PRECACHE_URLS) {
                try {
                    await cache.add(url);
                } catch (err) {
                    console.warn('Pre-cache skipped for URL:', url, err);
                }
            }
        })
    );
});

// Activate: Clean up older cache versions
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((name) => {
                    if (name !== CACHE_NAME) {
                        return caches.delete(name);
                    }
                })
            );
        }).then(() => self.clients.claim())
    );
});

// Fetch: Offline-First Strategy
self.addEventListener('fetch', (event) => {
    const url = new URL(event.request.url);

    // 1a. Code assets (JS/CSS): Stale-While-Revalidate (instant offline boot + fresh background update)
    if (url.pathname.startsWith('/static/') && (url.pathname.endsWith('.js') || url.pathname.endsWith('.css'))) {
        event.respondWith(
            caches.match(event.request, { ignoreSearch: true }).then((cached) => {
                const netFetch = fetch(event.request).then((networkResp) => {
                    if (networkResp && networkResp.status === 200) {
                        const copy = networkResp.clone();
                        caches.open(CACHE_NAME).then((cache) => cache.put(event.request, copy));
                    }
                    return networkResp;
                }).catch(() => null);
                return cached || netFetch;
            })
        );
        return;
    }

    // 1b. Static Assets & Icons & Audio: Cache-First
    if (url.pathname.startsWith('/static/')) {
        event.respondWith(
            caches.match(event.request).then((cached) => {
                if (cached) return cached;
                return fetch(event.request).then((networkResp) => {
                    if (networkResp && networkResp.status === 200) {
                        const copy = networkResp.clone();
                        caches.open(CACHE_NAME).then((cache) => cache.put(event.request, copy));
                    }
                    return networkResp;
                });
            })
        );
        return;
    }

    // 2. API Quiz GET requests: Cache-First (instant offline) with background update
    if (url.pathname.startsWith('/api/quiz/')) {
        // If it's telemetry submission (POST), try network, fail gracefully
        if (event.request.method === 'POST') {
            event.respondWith(
                fetch(event.request).catch(() => {
                    return new Response(JSON.stringify({ status: 'offline_stored' }), {
                        headers: { 'Content-Type': 'application/json' }
                    });
                })
            );
            return;
        }

        event.respondWith(
            caches.match(event.request).then((cachedResponse) => {
                const networkFetch = fetch(event.request).then((networkResponse) => {
                    if (networkResponse && networkResponse.status === 200) {
                        const cloned = networkResponse.clone();
                        caches.open(CACHE_NAME).then((cache) => cache.put(event.request, cloned));
                    }
                    return networkResponse;
                }).catch(() => null);

                // Return cached version immediately if available!
                return cachedResponse || networkFetch;
            })
        );
        return;
    }

    // 3. HTML Navigation: Network-First with guaranteed Multi-Tier Cache Fallback
    if (event.request.mode === 'navigate' || event.request.headers.get('accept')?.includes('text/html')) {
        event.respondWith(
            fetch(event.request).then((netResp) => {
                if (netResp && netResp.status === 200) {
                    const copy = netResp.clone();
                    caches.open(CACHE_NAME).then((cache) => cache.put(event.request, copy));
                }
                return netResp;
            }).catch(async () => {
                // Multi-tier offline fallback: exact request -> /quiz -> / -> any cached quiz
                const directMatch = await caches.match(event.request, { ignoreSearch: true });
                if (directMatch) return directMatch;

                const quizShell = await caches.match('/quiz', { ignoreSearch: true });
                if (quizShell) return quizShell;

                const rootShell = await caches.match('/', { ignoreSearch: true });
                if (rootShell) return rootShell;

                // Last resort: search all cached responses for any quiz HTML
                const cache = await caches.open(CACHE_NAME);
                const keys = await cache.keys();
                for (const req of keys) {
                    if (req.url.includes('/quiz')) {
                        const fallback = await cache.match(req);
                        if (fallback) return fallback;
                    }
                }
                return new Response("Offline - Master Studio Quiz", {
                    headers: { "Content-Type": "text/html; charset=utf-8" }
                });
            })
        );
        return;
    }

    // Default: Cache first with network fallback
    event.respondWith(
        caches.match(event.request).then((resp) => resp || fetch(event.request))
    );
});
