(() => {
  "use strict";

  const body = document.body;
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  document.querySelectorAll("[data-year]").forEach((element) => {
    element.textContent = String(new Date().getFullYear());
  });

  const header = document.querySelector("[data-header]");
  const updateHeader = () => header?.classList.toggle("is-scrolled", window.scrollY > 28);
  updateHeader();
  window.addEventListener("scroll", updateHeader, { passive: true });

  const menuButton = document.querySelector(".menu-button");
  const mobileDrawer = document.querySelector(".mobile-drawer");

  const setDrawerState = (open) => {
    if (!menuButton || !mobileDrawer) return;
    menuButton.setAttribute("aria-expanded", String(open));
    menuButton.setAttribute("aria-label", open ? "Menü schließen" : "Menü öffnen");
    mobileDrawer.setAttribute("aria-hidden", String(!open));
    mobileDrawer.classList.toggle("is-open", open);
    body.classList.toggle("drawer-open", open);
  };

  menuButton?.addEventListener("click", () => {
    setDrawerState(menuButton.getAttribute("aria-expanded") !== "true");
  });

  mobileDrawer?.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => setDrawerState(false));
  });

  const revealTargets = [
    ...document.querySelectorAll(".reveal-line, .image-reveal, .headline-line")
  ].filter((element) => !element.closest(".atlas-hero"));

  revealTargets.forEach((element) => element.classList.add("reveal-pending"));

  if (!prefersReducedMotion && "IntersectionObserver" in window) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.01, rootMargin: "0px 0px -2%" });

    revealTargets.forEach((element) => revealObserver.observe(element));
  } else {
    revealTargets.forEach((element) => element.classList.add("is-visible"));
  }

  const heroData = [
    { index: "01 / 03", title: "Wohnbau", copy: "Individuell geplant. Massiv gebaut." },
    { index: "02 / 03", title: "Sonderbau", copy: "Besondere Aufgaben. Sauber gelöst." },
    { index: "03 / 03", title: "Außenraum", copy: "Flächen, die Grundstück und Gebäude verbinden." }
  ];
  const heroGallery = document.querySelector("[data-hero-gallery]");
  const heroSlides = [...document.querySelectorAll("[data-hero-slide]")];
  const heroTabs = [...document.querySelectorAll("[data-hero-tab]")];
  const heroIndex = document.querySelector("[data-hero-index]");
  const heroTitle = document.querySelector("[data-hero-title]");
  const heroCopy = document.querySelector("[data-hero-copy]");
  const heroProgress = document.querySelector("[data-hero-progress]");
  let activeHero = 0;
  let heroTimer = 0;

  const runHeroProgress = () => {
    if (!heroProgress || prefersReducedMotion) return;
    heroProgress.classList.remove("is-running");
    void heroProgress.offsetWidth;
    heroProgress.classList.add("is-running");
  };

  const stopHero = () => {
    window.clearInterval(heroTimer);
    heroTimer = 0;
    heroProgress?.classList.remove("is-running");
  };

  const startHero = () => {
    stopHero();
    if (prefersReducedMotion || heroSlides.length < 2 || document.hidden) return;
    runHeroProgress();
    heroTimer = window.setInterval(() => {
      setHeroSlide((activeHero + 1) % heroSlides.length, false);
    }, 6500);
  };

  function setHeroSlide(nextIndex, restartTimer = true) {
    const boundedIndex = Math.max(0, Math.min(Number(nextIndex), heroSlides.length - 1));
    const data = heroData[boundedIndex];
    activeHero = boundedIndex;

    heroSlides.forEach((slide, index) => {
      slide.classList.toggle("is-active", index === boundedIndex);
    });
    heroTabs.forEach((tab, index) => {
      const isActive = index === boundedIndex;
      tab.classList.toggle("is-active", isActive);
      tab.setAttribute("aria-selected", String(isActive));
    });

    if (data) {
      if (heroIndex) heroIndex.textContent = data.index;
      if (heroTitle) heroTitle.textContent = data.title;
      if (heroCopy) heroCopy.textContent = data.copy;
    }

    if (restartTimer) startHero();
    else runHeroProgress();
  }

  heroTabs.forEach((tab) => {
    tab.addEventListener("click", () => setHeroSlide(tab.dataset.heroTab));
  });

  heroGallery?.addEventListener("mouseenter", stopHero);
  heroGallery?.addEventListener("mouseleave", startHero);
  heroGallery?.addEventListener("focusin", stopHero);
  heroGallery?.addEventListener("focusout", (event) => {
    if (!heroGallery.contains(event.relatedTarget)) startHero();
  });
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) stopHero();
    else startHero();
  });
  startHero();

  const serviceEntries = [...document.querySelectorAll("[data-service-entry]")];
  const serviceImages = [...document.querySelectorAll("[data-service-image]")];
  const serviceCaption = document.querySelector("[data-service-caption]");
  const serviceLabels = [
    "Wohn- & Rohbau",
    "Sanierung & Umbau",
    "Gewerbe & Landwirtschaft",
    "Bodenplatten & Außenraum"
  ];

  const setActiveService = (nextIndex) => {
    const activeIndex = Math.max(0, Math.min(Number(nextIndex), serviceEntries.length - 1));

    serviceEntries.forEach((entry, index) => {
      const isActive = index === activeIndex;
      entry.classList.toggle("is-active", isActive);
      entry.querySelector("button")?.setAttribute("aria-expanded", String(isActive));
      const toggle = entry.querySelector(".service-entry__toggle");
      if (toggle) toggle.textContent = isActive ? "−" : "+";
    });
    serviceImages.forEach((image, index) => image.classList.toggle("is-active", index === activeIndex));
    if (serviceCaption) serviceCaption.textContent = serviceLabels[activeIndex] || "";
  };

  serviceEntries.forEach((entry) => {
    entry.querySelector("button")?.addEventListener("click", () => {
      setActiveService(entry.dataset.serviceEntry);
    });
  });

  const sectionLinks = [...document.querySelectorAll(".main-nav a")];
  const sectionTargets = sectionLinks
    .map((link) => document.querySelector(link.getAttribute("href")))
    .filter(Boolean);

  if (sectionTargets.length && "IntersectionObserver" in window) {
    const navObserver = new IntersectionObserver((entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (!visible) return;

      sectionLinks.forEach((link) => {
        link.classList.toggle("is-active", link.getAttribute("href") === `#${visible.target.id}`);
      });
    }, { rootMargin: "-30% 0px -58%", threshold: [0, 0.15, 0.4] });
    sectionTargets.forEach((section) => navObserver.observe(section));
  }

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") setDrawerState(false);
  });

  const contactForm = document.querySelector("[data-contact-form]");
  const formNote = document.querySelector("[data-form-note]");

  contactForm?.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!contactForm.reportValidity()) return;

    const formData = new FormData(contactForm);
    const name = String(formData.get("name") || "").trim();
    const email = String(formData.get("email") || "").trim();
    const phone = String(formData.get("phone") || "").trim();
    const message = String(formData.get("message") || "").trim();
    const subject = encodeURIComponent(`Projektanfrage von ${name}`);
    const mailBody = encodeURIComponent(
      `Guten Tag,\n\n${message}\n\nKontaktdaten:\nName: ${name}\nE-Mail: ${email}\nTelefon: ${phone || "nicht angegeben"}\n\nViele Grüße\n${name}`
    );

    if (formNote) {
      formNote.textContent = "Die Anfrage ist vorbereitet. Ihr E-Mail-Programm wird jetzt geöffnet.";
    }
    window.location.href = `mailto:info@seeberger-bau.de?subject=${subject}&body=${mailBody}`;
  });
})();
