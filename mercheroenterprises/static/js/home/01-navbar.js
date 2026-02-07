document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    const body = document.body;
    const navbar = document.querySelector('.navbar');
    const heroSection = document.querySelector('#hero');

    if (hamburger && navMenu) {
        hamburger.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            body.classList.toggle('menu-open');
        });

        document.addEventListener('click', (event) => {
            if (!hamburger.contains(event.target) && !navMenu.contains(event.target)) {
                navMenu.classList.remove('active');
                body.classList.remove('menu-open');
            }
        });

        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                body.classList.remove('menu-open');
            });
        });
    }

    if (navbar && heroSection) {
        const heroHeight = heroSection.offsetHeight;
        window.addEventListener('scroll', () => {
            if (window.scrollY > heroHeight - 120) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        if (window.scrollY > heroHeight - 120) {
            navbar.classList.add('scrolled');
        }
    }
});
