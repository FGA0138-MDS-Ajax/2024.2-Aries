const submitCancelBotao = document.querySelector(".submitCancelBotao");
const modalFilter = document.querySelector(".modalFilter");
const closeModalBtn = document.getElementById("closeModalBtn");

modalFilter.style.display = "none";

submitCancelBotao.addEventListener("click", function (event) {
    const isVisible = modalFilter.style.display === "flex";

    modalFilter.style.display = isVisible ? "none" : "flex";
    submitCancelBotao.classList.toggle("active", !isVisible);

    if (!isVisible) {
        document.addEventListener("click", closeOnClickOutside);
    }
});

closeModalBtn.addEventListener("click", function () {
    modalFilter.style.display = "none";
    submitCancelBotao.classList.remove("active");
    document.removeEventListener("click", closeOnClickOutside);
});

function closeOnClickOutside(event) {
    if (!modalFilter.contains(event.target) && !submitCancelBotao.contains(event.target)) {
        modalFilter.style.display = "none";
        submitCancelBotao.classList.remove("active");
        document.removeEventListener("click", closeOnClickOutside);
    }
}


// abrir modal novo flight
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

})

// rating de voo
document.addEventListener("DOMContentLoaded", function () {
    const stars = document.querySelectorAll(".star");
    const ratingText = document.getElementById("ratingText");
    const ratings = ["Ruim", "Regular", "Bom", "Muito Bom", "Ótimo"];
    stars.forEach((star, index) => {
        star.addEventListener("click", function () {
            let selectedValue = this.getAttribute("data-value");
            stars.forEach((s, i) => {
                if (i < selectedValue) {
                    s.classList.add("selected");
                } else {
                    s.classList.remove("selected");
                }
            });
            ratingText.textContent = ratings[selectedValue - 1];
        });
    });
});



// mostra div adcional se checkbox marcado
document.addEventListener("DOMContentLoaded", function () {
    const checkbox = document.getElementById("accidentCheckbox");
    const extraContent = document.getElementById("additionalInputs");

    checkbox.addEventListener("change", function () {
        if (this.checked) {
            extraContent.classList.remove("accidentBox");
        } else {
            extraContent.classList.add("accidentBox");
        }
    });
});

// estilização para dropdown
function showOptions(e) {
    let divOptions = document.getElementById("divOptions");
    if (divOptions.style.display == "none" || divOptions.style.display == "") {
        divOptions.style.display = "inline-block";
    } else {
        divOptions.style.display = "none";
    }
}
function clickMe(e) {
    console.log('click me');
    e.stopPropagation();
}
function hideOptions(e) {
    let divOptions = document.getElementById("divOptions");

    if (divOptions.contains(e.target)) {
        divOptions.style.display = "inline-block";
    } else {
        divOptions.style.display = "none";
    }
}

document.addEventListener("DOMContentLoaded", function () {
    let checkbox = document.querySelectorAll("#divOptions input");
    let inputCheckbox = document.getElementById("inputCheckbox");

    for (let i = 0; i < checkbox.length; i++) {
        checkbox[i].addEventListener("change", (e) => {
            if (e.target.checked == true) {
                if (inputCheckbox.value == "") {
                    inputCheckbox.value = checkbox[i].value;
                } else {
                    inputCheckbox.value += `,${checkbox[i].value}`;
                }
            } else {
                let values = inputCheckbox.value.split(",");

                for (let r = 0; r < values.length; r++) {
                    if (values[r] == e.target.value) {
                        values.splice(r, 1);
                    }
                }
                inputCheckbox.value = values;
            }
        });
    }
});


const openModalBtns = document.querySelectorAll(".flightCard");

openModalBtns.forEach((btn) => {
    const modal = btn.querySelector(".modalEditFlight");

    if (!modal) return;

    // Evento para abrir o modal
    btn.addEventListener("click", function () {
        modal.style.display = "block";
    });

    const closeModalViewBtns = modal.querySelectorAll(".closeModalBtnEditFlight");

    closeModalViewBtns.forEach((closeBtn) => {
        closeBtn.addEventListener("click", (event) => {
            event.stopPropagation(); // Impede que o clique se propague para o flightCard
            modal.style.display = "none"; // Fecha o modal
        });
    });
});

        
