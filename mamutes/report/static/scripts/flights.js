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
});

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

