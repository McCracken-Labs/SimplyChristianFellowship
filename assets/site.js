// Simply Christian Fellowship — shared behavior
(function () {
  var root = document.documentElement;

  // ---- Mobile nav toggle ----
  function initNav() {
    var toggle = document.querySelector('.nav-toggle');
    var links = document.querySelector('.nav-links');
    if (!toggle || !links) return;
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        links.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // ---- Theme toggle (remembered, animated only on click) ----
  function initTheme() {
    var btn = document.querySelector('.theme-toggle');
    if (!btn) return;
    btn.addEventListener('click', function () {
      root.classList.add('theme-anim');
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('scf-theme', next); } catch (e) {}
      btn.setAttribute('aria-pressed', next === 'dark' ? 'true' : 'false');
    });
  }

  // ---- Logo scrolls to top (a sticky header defeats a plain #top anchor) ----
  function initLogoTop() {
    var brand = document.querySelector('.brand');
    if (!brand) return;
    var here = location.pathname.split('/').pop() || 'index.html';
    var target = (brand.getAttribute('href') || '').split('/').pop();
    if (target === here || (here === '' && target === 'index.html')) {
      brand.addEventListener('click', function (e) {
        e.preventDefault();
        var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
      });
    }
  }

  // ---- Scroll reveal ----
  function initReveal() {
    var els = document.querySelectorAll('.reveal');
    if (!els.length) return;
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduce || !('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('is-visible'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  }

  // ---- Contact / prayer form (Formspree AJAX) ----
  function initContactForm() {
    var form = document.getElementById('contact-form');
    if (!form) return;
    var status = form.querySelector('.form-status');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      // honeypot: if a bot filled the hidden field, pretend success and stop
      var hp = form.querySelector('[name="_gotcha"]');
      if (hp && hp.value) { show('ok', 'Thank you. Your message has been sent.'); return; }
      if (form.action.indexOf('YOUR_FORM_ID') !== -1) {
        show('err', 'The form is not connected yet. Please check back soon.');
        return;
      }
      var btn = form.querySelector('button[type="submit"]');
      if (btn) { btn.disabled = true; }
      show('', 'Sending...');
      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { 'Accept': 'application/json' }
      }).then(function (r) {
        if (r.ok) { form.reset(); show('ok', 'Thank you. Your message has been received.'); }
        else { r.json().then(function (d) {
          show('err', (d && d.errors && d.errors[0] && d.errors[0].message) || 'Something went wrong. Please try again.');
        }).catch(function () { show('err', 'Something went wrong. Please try again.'); }); }
      }).catch(function () {
        show('err', 'Network error. Please try again in a moment.');
      }).then(function () { if (btn) { btn.disabled = false; } });
    });
    function show(kind, msg) {
      if (!status) return;
      status.className = 'form-status' + (kind ? ' ' + kind : '');
      status.textContent = msg;
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    initNav(); initTheme(); initLogoTop(); initReveal(); initContactForm();
  });
})();
