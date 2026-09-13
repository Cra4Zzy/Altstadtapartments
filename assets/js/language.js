(() => {
  'use strict';
  const KEY='altstadt-language';
  const path=location.pathname;
  const isEn=/\/en(?:\/|$)/.test(path);
  const current=isEn?'en':'de';
  const saved=localStorage.getItem(KEY);
  const browser=(navigator.languages&&navigator.languages[0]||navigator.language||'de').toLowerCase();
  const preferred=saved||(browser.startsWith('de')?'de':'en');
  const mapTo=(lang)=>{
    const clean=path.replace(/\/en\/?/,'/');
    if(lang==='en') return '/en'+(clean==='/'?'/':clean);
    return clean||'/';
  };
  if(!saved && preferred!==current && !location.search.includes('langstay=1')){
    location.replace(mapTo(preferred)+location.search+location.hash);return;
  }
  const header=document.querySelector('.site-header .header-actions');
  if(!header)return;
  const wrap=document.createElement('div');
  wrap.className='language-switch';
  wrap.setAttribute('aria-label',current==='de'?'Sprache wählen':'Choose language');
  wrap.innerHTML=`<button type="button" data-lang="de" aria-pressed="${current==='de'}" title="Deutsch"><span class="lang-flag" aria-hidden="true">🇩🇪</span><span>DE</span></button><span class="lang-divider" aria-hidden="true"></span><button type="button" data-lang="en" aria-pressed="${current==='en'}" title="English"><span class="lang-flag" aria-hidden="true">🇬🇧</span><span>EN</span></button>`;
  header.insertBefore(wrap,header.querySelector('.menu-button'));
  wrap.addEventListener('click',e=>{
    const b=e.target.closest('[data-lang]');if(!b)return;
    const lang=b.dataset.lang;localStorage.setItem(KEY,lang);
    if(lang!==current) location.href=mapTo(lang)+'?langstay=1';
  });
})();
