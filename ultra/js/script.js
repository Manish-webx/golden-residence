/**
 * ============================================================================
 * THE AUREVA | ULTRA-PREMIUM SENIOR LIVING SANCTUARY JAVASCRIPT
 * Responsive & Error-Free Interactive Controller • Pure Vanilla JS
 * ============================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
    initPreloader();
    initNavbarScroll();
    initMobileNavigation();
    initRevealAnimations();
    initMouseParallax();
    // initMagneticButtons(); // Disabled: removed button hover movement effect
});

/**
 * 1. PRELOADER & SPLASH EMBLEM ANIMATION
 */
function initPreloader() {
    const preloader = document.getElementById('luxury-preloader');
    if (!preloader) return;

    const hidePreloader = () => {
        preloader.classList.add('fade-out');
        setTimeout(() => {
            preloader.style.display = 'none';
        }, 800);
    };

    if (document.readyState === 'complete') {
        setTimeout(hidePreloader, 1000);
    } else {
        window.addEventListener('load', () => {
            setTimeout(hidePreloader, 1000);
        });
        setTimeout(hidePreloader, 3000);
    }
}

/**
 * 2. STICKY NAVBAR & GLASSMORPHISM TRANSITION
 */
function initNavbarScroll() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 60) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    }, { passive: true });
}

/**
 * 3. MOBILE HAMBURGER NAVIGATION
 */
function initMobileNavigation() {
    const toggleBtn = document.getElementById('mobile-toggle');
    const navLinks = document.getElementById('nav-links');
    if (!toggleBtn || !navLinks) return;

    const navItems = navLinks.querySelectorAll('a');

    toggleBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        navLinks.classList.toggle('active');
        toggleBtn.classList.toggle('active');
        document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
    });

    navItems.forEach(item => {
        item.addEventListener('click', () => {
            navLinks.classList.remove('active');
            toggleBtn.classList.remove('active');
            document.body.style.overflow = '';
        });
    });

    // Close menu when clicking anywhere outside on mobile
    document.addEventListener('click', (e) => {
        if (navLinks.classList.contains('active') && !navLinks.contains(e.target) && !toggleBtn.contains(e.target)) {
            navLinks.classList.remove('active');
            toggleBtn.classList.remove('active');
            document.body.style.overflow = '';
        }
    });
}

/**
 * 4. SCROLL REVEAL ANIMATIONS (INTERSECTION OBSERVER)
 */
function initRevealAnimations() {
    const revealElements = document.querySelectorAll('.reveal-on-scroll');
    if (!revealElements.length || typeof IntersectionObserver === 'undefined') {
        revealElements.forEach(el => el.classList.add('revealed'));
        return;
    }

    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -60px 0px',
        threshold: 0.1
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    revealElements.forEach(el => revealObserver.observe(el));
}

/**
 * 5. MOUSE PARALLAX EFFECT FOR HERO & AMBIENT GLOWS (DESKTOP ONLY)
 */
function initMouseParallax() {
    // Only apply on wide viewports without touch priority to prevent mobile scroll stutter
    if (window.innerWidth < 1024 || ('ontouchstart' in window)) return;

    const heroBg = document.getElementById('parallax-hero-bg');
    const glow1 = document.querySelector('.glow-1');
    const glow2 = document.querySelector('.glow-2');

    let requestRunning = false;
    let mouseX = 0;
    let mouseY = 0;

    document.addEventListener('mousemove', (e) => {
        mouseX = (e.clientX / window.innerWidth) - 0.5;
        mouseY = (e.clientY / window.innerHeight) - 0.5;

        if (!requestRunning) {
            requestAnimationFrame(() => {
                if (heroBg) {
                    heroBg.style.transform = `scale(1.06) translate(${mouseX * -25}px, ${mouseY * -25}px)`;
                }
                if (glow1 && glow2) {
                    glow1.style.transform = `translate(${mouseX * 80}px, ${mouseY * 80}px)`;
                    glow2.style.transform = `translate(${mouseX * -80}px, ${mouseY * -80}px)`;
                }
                requestRunning = false;
            });
            requestRunning = true;
        }
    }, { passive: true });
}

