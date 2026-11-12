// Product detail page: Description / Size Chart tab switching.
document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.pc-tab');
    if (tabs.length) {
        tabs.forEach((tab) => {
            tab.addEventListener('click', () => {
                const target = tab.getAttribute('data-product-tab');

                document.querySelectorAll('.pc-tab').forEach((t) => {
                    t.classList.remove('active');
                    t.setAttribute('aria-selected', 'false');
                });
                tab.classList.add('active');
                tab.setAttribute('aria-selected', 'true');

                document.querySelectorAll('.pc-tab-panel').forEach((panel) => {
                    panel.classList.toggle('active', panel.getAttribute('data-product-panel') === target);
                });
            });
        });
    }

    const gallery = document.querySelector('.pc-gallery');
    if (gallery) {
        const galleryImage = gallery.querySelector('.pc-gallery-main img');
        const prevBtn = gallery.querySelector('.pc-gallery-prev');
        const nextBtn = gallery.querySelector('.pc-gallery-next');
        const dots = gallery.querySelectorAll('.pc-dot');
        const imageData = gallery.dataset.galleryImages || '';
        const images = imageData ? imageData.split('||') : [];
        let currentIndex = 0;

        if (images.length > 1) {
            const baseAlt = galleryImage ? galleryImage.alt.replace(/\s*\(\d+ of \d+\)/, '') : '';

            const updateImage = (index) => {
                currentIndex = (index + images.length) % images.length;
                if (galleryImage) {
                    galleryImage.style.opacity = '0.5';
                    setTimeout(() => {
                        galleryImage.src = images[currentIndex];
                        galleryImage.alt = `${baseAlt} (${currentIndex + 1} of ${images.length})`;
                        galleryImage.style.opacity = '1';
                    }, 100);
                }
                dots.forEach((dot, i) => {
                    dot.classList.toggle('active', i === currentIndex);
                });
            };

            if (prevBtn) {
                prevBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    updateImage(currentIndex - 1);
                });
            }

            if (nextBtn) {
                nextBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    updateImage(currentIndex + 1);
                });
            }

            dots.forEach((dot) => {
                dot.addEventListener('click', (e) => {
                    e.preventDefault();
                    const index = parseInt(dot.getAttribute('data-index'), 10);
                    if (!isNaN(index)) {
                        updateImage(index);
                    }
                });
            });
        } else {
            if (prevBtn) prevBtn.style.display = 'none';
            if (nextBtn) nextBtn.style.display = 'none';
        }
    }
});
