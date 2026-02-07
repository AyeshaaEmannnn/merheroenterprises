document.addEventListener('DOMContentLoaded', () => {
    const sliders = document.querySelectorAll('.slider-wrapper');
    sliders.forEach(slider => {
        let touchStartX = 0;
        let touchEndX = 0;
        slider.addEventListener('touchstart', e => touchStartX = e.changedTouches[0].screenX);
        slider.addEventListener('touchend', e => {
            touchEndX = e.changedTouches[0].screenX;
            if (touchStartX - touchEndX > 50 || touchEndX - touchStartX > 50) {
                slider.style.animationPlayState = 'paused';
                setTimeout(() => slider.style.animationPlayState = 'running', 1000);
            }
        });
    });
});
