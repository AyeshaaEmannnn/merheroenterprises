document.addEventListener('DOMContentLoaded', () => {
    const heroSlides = document.querySelectorAll('.hero .slide');
    const heroDots = document.querySelectorAll('.slider-dots .dot');
    const prevBtn = document.querySelector('.slider-arrow.prev');
    const nextBtn = document.querySelector('.slider-arrow.next');

    let currentIndex = 0;
    let autoSlide;

    function showSlide(index) {
        heroSlides.forEach((s, i) => s.classList.toggle('active', i === index));
        heroDots.forEach((d, i) => d.classList.toggle('active', i === index));
        currentIndex = index;
    }

    function nextSlide() {
        showSlide((currentIndex + 1) % heroSlides.length);
    }

    function prevSlide() {
        showSlide((currentIndex - 1 + heroSlides.length) % heroSlides.length);
    }

    function startAutoSlide() { autoSlide = setInterval(nextSlide, 5500); }
    function stopAutoSlide() { clearInterval(autoSlide); }

    nextBtn.addEventListener('click', () => { nextSlide(); stopAutoSlide(); startAutoSlide(); });
    prevBtn.addEventListener('click', () => { prevSlide(); stopAutoSlide(); startAutoSlide(); });
    heroDots.forEach((dot, index) => { dot.addEventListener('click', () => { showSlide(index); stopAutoSlide(); startAutoSlide(); }); });

    showSlide(0);
    startAutoSlide();
});
