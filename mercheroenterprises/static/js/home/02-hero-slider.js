const desktopVideo = "/static/videos/laptopview.mp4";
const mobileVideo = "/static/videos/mobileview.mp4";
const heroVideo = document.getElementById("heroVideo");
const source = heroVideo.querySelector("source");
function loadHeroVideo() {
    source.src = window.innerWidth <= 768 ? mobileVideo : desktopVideo;
    heroVideo.load();
    heroVideo.play().catch(() => {});
}
loadHeroVideo();
window.addEventListener("resize", loadHeroVideo);