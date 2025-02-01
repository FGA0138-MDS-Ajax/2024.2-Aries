const submitCancelBotao = document.querySelector(".submitCancelBotao");
    const modalFilter = document.querySelector(".modalFilter");
    const closeModalBtn = document.getElementById("closeModalBtn");

    modalFilter.style.display = "none";

    submitCancelBotao.addEventListener("click", function () {
        const isVisible = modalFilter.style.display === "flex";

        modalFilter.style.display = isVisible ? "none" : "flex";
        submitCancelBotao.classList.toggle("active", !isVisible);
    });

    closeModalBtn.addEventListener("click", function () {
        modalFilter.style.display = "none";
        submitCancelBotao.classList.remove("active");
    });

// document.addEventListener("click", (e) => {
//     let target = e.target;

//     if (target.classList.contains("btns")) {
//         alert('MAUARA')
//         let modal = document.querySelector(".modal");                        
//         // if (!modalPrime.modalHTML) {
//         //     modalPrime.modalHTML = modal.innerHTML;
//         // }      
//         if (modal) {
//             modal.showModal();
//             alert('OLA')
//         }
//         alert('OI MUNDO')
//     }
// })

document.addEventListener("DOMContentLoaded", function () {

    const openModalBtn = document.getElementById("openModalBtn");
    const modal = document.getElementById("modalNewFlight");
    const closeModalBtn = document.getElementById("closeModalBtnNew");

    openModalBtn.addEventListener("click", function () {
        modal.style.display = "block";
    });

    closeModalBtn.addEventListener("click", function () {
        modal.style.display = "none";
    });

    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});
