// Master Studio Dashboard - Client JS

document.addEventListener('DOMContentLoaded', () => {
  // Animate stat values on load
  document.querySelectorAll('.stat-value').forEach(el => {
    const text = el.textContent;
    const num = parseFloat(text);
    if (isNaN(num)) return;

    const suffix = text.replace(/[\d.]/g, '');
    const duration = 600;
    const start = performance.now();

    function tick(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = num * eased;

      if (num % 1 !== 0) {
        el.textContent = current.toFixed(1) + suffix;
      } else {
        el.textContent = Math.round(current) + suffix;
      }

      if (progress < 1) {
        requestAnimationFrame(tick);
      }
    }

    el.textContent = '0' + suffix;
    requestAnimationFrame(tick);
  });

  // Animate content bars
  document.querySelectorAll('.bar-fill').forEach(bar => {
    const target = bar.style.width;
    bar.style.width = '0%';
    setTimeout(() => {
      bar.style.width = target;
    }, 100);
  });

  // Auto-refresh data every 30s
  setInterval(async () => {
    try {
      const res = await fetch('/api/data');
      if (res.ok) {
        // Data refreshed — could update DOM incrementally if needed
        // For now, full reload keeps it simple
      }
    } catch (e) {
      // Server not reachable — ignore
    }
  }, 30000);
});
