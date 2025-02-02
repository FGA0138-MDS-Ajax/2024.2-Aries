document.addEventListener("DOMContentLoaded", function () {
    const openModalAddBtn = document.getElementById("openModalAddBtn"); // js do modal add-reunião
    const closeModalAddBtn = document.getElementById("closeModalAddBtn");
    const modalAdd = document.getElementById("modalAdd");

    openModalAddBtn.addEventListener("click", function (event) {
        event.preventDefault();
        // console.log("abrindo o modal");
        modalAdd.style.display = "flex";
    });

    closeModalAddBtn.addEventListener("click", function () {
        // console.log("fechando o modal");
        modalAdd.style.display = "none";
    });

    window.addEventListener("click", function (event) {
        if (event.target === modalAdd) {
            modalAdd.style.display = "none";
        }
    });

    const openModalFilterBtn = document.getElementById("openModalFilterBtn"); // js do modal filtro
    const closeModalFilterBtn = document.getElementById("closeModalFilterBtn");
    const modalFilter = document.getElementById("modalFilter");

    openModalFilterBtn.addEventListener("click", function (event) {
        event.preventDefault();
        // console.log("abrindo o modal");
        modalFilter.style.display = "flex";
    });

    closeModalFilterBtn.addEventListener("click", function () {
        // console.log("fechando o modal");
        modalFilter.style.display = "none";
    });

    window.addEventListener("click", function (event) {
        if (event.target === modalFilter) {
            modalFilter.style.display = "none";
        }
    });
});
