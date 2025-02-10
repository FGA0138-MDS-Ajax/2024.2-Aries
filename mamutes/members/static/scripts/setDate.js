document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('input[type="date"]').forEach(input => {
        input.addEventListener("input", function () {
            let parts = this.value.split("-");
            if (parts[0] && parts[0].length > 4) {
                parts[0] = parts[0].slice(0, 4); // Limita o ano a 4 dígitos
                this.value = parts.join("-");
            }
        });
    });
});
