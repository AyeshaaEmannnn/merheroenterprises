document.addEventListener('DOMContentLoaded', () => {
    // Email Modal
    const emailModal = document.getElementById('emailModal');
    const closeEmailModal = document.querySelector('.close-email-modal');
    const openEmailClientBtn = document.getElementById('openEmailClient');
    const copyEmailBtn = document.getElementById('copyEmailBtn');
    const modalEmailAddress = document.getElementById('modalEmailAddress');
    const emailLinks = document.querySelectorAll('a[href^="mailto:"]');

    let currentEmail = '';

    emailLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            currentEmail = link.href.replace('mailto:', '');
            modalEmailAddress.textContent = currentEmail;
            openEmailClientBtn.href = `mailto:${currentEmail}`;
            emailModal.classList.add('active');
            copyEmailBtn.classList.remove('copied');
            copyEmailBtn.innerHTML = '<i class="fas fa-copy"></i> Copy Email Address';
        });
    });

    closeEmailModal.addEventListener('click', () => emailModal.classList.remove('active'));
    copyEmailBtn.addEventListener('click', () => {
        navigator.clipboard.writeText(currentEmail).then(() => {
            copyEmailBtn.classList.add('copied');
            copyEmailBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
            setTimeout(() => {
                copyEmailBtn.classList.remove('copied');
                copyEmailBtn.innerHTML = '<i class="fas fa-copy"></i> Copy Email Address';
            }, 2000);
        });
    });
    emailModal.addEventListener('click', e => { if (e.target === emailModal) emailModal.classList.remove('active'); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && emailModal.classList.contains('active')) emailModal.classList.remove('active'); });

    // Gallery Modal
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImage');
    const closeBtn = document.getElementById('closeModal');
    const prevBtn = document.getElementById('prevImage');
    const nextBtn = document.getElementById('nextImage');
    const galleryImages = document.querySelectorAll('.mini-img');

    let currentImageIndex = 0;
    const images = Array.from(galleryImages);

    galleryImages.forEach((img, index) => {
        img.addEventListener('click', () => {
            currentImageIndex = index;
            openModal(img);
        });
    });

    function openModal(img) { modal.classList.add('active'); modalImg.src = img.src; modalImg.alt = img.alt; }
    function showImage(index) { currentImageIndex = (index + images.length) % images.length; openModal(images[currentImageIndex]); }

    closeBtn.addEventListener('click', () => modal.classList.remove('active'));
    nextBtn.addEventListener('click', () => showImage(currentImageIndex + 1));
    prevBtn.addEventListener('click', () => showImage(currentImageIndex - 1));
    modal.addEventListener('click', e => { if (e.target === modal) modal.classList.remove('active'); });
    document.addEventListener('keydown', e => {
        if (modal.classList.contains('active')) {
            if (e.key === 'ArrowRight') showImage(currentImageIndex + 1);
            else if (e.key === 'ArrowLeft') showImage(currentImageIndex - 1);
        }
    });
});
