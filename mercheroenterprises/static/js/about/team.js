       document.addEventListener('DOMContentLoaded', function () {
            // Header scroll effect
            var header = document.getElementById('header');

            window.addEventListener('scroll', function () {
                if (window.scrollY > 50) {
                    header.classList.add('scrolled');
                } else {
                    header.classList.remove('scrolled');
                }
            });

            // Intersection Observer for reveals
            var observerOptions = {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            };

            var observer = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                    }
                });
            }, observerOptions);

            var revealElements = document.querySelectorAll('.reveal');
            revealElements.forEach(function (el) {
                observer.observe(el);
            });
        });