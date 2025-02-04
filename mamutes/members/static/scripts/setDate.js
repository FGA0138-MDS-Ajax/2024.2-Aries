document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".data-input").forEach(input => {
        input.addEventListener("input", function () {
            if (this.type === "date") {
                let parts = this.value.split("-");
                if (parts[0] && parts[0].length > 4) {
                    parts[0] = parts[0].slice(0, 4);
                    this.value = parts.join("-");
                }
            }
        });
    });
});
