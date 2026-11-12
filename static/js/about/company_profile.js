// Initialize variables first
const scrollIndicator = document.getElementById('scrollIndicator');
const menuToggle = document.getElementById('menuToggle');
const mobileMenu = document.getElementById('mobileMenu');
let lastScrollY = 0;
let ticking = false;

// Scroll Progress Indicator
function updateScrollProgress() {
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollProgress = Math.min(window.scrollY / scrollHeight, 1);
    scrollIndicator.style.transform = `scaleX(${scrollProgress})`;
}

// Intersection Observer for animations
function setupObserver() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');

                // Animate capability bars
                const fills = entry.target.querySelectorAll('.capability-fill');
                fills.forEach(fill => {
                    const width = fill.dataset.width || 100;
                    setTimeout(() => {
                        fill.style.transform = `scaleX(${width / 100})`;
                    }, 300);
                });
            }
        });
    }, observerOptions);

    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
}

// Mobile Menu Toggle
function setupMobileMenu() {
    menuToggle.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });

    // Close menu when clicking links
    mobileMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.add('hidden');
        });
    });
}

// Smooth scroll for anchor links
function setupSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Scroll handler with throttling
function onScroll() {
    lastScrollY = window.scrollY;

    if (!ticking) {
        window.requestAnimationFrame(() => {
            updateScrollProgress();
            ticking = false;
        });
        ticking = true;
    }
}

// Initialize everything when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    setupObserver();
    setupMobileMenu();
    setupSmoothScroll();

    // Initial scroll progress
    updateScrollProgress();
});

// Add scroll listener
window.addEventListener('scroll', onScroll, { passive: true });

// Check for reduced motion preference
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
if (prefersReducedMotion.matches) {
    document.querySelectorAll('.reveal').forEach(el => {
        el.classList.add('visible');
    });
    document.querySelectorAll('.capability-fill').forEach(fill => {
        fill.style.transform = 'scaleX(1)';
    });
}