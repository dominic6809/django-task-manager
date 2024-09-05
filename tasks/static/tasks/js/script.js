// Set the current year in the footer
document.getElementById('year').textContent = new Date().getFullYear();

document.addEventListener('DOMContentLoaded', function() {
    // Select all alerts
    var alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        // Set timeout to hide each alert after 3 seconds.
        setTimeout(function() {
            alert.classList.remove('show');
            alert.classList.add('fade');
        }, 3000);
    });
});
