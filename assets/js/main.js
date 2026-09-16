(() => {
  'use strict';
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  const menuButton = $('.menu-button');
  const menu = $('#mobile-nav');
  const header = $('.site-header');
  let dialog;
  const updateLock = () => document.body.classList.toggle('locked', menu?.hidden === false || dialog?.open === true);
  function closeMenu(focus = false) {
    if (!menu || !menuButton) return;
    menu.hidden = true;
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Menü öffnen');
    updateLock();
    if (focus) menuButton.focus();
  }
  menuButton?.addEventListener('click', () => {
    if (!menu.hidden) return closeMenu();
    menu.hidden = false;
    menuButton.setAttribute('aria-expanded', 'true');
    menuButton.setAttribute('aria-label', 'Menü schließen');
    updateLock();
    if (!reducedMotion.matches && menu.animate) menu.animate([{opacity:0,transform:'translateY(-8px)'},{opacity:1,transform:'none'}],{duration:220,easing:'ease-out'});
  });
  $$('#mobile-nav a').forEach(a => a.addEventListener('click', () => closeMenu()));
  document.addEventListener('keydown', e => {
    if (menu?.hidden !== false) return;
    if (e.key === 'Escape') closeMenu(true);
    if (e.key === 'Tab') {
      const targets = [menuButton, ...$$('a', menu)];
      const first = targets[0], last = targets[targets.length - 1];
      if (e.shiftKey && (document.activeElement === first || !targets.includes(document.activeElement))) {e.preventDefault();last.focus();}
      else if (!e.shiftKey && (document.activeElement === last || !targets.includes(document.activeElement))) {e.preventDefault();first.focus();}
    }
  });
  document.addEventListener('click', e => {if (menu?.hidden === false && !header.contains(e.target)) closeMenu();});
  matchMedia('(min-width: 951px)').addEventListener('change', e => {if (e.matches) closeMenu();});
  $$('[data-year]').forEach(el => {el.textContent = new Date().getFullYear();});
  let scheduled = 0;
  const hero = $('.hero-main-photo');
  const heroImage = $('img', hero || document.createElement('div'));
  function updateScroll() {
    scheduled = 0;
    header?.classList.toggle('scrolled', scrollY > 12);
    if (!heroImage) return;
    if (reducedMotion.matches || innerWidth < 951) {heroImage.style.transform = '';return;}
    const bounds = hero.getBoundingClientRect();
    if (bounds.bottom > 0 && bounds.top < innerHeight) {
      const offset = Math.max(-12,Math.min(12,(innerHeight / 2 - bounds.top - bounds.height / 2) * .025));
      heroImage.style.transform = `translate3d(0,${offset}px,0) scale(1.05)`;
    }
  }
  const queueScroll = () => {if (!scheduled) scheduled = requestAnimationFrame(updateScroll);};
  addEventListener('scroll',queueScroll,{passive:true});
  addEventListener('resize',queueScroll);
  reducedMotion.addEventListener('change',queueScroll);
  updateScroll();
  if ('IntersectionObserver' in window && !reducedMotion.matches) {
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) {entry.target.classList.add('visible');observer.unobserve(entry.target);}
    }),{threshold:.06,rootMargin:'0px 0px -18px 0px'});
    $$('[data-reveal]').forEach(el => observer.observe(el));
    document.documentElement.classList.add('reveal-ready');
    reducedMotion.addEventListener('change',e => {if (e.matches) document.documentElement.classList.remove('reveal-ready');});
  }
  const links = $$('[data-gallery]');
  if (!links.length || typeof HTMLDialogElement === 'undefined') return;
  dialog = document.createElement('dialog');
  dialog.className = 'photo-dialog';
  dialog.setAttribute('aria-label','Apartment-Fotogalerie');
  dialog.innerHTML = '<div class="photo-dialog-inner"><div class="photo-dialog-top"><span data-photo-count aria-live="polite"></span><button class="photo-close" type="button" aria-label="Galerie schließen">×</button></div><div class="photo-stage"><button class="photo-prev" type="button" aria-label="Vorheriges Bild">←</button><img alt=""><button class="photo-next" type="button" aria-label="Nächstes Bild">→</button></div><p class="photo-caption" aria-live="polite"></p></div>';
  document.body.append(dialog);
  const photo = $('.photo-stage img',dialog), caption = $('.photo-caption',dialog), count = $('[data-photo-count]',dialog);
  const previous = $('.photo-prev',dialog), next = $('.photo-next',dialog);
  let current = [], index = 0, trigger = null, touchStart = null;
  function showImage(newIndex) {
    index = (newIndex + current.length) % current.length;
    const selected = current[index];
    photo.src = selected.href;
    photo.alt = selected.dataset.caption || $('img',selected)?.alt || 'Apartmentaufnahme';
    caption.textContent = photo.alt;
    count.textContent = `${index + 1} / ${current.length}`;
    previous.hidden = next.hidden = current.length < 2;
  }
  links.forEach(link => link.addEventListener('click',e => {
    if (e.ctrlKey || e.metaKey || e.shiftKey || e.altKey) return;
    e.preventDefault();
    trigger = link;
    current = links.filter(item => item.dataset.gallery === link.dataset.gallery);
    showImage(current.indexOf(link));
    dialog.showModal();
    updateLock();
    $('.photo-close',dialog).focus();
  }));
  $('.photo-close',dialog).addEventListener('click',() => dialog.close());
  previous.addEventListener('click',() => showImage(index - 1));
  next.addEventListener('click',() => showImage(index + 1));
  dialog.addEventListener('keydown',e => {
    if (e.key === 'ArrowLeft') {e.preventDefault();showImage(index - 1);}
    if (e.key === 'ArrowRight') {e.preventDefault();showImage(index + 1);}
  });
  dialog.addEventListener('click',e => {if (e.target === dialog) dialog.close();});
  photo.addEventListener('touchstart',e => {touchStart = {x:e.changedTouches[0].clientX,y:e.changedTouches[0].clientY};},{passive:true});
  photo.addEventListener('touchend',e => {
    if (!touchStart) return;
    const dx = e.changedTouches[0].clientX - touchStart.x, dy = e.changedTouches[0].clientY - touchStart.y;
    if (Math.abs(dx)>50 && Math.abs(dx)>Math.abs(dy)) showImage(index + (dx < 0 ? 1 : -1));
    touchStart = null;
  },{passive:true});
  dialog.addEventListener('close',() => {updateLock();trigger?.focus({preventScroll:true});});
})();

