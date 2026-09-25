/**
 * Master Studio Offline Service Worker (PWA)
 * Enables 100% offline quiz drills, flashcard review, and asset caching.
 */

const CACHE_NAME = 'master-studio-v5';

const PRECACHE_URLS = [
    '/',
    '/quiz',
    '/api/quiz/list',
    '/static/quiz.css',
    '/static/quiz.js',
    '/static/lucide.min.js',
    '/static/manifest.json',
    '/static/icon-192.png',
    '/static/icon-512.png',
    '/static/sounds/correct.mp3',
    '/static/sounds/wrong.mp3',
    '/static/sounds/completed.mp3',
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
// Install: Pre-cache static application shell
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(PRECACHE_URLS);
        }).then(() => self.skipWaiting())
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

    // 1. Static Assets & Icons & Audio: Cache-First
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

    // 3. HTML Views (/quiz, /quiz/..., /): Cache-First / Fallback to /quiz
    if (event.request.mode === 'navigate' || event.request.headers.get('accept')?.includes('text/html')) {
        event.respondWith(
            caches.match(event.request).then((cachedResponse) => {
                // If exact page is in cache, return immediately (100% offline!)
                if (cachedResponse) {
                    // Update cache in background if online
                    fetch(event.request).then((netResp) => {
                        if (netResp && netResp.status === 200) {
                            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, netResp));
                        }
                    }).catch(() => {});
                    return cachedResponse;
                }

                // If not in cache, try network, fall back to /quiz hub
                return fetch(event.request).then((networkResponse) => {
                    const cloned = networkResponse.clone();
                    caches.open(CACHE_NAME).then((cache) => cache.put(event.request, cloned));
                    return networkResponse;
                }).catch(() => {
                    return caches.match('/quiz').then((hub) => hub || caches.match('/'));
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
