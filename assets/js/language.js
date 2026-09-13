(() => {
  'use strict';

  const KEY = 'altstadt-language';
  const path = location.pathname;
  const isGitHubPages = location.hostname.endsWith('github.io');

  // GitHub project pages live below /<repo>/ while the custom domain lives at /.
  const segments = path.split('/').filter(Boolean);
  const basePath = isGitHubPages && segments.length ? `/${segments[0]}` : '';
  const pathWithoutBase = basePath && path.startsWith(basePath)
    ? (path.slice(basePath.length) || '/')
    : path;

  const isEn = /^\/en(?:\/|$)/.test(pathWithoutBase);
  const current = isEn ? 'en' : 'de';
  const saved = localStorage.getItem(KEY);
  const browser = (navigator.languages?.[0] || navigator.language || 'de').toLowerCase();
  const preferred = saved || (browser.startsWith('de') ? 'de' : 'en');

  const localizedPath = (lang) => {
    let clean = pathWithoutBase.replace(/^\/en(?:\/|$)/, '/');
    if (!clean.startsWith('/')) clean = `/${clean}`;

    const localized = lang === 'en'
      ? `/en${clean === '/' ? '/' : clean}`
      : clean;

    return `${basePath}${localized}` || '/';
  };

  const navigateToLanguage = (lang, replace = false) => {
    const target = new URL(location.href);
    target.pathname = localizedPath(lang);
    target.searchParams.set('langstay', '1');

    if (replace) location.replace(target.href);
    else location.href = target.href;
  };

  // On first visit only: use browser language. A manual choice always wins afterwards.
  if (!saved && preferred !== current && !new URLSearchParams(location.search).has('langstay')) {
    navigateToLanguage(preferred, true);
    return;
  }

  const header = document.querySelector('.site-header .header-actions');
  if (!header) return;

  const wrap = document.createElement('div');
  wrap.className = 'language-switch';
  wrap.setAttribute('aria-label', current === 'de' ? 'Sprache wählen' : 'Choose language');
  wrap.innerHTML = `
    <button type="button" data-lang="de" aria-pressed="${current === 'de'}" title="Deutsch">
      <span class="lang-flag" aria-hidden="true">🇩🇪</span><span>DE</span>
    </button>
    <span class="lang-divider" aria-hidden="true"></span>
    <button type="button" data-lang="en" aria-pressed="${current === 'en'}" title="English">
      <span class="lang-flag" aria-hidden="true">🇬🇧</span><span>EN</span>
    </button>`;

  header.insertBefore(wrap, header.querySelector('.menu-button'));

  wrap.addEventListener('click', (event) => {
    const button = event.target.closest('[data-lang]');
    if (!button) return;

    const lang = button.dataset.lang;
    localStorage.setItem(KEY, lang);
    if (lang !== current) navigateToLanguage(lang);
  });
})();
