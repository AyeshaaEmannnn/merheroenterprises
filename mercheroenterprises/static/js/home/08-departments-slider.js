// Departments Slider - Mobile Only
document.addEventListener('DOMContentLoaded', () => {
    const departmentsGrid = document.querySelector('.departments-grid');

    if (!departmentsGrid) return;

    // Check if we're on mobile
    const isMobile = () => window.innerWidth <= 768;

    function initDepartmentsSlider() {
        if (!isMobile()) return;

        // Clone cards for infinite scroll effect
        const cards = Array.from(departmentsGrid.children);
        const originalCount = cards.length;

        if (cards.length > 0) {
            cards.forEach(card => {
                departmentsGrid.appendChild(card.cloneNode(true));
            });
        }

        let pos = 0;
        let running = true;
        let containerWidth = 0;
        const speed = 0.8; // Adjust scroll speed (higher = faster)

        function updateWidth() {
            containerWidth = Math.floor(departmentsGrid.scrollWidth / 2);
            if (pos >= containerWidth) pos = 0;
        }

        function step() {
            if (running && containerWidth > 0) {
                pos += speed;
                if (pos >= containerWidth) pos = 0;
                departmentsGrid.style.transform = `translate3d(-${pos}px, 0, 0)`;
            }
            requestAnimationFrame(step);
        }

        // Pause on interaction
        departmentsGrid.addEventListener('mouseenter', () => running = false);
        departmentsGrid.addEventListener('mouseleave', () => running = true);
        departmentsGrid.addEventListener('touchstart', () => running = false);
        departmentsGrid.addEventListener('touchend', () => running = true);

        // Update on resize
        window.addEventListener('resize', () => {
            if (!isMobile()) {
                // Reset to desktop if resized to larger screen
                departmentsGrid.style.transform = 'none';
                return;
            }
            updateWidth();
        });

        updateWidth();
        requestAnimationFrame(step);
    }

    // Initialize on load
    initDepartmentsSlider();

    // Re-initialize on window resize
    window.addEventListener('resize', () => {
        if (isMobile()) {
            // Only reinit if it wasn't mobile before and now is
            initDepartmentsSlider();
        }
    });
});