;(() => {
  'use strict';
  if (!document.body.classList.contains('home')) return;
  for (const href of ['assets/css/variants.css','assets/css/gartenschau.css']) {
    if (!document.querySelector(`link[href="${href}"]`)) {
      const link=document.createElement('link');link.rel='stylesheet';link.href=href;document.head.append(link);
    }
  }
  const choices={pur:'01 · Pur',sand:'02 · Sand',salbei:'03 · Salbei',terracotta:'04 · Terrakotta',fjord:'05 · Fjord'};
  const params=new URLSearchParams(location.search);let saved;
  try{saved=localStorage.getItem('altstadt-design-v2')}catch{}
  const apply=(key,updateUrl=false)=>{
    document.documentElement.dataset.theme=key;
    try{localStorage.setItem('altstadt-design-v2',key)}catch{}
    document.querySelectorAll('[data-set-theme]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.setTheme===key)));
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content','#ffffff');
    if(updateUrl){const u=new URL(location.href);u.searchParams.set('theme',key);history.replaceState(null,'',u)}
  };
  const preview=location.hostname.includes('github.io')||['localhost','127.0.0.1'].includes(location.hostname)||location.protocol==='file:';
  if(!preview){apply(choices[params.get('theme')]?params.get('theme'):(choices[saved]?saved:'pur'));return;}
  const box=document.createElement('details');box.className='theme-preview';box.open=innerWidth>600;
  box.innerHTML='<summary>Designvarianten ansehen</summary><div class="theme-preview__options">'+Object.entries(choices).map(([k,v])=>`<button type="button" data-set-theme="${k}">${v}</button>`).join('')+'</div><small>Drei helle Klassiker · zwei farbigere Entwürfe</small>';
  document.body.append(box);
  box.addEventListener('click',e=>{const b=e.target.closest('[data-set-theme]');if(b)apply(b.dataset.setTheme,true)});
  apply(choices[params.get('theme')]?params.get('theme'):(choices[saved]?saved:'pur'));
})();
