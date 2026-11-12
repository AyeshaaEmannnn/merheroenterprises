document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    const body = document.body;
    const navbar = document.querySelector('.navbar');
    const heroSection = document.querySelector('#hero');

    // Hamburger Menu Toggle (Mobile)
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

        // Close menu when clicking outside
        document.addEventListener('click', (event) => {
            // Agar click menu ya hamburger ke bahar hai
            if (!hamburger.contains(event.target) && !navMenu.contains(event.target)) {
                navMenu.classList.remove('active');
                body.classList.remove('menu-open');

                // Desktop par bhi dropdowns band karein bahar click karne par
                document.querySelectorAll('li.dropdown.open').forEach(dd => dd.classList.remove('open'));
            }
        });

        // Regular Links (jo dropdown nahi hain) - click par menu band karein
        navMenu.querySelectorAll('a').forEach(link => {
            const parentLi = link.parentElement;
            const isDropdownTrigger = parentLi.classList.contains('dropdown');

            if (!isDropdownTrigger) {
                link.addEventListener('click', () => {
                    navMenu.classList.remove('active');
                    body.classList.remove('menu-open');
                });
            }
        });

        // ==================================================
        // DROPDOWN LOGIC (Laptop & Mobile Dono ke liye)
        // ==================================================
        navMenu.querySelectorAll('li.dropdown > a').forEach(trigger => {
            trigger.addEventListener('click', (e) => {
                e.preventDefault(); // Link ka default kaam roko

                const li = trigger.parentElement;

                // Agar koi aur dropdown open hai to use band karo
                navMenu.querySelectorAll('li.dropdown.open').forEach(openLi => {
                    if (openLi !== li) openLi.classList.remove('open');
                });

                // Toggle current dropdown
                li.classList.toggle('open');
                trigger.setAttribute('aria-expanded', li.classList.contains('open') ? 'true' : 'false');
            });
        });

        // ==================================================
        // PRODUCT SUBCATEGORY SUBMENU TOGGLE
        // ==================================================
        // Click on a main product category with subcategories should open its submenu,
        // while category page remains available via the submenu title link.
        navMenu.querySelectorAll('.product-category-item.has-submenu > a').forEach(trigger => {
            trigger.addEventListener('click', (e) => {
                const parent = trigger.parentElement;
                const submenu = parent.querySelector('.product-submenu');

                if (!submenu) return; // no submenu, regular link behavior

                e.preventDefault();
                e.stopPropagation();

                // Close any other open submenus
                navMenu.querySelectorAll('.product-category-item.has-submenu.submenu-open').forEach(el => {
                    if (el !== parent) {
                        el.classList.remove('submenu-open');
                        const otherSub = el.querySelector('.product-submenu');
                        if (otherSub) otherSub.style.display = '';
                    }
                });

                const isOpen = parent.classList.toggle('submenu-open');
                submenu.style.display = isOpen ? 'block' : '';
            });
        });

        // Ensure submenus reset on window resize
        let resizeTimer;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(() => {
                if (window.innerWidth > 768) {
                    document.querySelectorAll('.product-category-item.has-submenu.submenu-open').forEach(el => {
                        el.classList.remove('submenu-open');
                        const sub = el.querySelector('.product-submenu');
                        if (sub) sub.style.display = '';
                    });
                }
            }, 250);
        });

    }

    // Navbar Scroll Effect
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
