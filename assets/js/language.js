(() => {
  'use strict';

  const KEY = 'altstadt-language';
  const path = location.pathname;
  const isGitHubPages = location.hostname.endsWith('github.io');

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

  if (!saved && preferred !== current && !new URLSearchParams(location.search).has('langstay')) {
    navigateToLanguage(preferred, true);
    return;
  }

  const header = document.querySelector('.site-header .header-actions');
  if (!header) return;

  const flagBase = `${basePath}/assets/img/flags`;
  const wrap = document.createElement('div');
  wrap.className = 'language-switch';
  wrap.setAttribute('aria-label', current === 'de' ? 'Sprache wählen' : 'Choose language');
  wrap.innerHTML = `
    <button type="button" class="language-flag${current === 'de' ? ' is-active' : ''}" data-lang="de" aria-label="Deutsch" title="Deutsch">
      <img src="${flagBase}/de.svg" alt="" aria-hidden="true">
    </button>
    <button type="button" class="language-flag${current === 'en' ? ' is-active' : ''}" data-lang="en" aria-label="English" title="English">
      <img src="${flagBase}/en.svg" alt="" aria-hidden="true">
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
