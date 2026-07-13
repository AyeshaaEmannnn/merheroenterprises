
    // Initialize all variables first
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    let hasAnimatedStats = false;

    // Scroll reveal with IntersectionObserver
    function initScrollReveal() {
      const reveals = document.querySelectorAll('.reveal');
      
      if (prefersReducedMotion) {
        reveals.forEach(el => el.classList.add('visible'));
        return;
      }
      
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
          }
        });
      }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
      });
      
      reveals.forEach(el => observer.observe(el));
    }

    // Animate stat numbers
    function animateStats() {
      const stats = document.querySelectorAll('.stat-number');
      
      stats.forEach(stat => {
        const target = parseInt(stat.dataset.target, 10);
        if (isNaN(target)) return;
        
        const duration = 2000;
        const startTime = performance.now();
        
        function updateNumber(currentTime) {
          const elapsed = currentTime - startTime;
          const progress = Math.min(elapsed / duration, 1);
          
          // Easing function
          const easeOutQuart = 1 - Math.pow(1 - progress, 4);
          const currentValue = Math.floor(easeOutQuart * target);
          
          stat.textContent = currentValue;
          
          if (progress < 1) {
            requestAnimationFrame(updateNumber);
          } else {
            stat.textContent = target;
          }
        }
        
        requestAnimationFrame(updateNumber);
      });
    }

    // Observe stats section
    function initStatsObserver() {
      if (prefersReducedMotion) {
        const stats = document.querySelectorAll('.stat-number');
        stats.forEach(stat => {
          const target = stat.dataset.target;
          if (target) stat.textContent = target;
        });
        return;
      }
      
      const statsSection = document.querySelector('.stat-number');
      if (!statsSection) return;
      
      const statsContainer = statsSection.closest('.grid');
      if (!statsContainer) return;
      
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting && !hasAnimatedStats) {
            hasAnimatedStats = true;
            animateStats();
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.5 });
      
      observer.observe(statsContainer);
    }

    // Initialize everything after DOM is ready
    document.addEventListener('DOMContentLoaded', () => {
      initScrollReveal();
      initStatsObserver();
    });
