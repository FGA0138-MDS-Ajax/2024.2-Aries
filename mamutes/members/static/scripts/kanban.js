const modal = document.getElementById("modal");
const openModalBtn = document.querySelectorAll("#buttonNewTask");
const closeModalBtn = document.getElementById("close-modal");
// Função para abrir o modal

openModalBtn.forEach((btn) => {
  btn.addEventListener("click", function() {
    modal.style.display = "flex"; // Exibe o modal
  });
});

// Função para fechar o modal
closeModalBtn.addEventListener("click", function() {
  modal.style.display = "none"; // Esconde o modal
});
// Fechar o modal se clicar fora do conteúdo
window.addEventListener("click", function(event) {
  if (event.target === modal) {
    modal.style.display = "none"; // Esconde o modal se clicar fora dele
  }
});

const openMiniModalBtn = document.getElementById("plus-people");
const miniModal = document.getElementById("miniModal");
const closeMiniModalBtn = document.getElementById("closeMiniModalBtn");

openMiniModalBtn.addEventListener("click", function() {
        miniModal.style.display = "block";
    });

    // Fechamento do modal
    closeMiniModalBtn.addEventListener("click", function() {
        miniModal.style.display = "none";
    });

    // Fechar o modal se clicar fora da área do modal
    window.addEventListener("click", function(event) {
        if (event.target === miniModal) {
            miniModal.style.display = "none";
        }
    });


    $(document).ready(function() {
      // Simulando um progresso de 3 segundos
      $('.progress-bar').addClass('active');
  });