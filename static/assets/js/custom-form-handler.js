document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('.php-email-form');
    
    forms.forEach(function(form) {
      form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Show loading indicator
        form.querySelector('.loading').style.display = 'block';
        form.querySelector('.error-message').style.display = 'none';
        form.querySelector('.sent-message').style.display = 'none';
        
        // Create form data
        const formData = new FormData(form);
        
        // Submit the form
        fetch(form.action, {
          method: 'POST',
          body: formData,
          headers: {
            'X-Requested-With': 'XMLHttpRequest'
          }
        })
        .then(response => {
          form.querySelector('.loading').style.display = 'none';
          
          if (response.redirected) {
            // If Django returns a redirect, follow it
            window.location.href = response.url;
          } else if (response.ok) {
            // Show success message briefly before redirecting
            form.querySelector('.sent-message').style.display = 'block';
            setTimeout(() => {
              window.location.href = '/home/';
            }, 1000);
          } else {
            form.querySelector('.error-message').textContent = 'Form submission failed. Please try again.';
            form.querySelector('.error-message').style.display = 'block';
          }
        })
        .catch(error => {
          form.querySelector('.loading').style.display = 'none';
          form.querySelector('.error-message').textContent = 'Network error. Please try again.';
          form.querySelector('.error-message').style.display = 'block';
        });
      });
    });
  });