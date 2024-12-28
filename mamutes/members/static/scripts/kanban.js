const modal = document.getElementById("modal");
const openModalBtn = document.querySelector(".text-wrapper-8");
const closeModalBtn = document.getElementById("close-modal");

// Função para abrir o modal
openModalBtn.addEventListener("click", function() {
  modal.style.display = "flex"; // Exibe o modal
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

