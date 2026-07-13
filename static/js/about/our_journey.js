// Initialize variables first
const menuBtn = document.getElementById('menuBtn');
const mobileNav = document.getElementById('mobileNav');
let isMenuOpen = false;

// Intersection Observer for scroll animations
function initObserver() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.reveal').forEach(el => {
        observer.observe(el);
    });
}

// Mobile menu toggle
function toggleMenu() {
    isMenuOpen = !isMenuOpen;
    mobileNav.classList.toggle('hidden', !isMenuOpen);
}

// Smooth scroll for anchor links
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerOffset = 100;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });

                // Close mobile menu if open
                if (isMenuOpen) {
                    toggleMenu();
                }
            }
        });
    });
}

// Initialize everything when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    initObserver();
    initSmoothScroll();
    menuBtn.addEventListener('click', toggleMenu);
});

// Check for reduced motion preference
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
if (prefersReducedMotion.matches) {
    document.querySelectorAll('.reveal').forEach(el => {
        el.classList.add('visible');
    });
}