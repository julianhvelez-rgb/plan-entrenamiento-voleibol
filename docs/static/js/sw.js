// Service Worker para PWA

const CACHE_NAME = 'voleibol-v2';
const urlsToCache = [
  './',
  './index.html',
  './static/css/styles.css',
  './static/js/app.js',
  './static/manifest.json',
  './static/img/icon-72.png',
  './static/img/icon-96.png',
  './static/img/icon-128.png',
  './static/img/icon-144.png',
  './static/img/icon-152.png',
  './static/img/icon-192.png',
  './static/img/icon-384.png',
  './static/img/icon-512.png',
  './static/img/icon-maskable-192.png',
  './static/img/icon-maskable-512.png',
  './static/img/screenshot1.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response;
        }
        return fetch(event.request);
      }
    )
  );
});
