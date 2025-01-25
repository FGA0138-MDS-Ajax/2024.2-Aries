document.addEventListener("DOMContentLoaded", function () {
    const editButtons = document.querySelectorAll(".btnEditTask");
    const twoButton = document.querySelector(".twoButton");

    editButtons.forEach(button => {
        button.addEventListener("click", function (e) {
            // Oculta o botão `.twoButton` se ele já estiver visível
            if (twoButton.style.display === "block") {
                twoButton.style.display = "none";
            } else {
                // Posiciona o botão `.twoButton` próximo ao botão clicado
                const rect = button.getBoundingClientRect();
                twoButton.style.top = `${rect.top + window.scrollY + button.offsetHeight}px`;
                twoButton.style.left = `${rect.left + window.scrollX}px`;

                // Exibe o botão `.twoButton`
                twoButton.style.display = "block";
            }
        });
    });

    // Esconde o botão ao clicar fora dele
    document.addEventListener("click", function (e) {
        if (!e.target.closest(".twoButton") && !e.target.closest(".btnEditTask")) {
            twoButton.style.display = "none";
        }
    });
});