/**
 * 6. MAGNETIC BUTTON HOVER EFFECT (DESKTOP ONLY)
 */
function initMagneticButtons() {
    // Feature removed so buttons do not move on hover/mousemove
    return;
}

/**
 * 7. ENQUIRE MODAL PORTAL CONTROLS (#enquire-modal)
 */
function openEnquireModal(titleText, subtitleText, priceText) {
    const modal = document.getElementById('enquire-modal');
    const modalFormTitle = document.getElementById('modal-form-title');
    const modalSubjectHidden = document.getElementById('modal-subject-hidden');

    if (!modal) return;

    if (modalFormTitle && titleText) modalFormTitle.innerText = titleText;
    if (modalSubjectHidden && titleText) {
        modalSubjectHidden.value = `${titleText} (${subtitleText || ''} | ${priceText || ''})`;
    }

    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeEnquireModal() {
    const modal = document.getElementById('enquire-modal');
    if (!modal) return;

    modal.classList.remove('active');
    document.body.style.overflow = '';
}

window.addEventListener('click', (e) => {
    const modal = document.getElementById('enquire-modal');
    if (e.target === modal) {
        closeEnquireModal();
    }
});

// Escape key closes modals
window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeEnquireModal();
        closeGalleryLightbox(e);
    }
});

/**
 * 8. MAIN ENQUIRY FORM SUBMISSION PROTOCOL (#staticform)
 */
function handleEnquirySubmit(event) {
    event.preventDefault();
    
    const submitBtn = document.getElementById('mainSubmitBtn');
    const successMsg = document.getElementById('main-success-msg');
    const form = document.getElementById('landing-enquiry-form');

    if (!submitBtn || !successMsg || !form) return;

    submitBtn.innerHTML = '<span>Verifying Protocol...</span> <i class="fa-solid fa-spinner fa-spin"></i>';
    submitBtn.disabled = true;

    setTimeout(() => {
        submitBtn.style.display = 'none';
        successMsg.style.display = 'block';
        form.reset();

        successMsg.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }, 1500);
}

/**
 * 9. MODAL FORM SUBMISSION PROTOCOL
 */
function handleModalSubmit(event) {
    event.preventDefault();

    const submitBtn = document.getElementById('modalSubmitBtn');
    const successMsg = document.getElementById('modal-success-msg');
    const form = document.getElementById('modal-form-inner');

    if (!submitBtn || !successMsg || !form) return;

    submitBtn.innerHTML = '<span>Processing VIP Access...</span> <i class="fa-solid fa-spinner fa-spin"></i>';
    submitBtn.disabled = true;

    setTimeout(() => {
        submitBtn.style.display = 'none';
        successMsg.style.display = 'block';
        form.reset();
    }, 1400);
}

/**
 * 10. FULL-SCREEN IMAGE LIGHTBOX COLLAGE CONTROLS (#gallery-lightbox)
 */
let currentLightboxTitle = '';

function openGalleryLightbox(imgUrl, titleText, pillText) {
    const lightbox = document.getElementById('gallery-lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxTitle = document.getElementById('lightbox-title');
    const lightboxPill = document.getElementById('lightbox-pill');

    if (!lightbox) return;

    currentLightboxTitle = titleText || 'Residence Architectural View';

    if (lightboxImg) lightboxImg.src = imgUrl;
    if (lightboxTitle) lightboxTitle.innerText = currentLightboxTitle;
    if (lightboxPill) lightboxPill.innerText = pillText || 'ARCHITECTURAL VIEW';

    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeGalleryLightbox(e) {
    if (e && e.stopPropagation) e.stopPropagation();
    const lightbox = document.getElementById('gallery-lightbox');
    if (!lightbox) return;

    lightbox.classList.remove('active');
    document.body.style.overflow = '';
}

function triggerLightboxEnquire() {
    closeGalleryLightbox();
    setTimeout(() => {
        openEnquireModal(`Collage Inquiry - ${currentLightboxTitle}`, '4 BHK (~4,200 Sq.Ft.)', '₹12 Cr* Onwards');
    }, 250);
}

