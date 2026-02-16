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

        // Close button (mobile)
        const navClose = document.querySelector('.nav-close');
        if (navClose) {
            navClose.addEventListener('click', () => {
                navMenu.classList.remove('active');
                body.classList.remove('menu-open');
            });
        }

        document.addEventListener('click', (event) => {
            if (!hamburger.contains(event.target) && !navMenu.contains(event.target)) {
                navMenu.classList.remove('active');
                body.classList.remove('menu-open');
            }
        });

        // Close the mobile menu when clicking regular links, but keep
        // dropdown triggers expandable on mobile.
        navMenu.querySelectorAll('a').forEach(link => {
            const isDropdownTrigger = link.parentElement.classList.contains('dropdown') && link.nextElementSibling && link.nextElementSibling.classList.contains('dropdown-menu');
            if (isDropdownTrigger) return;
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                body.classList.remove('menu-open');
            });
        });

        // Make dropdowns expandable on touch / mobile
        navMenu.querySelectorAll('li.dropdown > a').forEach(trigger => {
            trigger.addEventListener('click', (e) => {
                // Only toggle on small screens (when navMenu is the mobile drawer)
                if (window.matchMedia('(max-width: 768px)').matches) {
                    e.preventDefault();
                    const li = trigger.parentElement;
                    li.classList.toggle('open');
                }
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
