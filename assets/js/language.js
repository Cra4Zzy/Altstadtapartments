(() => {
const root=new URL('../../',document.currentScript.src);const isEn=document.documentElement.lang==='en';const relative=decodeURI(location.pathname).slice(decodeURI(root.pathname).length).replace(/^en\//,'');
const host=document.querySelector('.header-actions');if(!host)return;
const wrap=document.createElement('div');wrap.className='language-switch';wrap.innerHTML=['de','en'].map(lang=>`<a class="language-flag${(lang==='en')===isEn?' is-active':''}" aria-label="${lang==='de'?'Deutsch':'English'}" lang="${lang}" href="${new URL((lang==='en'?'en/':'')+relative,root).href}">${lang.toUpperCase()}</a>`).join('');host.insertBefore(wrap,host.querySelector('.menu-button'));
})();