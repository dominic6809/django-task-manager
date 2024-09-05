document.addEventListener('DOMContentLoaded', function() {
    // Select all alerts
    var alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        // Set a timeout to hide each alert after 5 seconds
        setTimeout(function() {
            alert.classList.remove('show');
            alert.classList.add('fade');
        }, 3000); // 3000 milliseconds = 3 seconds
    });
});
