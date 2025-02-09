// rating de voo
document.addEventListener("DOMContentLoaded", function () {
    // Seleciona todos os contêineres orgSuccess
    const containers = document.querySelectorAll(".orgSuccess");

    containers.forEach((container) => {
        // Seleciona as estrelas, o input e o texto dentro do contêiner atual
        const stars = container.querySelectorAll(".starIcon .star");
        const input = container.querySelector("input[name='stars']");
        const ratingText = container.querySelector("#ratingText");  // Atualizei para usar o ID correto
        const ratings = ["Ruim", "Regular", "Bom", "Muito Bom", "Ótimo"];

        stars.forEach((star) => {
            star.addEventListener("click", function () {
                const value = star.getAttribute("data-value");

                // Atualiza o valor do campo oculto dentro do contêiner atual
                input.value = value;

                // Atualiza o texto de avaliação dentro do contêiner atual
                if (ratingText) {
                    ratingText.textContent = ratings[value - 1]; // Atualiza o texto conforme o valor
                }

                // Atualiza a classe 'selected' nas estrelas dentro do contêiner atual
                stars.forEach((s, i) => {
                    if (i < value) {
                        s.classList.add("selected");
                    } else {
                        s.classList.remove("selected");
                    }
                });
            });
        });
    });
});