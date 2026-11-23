/* Ali Ahmad Khostovan · site behaviour (no dependencies).
   Everything here is progressive enhancement: pages work without JavaScript. */
(function () {
  'use strict';
  var doc = document.documentElement;

  /* ---- Theme toggle (light / dark), remembered per browser ---------------- */
  var mq = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
  function effectiveTheme() { return doc.getAttribute('data-theme') || (mq && mq.matches ? 'dark' : 'light'); }
  function syncToggles() {
    var dark = effectiveTheme() === 'dark';
    document.querySelectorAll('[data-theme-toggle]').forEach(function (b) {
      b.setAttribute('aria-pressed', String(dark));
      b.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
      b.title = dark ? 'Light theme' : 'Dark theme';
    });
  }
  document.querySelectorAll('[data-theme-toggle]').forEach(function (b) {
    b.addEventListener('click', function () {
      var next = effectiveTheme() === 'dark' ? 'light' : 'dark';
      doc.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) { /* storage unavailable */ }
      syncToggles();
    });
  });
  if (mq && mq.addEventListener) mq.addEventListener('change', syncToggles);
  syncToggles();

  /* ---- Current page in the menu ------------------------------------------ */
  var page = document.body.getAttribute('data-page');
  document.querySelectorAll('[data-nav]').forEach(function (a) {
    if (a.getAttribute('data-nav') === page) a.setAttribute('aria-current', 'page');
  });

  /* ---- Mobile menu --------------------------------------------------------- */
  var navToggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  function setNav(open) {
    if (!navToggle || !nav) return;
    navToggle.setAttribute('aria-expanded', String(open));
    navToggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    nav.classList.toggle('open', open);
  }
  if (navToggle && nav) {
    navToggle.addEventListener('click', function () { setNav(navToggle.getAttribute('aria-expanded') !== 'true'); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setNav(false); });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) setNav(false); });
    window.addEventListener('resize', function () { if (window.innerWidth > 1080) setNav(false); });
  }

  /* ---- Deep-field starfield ------------------------------------------------
     A seeded, procedurally drawn field of stars and small galaxies. Bright stars
     get JWST-style diffraction spikes (six long, two short). Drawn once per size. */
  function rng(seed) {
    return function () {
      seed |= 0; seed = (seed + 0x6D2B79F5) | 0;
      var t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function spike(ctx, ang, len, alpha, width) {
    var x = Math.cos(ang) * len, y = Math.sin(ang) * len;
    var g = ctx.createLinearGradient(0, 0, x, y);
    g.addColorStop(0, 'rgba(255,255,255,' + alpha + ')');
    g.addColorStop(1, 'rgba(255,255,255,0)');
    ctx.strokeStyle = g; ctx.lineWidth = width;
    ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(x, y); ctx.stroke();
  }
  function drawField(canvas) {
    var host = canvas.parentElement;
    var w = host.clientWidth, h = host.clientHeight;
    if (!w || !h) return;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.round(w * dpr); canvas.height = Math.round(h * dpr);
    var ctx = canvas.getContext('2d');
    if (!ctx) return;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, w, h);
    var rand = rng(parseInt(canvas.getAttribute('data-seed') || '11', 10));
    var density = parseFloat(canvas.getAttribute('data-density') || '1');
    var area = w * h, i, x, y, a;

    // Faint stars
    var nStars = Math.round(area / 1700 * density);
    for (i = 0; i < nStars; i++) {
      x = rand() * w; y = rand() * h;
      var r = 0.25 + Math.pow(rand(), 5) * 1.35;
      a = 0.12 + Math.pow(rand(), 2) * 0.68;
      var hue = rand();
      ctx.fillStyle = hue < 0.14 ? 'rgba(255,214,170,' + a + ')' : hue < 0.3 ? 'rgba(185,212,255,' + a + ')' : 'rgba(255,255,255,' + a + ')';
      ctx.beginPath(); ctx.arc(x, y, r, 0, 6.2832); ctx.fill();
    }
    // Small galaxies: soft, elongated, mostly warm (distant galaxies look red/orange in JWST colour images)
    var nGal = Math.round(area / 8200 * density);
    for (i = 0; i < nGal; i++) {
      x = rand() * w; y = rand() * h;
      var s = 0.7 + Math.pow(rand(), 3) * 3.4;
      var e = 0.32 + rand() * 0.6;
      var warm = rand() < 0.68;
      a = 0.22 + rand() * 0.45;
      var c = warm ? (rand() < 0.5 ? '255,176,112' : '255,206,140') : '190,214,255';
      ctx.save(); ctx.translate(x, y); ctx.rotate(rand() * Math.PI); ctx.scale(1, e);
      var gr = ctx.createRadialGradient(0, 0, 0, 0, 0, s * 2.4);
      gr.addColorStop(0, 'rgba(255,247,232,' + a + ')');
      gr.addColorStop(0.32, 'rgba(' + c + ',' + (a * 0.62) + ')');
      gr.addColorStop(1, 'rgba(' + c + ',0)');
      ctx.fillStyle = gr; ctx.beginPath(); ctx.arc(0, 0, s * 2.4, 0, 6.2832); ctx.fill();
      ctx.restore();
    }
    // Bright stars with diffraction spikes, kept out of the text column so they never cross words.
    // data-avoid="x0,y0,x1,y1" (fractions of the canvas) sets the keep-out box.
    var av = (canvas.getAttribute('data-avoid') || '0,0.12,0.66,0.94').split(',').map(parseFloat);
    var nBright = Math.max(2, Math.round(area / 170000 * density));
    ctx.lineCap = 'round';
    var inBox = function (px, py) { return px > av[0] * w && px < av[2] * w && py > av[1] * h && py < av[3] * h; };
    for (i = 0; i < nBright; i++) {
      var placed = false;
      for (var tries = 0; tries < 12 && !placed; tries++) { x = rand() * w; y = rand() * h; placed = !inBox(x, y); }
      if (!placed) continue;
      var L = 9 + rand() * 24;
      a = 0.5 + rand() * 0.4;
      ctx.save(); ctx.translate(x, y);
      for (var k = 0; k < 6; k++) spike(ctx, Math.PI / 2 + k * Math.PI / 3, L * (k % 3 === 0 ? 1 : 0.82), a, 1);
      spike(ctx, 0, L * 0.42, a * 0.7, 0.7); spike(ctx, Math.PI, L * 0.42, a * 0.7, 0.7);
      var core = ctx.createRadialGradient(0, 0, 0, 0, 0, 5.5);
      core.addColorStop(0, 'rgba(255,255,255,' + a + ')');
      core.addColorStop(0.35, 'rgba(205,228,255,' + (a * 0.55) + ')');
      core.addColorStop(1, 'rgba(205,228,255,0)');
      ctx.fillStyle = core; ctx.beginPath(); ctx.arc(0, 0, 5.5, 0, 6.2832); ctx.fill();
      ctx.restore();
    }
  }
  var fields = Array.prototype.slice.call(document.querySelectorAll('canvas.starfield'));
  var lastW = 0;
  function drawAll(force) {
    var vw = window.innerWidth;
    if (!force && Math.abs(vw - lastW) < 2) return; // ignore mobile URL-bar height changes
    lastW = vw;
    fields.forEach(drawField);
  }
  if (fields.length) {
    drawAll(true);
    var t;
    window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(function () { drawAll(false); }, 160); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { drawAll(true); });
  }

  /* ---- Glossary tooltips (research page) --------------------------------- */
  var terms = document.querySelectorAll('a.term[href^="#g-"]');
  if (terms.length) {
    var tip = document.createElement('div');
    tip.className = 'tooltip'; tip.id = 'term-tip'; tip.setAttribute('role', 'tooltip'); tip.hidden = true;
    document.body.appendChild(tip);
    var showTip = function (el) {
      var entry = document.querySelector(el.getAttribute('href'));
      if (!entry) return;
      var dt = entry.querySelector('dt'), dd = entry.querySelector('dd');
      tip.innerHTML = '';
      var b = document.createElement('b'); b.textContent = dt ? dt.textContent : '';
      tip.appendChild(b); tip.appendChild(document.createTextNode(dd ? dd.textContent : ''));
      tip.hidden = false;
      var r = el.getBoundingClientRect(), sx = window.scrollX, sy = window.scrollY;
      var tw = tip.offsetWidth, th = tip.offsetHeight, vw = doc.clientWidth;
      var left = Math.max(sx + 12, Math.min(r.left + sx + r.width / 2 - tw / 2, sx + vw - tw - 12));
      var top = r.top + sy - th - 10;
      if (r.top - th - 10 < 72) top = r.bottom + sy + 10;
      tip.style.left = left + 'px'; tip.style.top = top + 'px';
      el.setAttribute('aria-describedby', 'term-tip');
    };
    var hideTip = function (el) { tip.hidden = true; if (el) el.removeAttribute('aria-describedby'); };
    terms.forEach(function (el) {
      el.addEventListener('mouseenter', function () { showTip(el); });
      el.addEventListener('mouseleave', function () { hideTip(el); });
      el.addEventListener('focus', function () { showTip(el); });
      el.addEventListener('blur', function () { hideTip(el); });
    });
    window.addEventListener('scroll', function () { if (!tip.hidden) tip.hidden = true; }, { passive: true });
  }

  /* ---- Publications filter + search -------------------------------------- */
  var pubs = document.querySelector('[data-pubs]');
  if (pubs) {
    var buttons = pubs.querySelectorAll('[data-filter]');
    var input = pubs.querySelector('input[type="search"]');
    var count = pubs.querySelector('[data-count]');
    var items = Array.prototype.slice.call(document.querySelectorAll('.pub'));
    var empty = document.querySelector('[data-pub-empty]');
    var filter = 'all';
    var apply = function () {
      var q = (input && input.value || '').trim().toLowerCase();
      var shown = 0;
      items.forEach(function (li) {
        var okF = filter === 'all' || (filter === 'first' && li.getAttribute('data-first') === '1') ||
                  (filter === 'student' && li.getAttribute('data-student') === '1');
        var ok = okF && (!q || li.textContent.toLowerCase().indexOf(q) !== -1);
        li.hidden = !ok; if (ok) shown++;
      });
      document.querySelectorAll('[data-pub-group]').forEach(function (g) {
        g.hidden = !g.querySelector('.pub:not([hidden])');
      });
      if (count) count.textContent = shown === items.length ? items.length + ' papers' : 'Showing ' + shown + ' of ' + items.length;
      if (empty) empty.hidden = shown !== 0;
    };
    buttons.forEach(function (b) {
      b.addEventListener('click', function () {
        filter = b.getAttribute('data-filter');
        buttons.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
        apply();
      });
    });
    if (input) input.addEventListener('input', apply);
    var preset = (location.hash.match(/filter=(first|student)/) || [])[1];
    if (preset) { var pb = pubs.querySelector('[data-filter="' + preset + '"]'); if (pb) pb.click(); }
  }

  /* ---- Click-to-load YouTube (privacy-enhanced, nothing loads until clicked) */
  document.querySelectorAll('[data-yt]').forEach(function (box) {
    var link = box.querySelector('a');
    if (!link) return;
    link.addEventListener('click', function (e) {
      e.preventDefault();
      var id = box.getAttribute('data-yt'), start = box.getAttribute('data-start');
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) + '?autoplay=1&rel=0' + (start ? '&start=' + parseInt(start, 10) : '');
      f.title = box.getAttribute('data-title') || 'YouTube video';
      f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      f.allowFullscreen = true;
      f.referrerPolicy = 'strict-origin-when-cross-origin';
      box.innerHTML = ''; box.appendChild(f);
    });
  });

  /* ---- Copy-to-clipboard (short bio) -------------------------------------- */
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    var label = btn.querySelector('span');
    var original = label ? label.textContent : '';
    btn.addEventListener('click', function () {
      var el = document.getElementById(btn.getAttribute('data-copy'));
      if (!el) return;
      var text = el.innerText.replace(/\s+\n/g, '\n').trim();
      var done = function () { if (label) { label.textContent = 'Copied'; setTimeout(function () { label.textContent = original; }, 1800); } };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () {});
      } else {
        var range = document.createRange(); range.selectNodeContents(el);
        var sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(range);
        try { document.execCommand('copy'); done(); } catch (e) { /* user can copy manually */ }
        sel.removeAllRanges();
      }
    });
  });
})();
