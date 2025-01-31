

// document.addEventListener("click", (e)=>{
//     eve = e.target;

//     modal = eve.closest(".modal")
//     miniModal = modal.querySelector(".mini-modal")
//     console.log(modal)
//     console.log(miniModal);

//     if(miniModal){
//       alert("oi")
        
//         if(miniModal.style.display === "block"){
//           miniModal.style.display = 'none';
//         } else {
//           miniModal.style.display = 'blox';
//         }
//     }

// })



// const openMiniModalBtn = document.querySelector(".plus-people");
// const miniModal = document.querySelector(".mini-modal");

// console.log(openMiniModalBtn)

// // Abre/fecha o modal de adicionar membros
// openMiniModalBtn.addEventListener("click", function(event) {
//     event.stopPropagation();
//     miniModal.style.display = (miniModal.style.display === "block") ? "none" : "block";
// });

// // Fechar o mini modal ao clicar fora dele
// document.addEventListener("click", function(event) {
//     if (!miniModal.contains(event.target) && event.target !== openMiniModalBtn) {
//         miniModal.style.display = "none";
//     }
// });

// Simulando um progresso de 3 segundos
// $(document).ready(function() {
    // $('.progress-bar').addClass('active');
// });
