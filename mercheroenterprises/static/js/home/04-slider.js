// Continuous auto-moving sliders (Manufacturing, OEM, Special)
document.addEventListener('DOMContentLoaded', () => {

    function initSlider(wrapperSelector, speed) {
        const wrapper = document.querySelector(wrapperSelector);
        if (!wrapper) return;

        wrapper.style.animation = 'none';
        wrapper.style.display = 'flex';
        wrapper.style.flexWrap = 'nowrap';

        const slides = Array.from(wrapper.children);
        const originalCount = slides.length;

        slides.forEach(slide => { slide.style.flex = '0 0 auto'; });
        slides.forEach(slide => wrapper.appendChild(slide.cloneNode(true)));

        let pos = 0;
        let running = true;
        let halfWidth = 0;

        function updateWidth() { halfWidth = Math.floor(wrapper.scrollWidth / 2); if (pos >= halfWidth) pos = 0; }
        window.addEventListener('resize', updateWidth);
        requestAnimationFrame(updateWidth);

        function step() { if (running && halfWidth > 0) { pos += speed; if (pos >= halfWidth) pos = 0; wrapper.style.transform = `translate3d(-${pos}px,0,0)`; } requestAnimationFrame(step); }

        wrapper.addEventListener('mouseenter', () => running = false);
        wrapper.addEventListener('mouseleave', () => running = true);
        wrapper.addEventListener('touchstart', () => running = false);
        wrapper.addEventListener('touchend', () => running = true);

        requestAnimationFrame(step);
    }

    initSlider('.manufacturing-slider .slider-wrapper', 0.6);
    initSlider('.oem-slider .slider-wrapper', 1.1);
    initSlider('.special-slider .slider-wrapper', 0.6);
});
