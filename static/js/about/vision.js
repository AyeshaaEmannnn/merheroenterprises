// Intersection Observer for reveal animations
document.addEventListener('DOMContentLoaded', function () {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    // Observe all reveal elements
    var revealElements = document.querySelectorAll('.reveal');
    revealElements.forEach(function (el) {
        observer.observe(el);
    });

    // Parallax effect on hero glows
    var heroGlow1 = document.querySelector('.hero-glow-1');
    var heroGlow2 = document.querySelector('.hero-glow-2');

    if (heroGlow1 && heroGlow2) {
        document.addEventListener('mousemove', function (e) {
            var moveX = (e.clientX - window.innerWidth / 2) * 0.02;
            var moveY = (e.clientY - window.innerHeight / 2) * 0.02;

            heroGlow1.style.transform = 'translate(' + moveX + 'px, ' + moveY + 'px)';
            heroGlow2.style.transform = 'translate(' + (-moveX) + 'px, ' + (-moveY) + 'px)';
        });
    }

    // Value cards hover effect with stagger
    var valueCards = document.querySelectorAll('.value-card');
    valueCards.forEach(function (card, index) {
        card.addEventListener('mouseenter', function () {
            this.style.zIndex = '10';
        });
        card.addEventListener('mouseleave', function () {
            this.style.zIndex = '1';
        });
    });
});