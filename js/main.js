(function () {
  'use strict';

  /* ============================================
     Mobile Navigation Toggle
     ============================================ */
  const navToggle = document.querySelector('.nav-toggle');

  if (navToggle) {
    navToggle.addEventListener('click', function () {
      const isOpen = document.body.classList.toggle('nav-open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    document.querySelectorAll('.nav-link').forEach(function (link) {
      link.addEventListener('click', function () {
        document.body.classList.remove('nav-open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && document.body.classList.contains('nav-open')) {
        document.body.classList.remove('nav-open');
        navToggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ============================================
     Trade Category Filtering
     ============================================ */
  const filterButtons = document.querySelectorAll('.filter-btn');
  const tradeCards = document.querySelectorAll('.trade-card[data-category]');

  function filterTrades(category) {
    tradeCards.forEach(function (card) {
      const match = category === 'all' || card.dataset.category === category;
      card.hidden = !match;
    });
  }

  filterButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      filterButtons.forEach(function (btn) {
        btn.classList.remove('active');
        btn.setAttribute('aria-pressed', 'false');
      });
      button.classList.add('active');
      button.setAttribute('aria-pressed', 'true');
      filterTrades(button.dataset.filter);
    });
  });

  /* ============================================
     Service Worker Registration
     ============================================ */
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('https://tradelift.surge.sh/sw.js').catch(function () {});
  }

  /* ============================================
     Newsletter Form (Formspree / mailto fallback)
     ============================================ */
  var NEWSLETTER_CONFIG = {
    formspreeEndpoint: 'https://formspree.io/f/xqpkvyjg'
  };

  var newsletterForm = document.querySelector('.newsletter-form');

  if (newsletterForm) {
    newsletterForm.addEventListener('submit', function (e) {
      e.preventDefault();

      var honeypot = newsletterForm.querySelector('[name="_gotcha"]');
      if (honeypot && honeypot.value) return;

      var emailInput = newsletterForm.querySelector('.newsletter-input');
      var email = emailInput ? emailInput.value.trim() : '';
      var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      if (!email || !emailPattern.test(email)) return;

      var button = newsletterForm.querySelector('button[type="submit"]');
      if (!button) return;
      if (button.disabled) return;
      var originalText = button.textContent;

      if (NEWSLETTER_CONFIG.formspreeEndpoint.indexOf('YOURID') !== -1) {
        window.location.href = 'mailto:?subject=' + encodeURIComponent('Subscribe me to TradeLift') + '&body=' + encodeURIComponent('Please add ' + email + ' to the TradeLift newsletter.');
        return;
      }

      button.textContent = 'Subscribing...';
      button.disabled = true;

      fetch(NEWSLETTER_CONFIG.formspreeEndpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: email })
      })
        .then(function (res) {
          if (!res.ok) {
            throw new Error('Formspree ' + res.status);
          }
          return res;
        })
        .then(function () {
          newsletterForm.reset();
          button.textContent = "You're on the list! Check your inbox to confirm.";
          setTimeout(function () {
            button.textContent = originalText;
            button.disabled = false;
          }, 4000);
        })
        .catch(function () {
          window.location.href = 'mailto:?subject=' + encodeURIComponent('Subscribe me to TradeLift') + '&body=' + encodeURIComponent('Please add ' + email + ' to the TradeLift newsletter.');
          button.textContent = originalText;
          button.disabled = false;
        });
    });
  }

  /* ============================================
     Exit-Intent Modal (Lead Magnet)
     ============================================ */
  const MODAL_STORAGE_KEY = 'tradelift_exit_modal_dismissed';
  const MODAL_VISITED_KEY = 'tradelift_has_visited';
  const ONESIGNAL_DISMISSED_KEY = 'tradelift_onesignal_dismissed';

  function createExitModal() {
    const modal = document.createElement('div');
    modal.id = 'exit-modal';
    modal.className = 'exit-modal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-labelledby', 'exit-modal-title');
    modal.innerHTML = `
      <div class="exit-modal-overlay" tabindex="-1"></div>
      <div class="exit-modal-content">
        <button class="exit-modal-close" aria-label="Close modal">&times;</button>
        <div class="exit-modal-icon" aria-hidden="true">🎁</div>
        <h2 id="exit-modal-title" class="exit-modal-title">Don't Leave Empty-Handed!</h2>
        <p class="exit-modal-subtitle">Grab our free PDF: <strong>5 Trades Paying $60K+ with No Degree</strong></p>
        <form class="exit-modal-form" action="#" method="POST">
          <input type="hidden" name="_next" value="https://tradelift.surge.sh/assets/careers.guide">
          <div class="exit-modal-form-group">
            <label for="exit-modal-email" class="visually-hidden">Email address</label>
            <input
              type="email"
              id="exit-modal-email"
              name="email"
              class="exit-modal-input"
              placeholder="Enter your email to get the PDF"
              required
              autocomplete="email"
              aria-describedby="exit-modal-privacy"
            >
            <div style="position:absolute;left:-9999px" aria-hidden="true">
              <input type="text" name="_gotcha" tabindex="-1" autocomplete="off">
            </div>
            <button type="submit" class="btn btn-primary exit-modal-submit">Get Free PDF</button>
          </div>
          <p id="exit-modal-privacy" class="exit-modal-privacy">We respect your privacy. Unsubscribe at any time.</p>
        </form>
        <div class="exit-modal-success hidden" aria-live="polite">
          <div class="exit-modal-success-icon" aria-hidden="true">✅</div>
          <h3 class="exit-modal-success-title">Thanks! Check your email.</h3>
          <p class="exit-modal-success-text">Your free PDF is on its way. You can also download it directly:</p>
          <a href="https://tradelift.surge.sh/assets/careers.guide" class="btn btn-primary exit-modal-download" download="trade-lift-5-trades.pdf">Download PDF Now</a>
        </div>
      </div>
    `;
    document.body.appendChild(modal);
    return modal;
  }

  function showExitModal() {
    if (localStorage.getItem(MODAL_STORAGE_KEY)) {
      return; // User already dismissed
    }
    const modal = document.getElementById('exit-modal') || createExitModal();
    modal.classList.add('show');
    document.body.style.overflow = 'hidden';
    
    // Focus trap
    const closeBtn = modal.querySelector('.exit-modal-close');
    const submitBtn = modal.querySelector('.exit-modal-submit');
    const focusable = Array.from(modal.querySelectorAll('button, input, a')).filter(function(el) {
      return !el.classList.contains('hidden') && el.getAttribute('tabindex') !== '-1';
    });
    const firstFocusable = focusable[0];
    const lastFocusable = focusable[focusable.length - 1];
    
    if (firstFocusable) firstFocusable.focus();
    
    modal.addEventListener('keydown', function trapFocus(e) {
      if (e.key === 'Tab') {
        if (e.shiftKey && document.activeElement === firstFocusable) {
          e.preventDefault();
          lastFocusable?.focus();
        } else if (!e.shiftKey && document.activeElement === lastFocusable) {
          e.preventDefault();
          firstFocusable?.focus();
        }
      } else if (e.key === 'Escape') {
        hideExitModal();
      }
    });
  }

  function hideExitModal() {
    const modal = document.getElementById('exit-modal');
    if (modal) {
      modal.classList.remove('show');
      document.body.style.overflow = '';
      localStorage.setItem(MODAL_STORAGE_KEY, 'true');
    }
  }

  function handleExitModalSubmit(e) {
    e.preventDefault();
    var form = e.target;
    var honeypot = form.querySelector('[name="_gotcha"]');
    if (honeypot && honeypot.value) return;

    var emailInput = form.querySelector('.exit-modal-input');
    var email = emailInput ? emailInput.value.trim() : '';
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email || !emailPattern.test(email)) return;

    var submitBtn = form.querySelector('.exit-modal-submit');
    if (!submitBtn) return;
    if (submitBtn.disabled) return;
    var originalText = submitBtn.textContent;

    if (NEWSLETTER_CONFIG.formspreeEndpoint.indexOf('YOURID') !== -1) {
      window.location.href = 'mailto:?subject=' + encodeURIComponent('Subscribe me to TradeLift') + '&body=' + encodeURIComponent('Please add ' + email + ' to the TradeLift newsletter.');
      return;
    }

    submitBtn.textContent = 'Subscribing...';
    submitBtn.disabled = true;

    fetch(NEWSLETTER_CONFIG.formspreeEndpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: email })
    })
      .then(function (res) {
        if (!res.ok) {
          throw new Error('Formspree ' + res.status);
        }
        return res;
      })
      .then(function () {
        form.classList.add('hidden');
        var success = form.parentElement.querySelector('.exit-modal-success');
        if (success) success.classList.remove('hidden');
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
      })
      .catch(function () {
        window.location.href = 'mailto:?subject=' + encodeURIComponent('Subscribe me to TradeLift') + '&body=' + encodeURIComponent('Please add ' + email + ' to the TradeLift newsletter.');
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
      });
  }

  // Initialize exit-intent modal
  function initExitModal() {
    // Mark as visited
    const hasVisited = localStorage.getItem(MODAL_VISITED_KEY);
    localStorage.setItem(MODAL_VISITED_KEY, 'true');
    
    // Desktop: mouseleave
    document.addEventListener('mouseleave', function (e) {
      if (!hasVisited && e.clientY <= 0) {
        showExitModal();
      }
    }, { once: true });
    
    // Mobile: beforeunload (scroll up detection as fallback)
    let lastScrollY = window.scrollY;
    window.addEventListener('scroll', function () {
      if (!hasVisited && window.scrollY < lastScrollY && window.scrollY < 100) {
        // User scrolled up near top - potential exit intent
        showExitModal();
      }
      lastScrollY = window.scrollY;
    }, { passive: true });
    
    // Beforeunload as last resort
    window.addEventListener('beforeunload', function () {
      if (!hasVisited && !localStorage.getItem(MODAL_STORAGE_KEY)) {
        showExitModal();
      }
    });
    
    // Event delegation for modal actions
    document.addEventListener('click', function (e) {
      const modal = document.getElementById('exit-modal');
      if (!modal) return;
      
      if (e.target.matches('.exit-modal-close') || e.target.matches('.exit-modal-overlay')) {
        hideExitModal();
      }
    });
    
    document.addEventListener('submit', function (e) {
      if (e.target.matches('.exit-modal-form')) {
        handleExitModalSubmit(e);
      }
    });
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initExitModal);
  } else {
    initExitModal();
  }

  /* ============================================
     OneSignal Web Push (Free Tier)
     ============================================ */
  function initOneSignal() {
    if (window.OneSignal) return;
    var ONESIGNAL_APP_ID = 'YOUR_ONESIGNAL_APP_ID';
    if (ONESIGNAL_APP_ID.indexOf('YOUR_') !== -1) return;
    
    // Check if user dismissed before
    if (localStorage.getItem(ONESIGNAL_DISMISSED_KEY)) return;
    
    // Check if this is at least second visit
    const hasVisited = localStorage.getItem(MODAL_VISITED_KEY);
    if (!hasVisited) {
      // First visit - don't prompt yet
      return;
    }
    
    // Load OneSignal SDK
    const script = document.createElement('script');
    script.src = 'https://cdn.onesignal.com/sdks/OneSignalSDK.js';
    script.async = true;
    script.onload = function () {
      window.OneSignal = window.OneSignal || [];
      OneSignal.push(function () {
        OneSignal.init({
          appId: "YOUR_ONESIGNAL_APP_ID", // Replace with actual App ID
          notifyButton: {
            enable: false // We'll use custom prompt
          },
          promptOptions: {
            slidedown: {
              enabled: true,
              actionMessage: "Get notified about new trade opportunities!",
              acceptButtonText: "Allow",
              cancelButtonText: "No thanks"
            }
          },
          autoRegister: false,
          autoResubscribe: true
        });
        
        // Show prompt on second visit (after a short delay)
        setTimeout(function () {
          OneSignal.showSlidedownPrompt();
        }, 3000);
        
        // Track dismissal
        OneSignal.on('notificationPermissionChange', function (permission) {
          if (permission === 'denied' || permission === 'default') {
            localStorage.setItem(ONESIGNAL_DISMISSED_KEY, 'true');
          }
        });
      });
    };
    document.head.appendChild(script);
  }
  
  // Initialize OneSignal after DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initOneSignal);
  } else {
    initOneSignal();
  }
})();