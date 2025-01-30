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

// Abre/fecha o modal de adicionar membros
openMiniModalBtn.addEventListener("click", function(event) {
    event.stopPropagation();
    miniModal.style.display = (miniModal.style.display === "block") ? "none" : "block";
});

// Fechar o mini modal ao clicar fora dele
document.addEventListener("click", function(event) {
    if (!miniModal.contains(event.target) && event.target !== openMiniModalBtn) {
        miniModal.style.display = "none";
    }
});

// Simulando um progresso de 3 segundos
$(document).ready(function() {
    $('.progress-bar').addClass('active');
});
