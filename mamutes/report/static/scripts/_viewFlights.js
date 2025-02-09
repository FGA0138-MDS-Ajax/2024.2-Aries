
// Seleciona os elementos flightCard para abrir o modal de visualização
const openModalBtns = document.querySelectorAll(".flightCard");

openModalBtns.forEach((btn) => {
    const modal = btn.querySelector(".modalViewFlight");

    if (!modal) return;

    // Evento para abrir o modal de visualização apenas se o clique for direto no flightCard
    btn.addEventListener("click", function (event) {
        if (event.target === btn) {
            modal.style.display = "block";
        }
    });

    const closeModalViewBtns = modal.querySelectorAll(".closeModalBtnView");

    closeModalViewBtns.forEach((closeBtn) => {
        closeBtn.addEventListener("click", (event) => {
            event.stopPropagation(); // Impede que o clique se propague para o flightCard
            modal.style.display = "none"; // Fecha o modal
        });
    });

    // Se houver botões dentro do modal para fechar (ou outras ações), você pode gerenciar assim:
    const closeForEdit = modal.querySelectorAll(".editBtn");

    closeForEdit.forEach((closeBtn) => {
        closeBtn.addEventListener("click", (event) => {
            event.stopPropagation(); // Impede que o clique se propague para o flightCard
            modal.style.display = "none"; // Fecha o modal de visualização
        });
    });
});
