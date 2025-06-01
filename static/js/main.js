// Custom JavaScript for the Online House Rental System

// Auto-hide alerts after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            alert.style.opacity = '0';
            setTimeout(function() {
                alert.remove();
            }, 300);
        }, 5000);
    });
});

// Enable Bootstrap tooltips
document.addEventListener('DOMContentLoaded', function() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

// Property search form validation
const searchForm = document.querySelector('form[action*="property_list"]');
if (searchForm) {
    searchForm.addEventListener('submit', function(e) {
        const minPrice = document.getElementById('min_price');
        const maxPrice = document.getElementById('max_price');
        
        if (minPrice.value && maxPrice.value && parseInt(minPrice.value) > parseInt(maxPrice.value)) {
            e.preventDefault();
            alert('Minimum price cannot be greater than maximum price');
        }
    });
}

// Booking form validation
const bookingForm = document.querySelector('form[action*="create_booking"]');
if (bookingForm) {
    bookingForm.addEventListener('submit', function(e) {
        const startDate = document.getElementById('start_date');
        const endDate = document.getElementById('end_date');
        
        if (new Date(startDate.value) >= new Date(endDate.value)) {
            e.preventDefault();
            alert('End date must be after start date');
        }
    });
}

// Image preview for property images
const imageInputs = document.querySelectorAll('input[type="file"][accept="image/*"]');
imageInputs.forEach(input => {
    input.addEventListener('change', function(e) {
        const preview = document.querySelector(`#${this.id}_preview`);
        if (preview) {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    preview.src = e.target.result;
                    preview.style.display = 'block';
                }
                reader.readAsDataURL(file);
            }
        }
    });
});

// Smooth scroll to top
const scrollToTop = document.querySelector('.scroll-to-top');
if (scrollToTop) {
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 100) {
            scrollToTop.style.display = 'block';
        } else {
            scrollToTop.style.display = 'none';
        }
    });
    
    scrollToTop.addEventListener('click', function(e) {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Property filter form reset
const filterForm = document.querySelector('form[action*="property_list"]');
if (filterForm) {
    const resetButton = document.querySelector('.filter-reset');
    if (resetButton) {
        resetButton.addEventListener('click', function(e) {
            e.preventDefault();
            filterForm.reset();
            filterForm.submit();
        });
    }
}

// Booking cancellation confirmation
const cancelButtons = document.querySelectorAll('form[action*="cancel_booking"]');
cancelButtons.forEach(form => {
    form.addEventListener('submit', function(e) {
        if (!confirm('Are you sure you want to cancel this booking?')) {
            e.preventDefault();
        }
    });
}); 