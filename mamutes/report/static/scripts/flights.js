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








document.addEventListener("DOMContentLoaded", function () {
    const checkboxes = document.querySelectorAll(".accidentCheckbox");

    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener("change", function () {
            const div = checkbox.closest('.form');
            const showAccidentForm = div.querySelector('.additionalInputs');
            const fields = showAccidentForm.querySelectorAll("input, textarea");

            if (this.checked) {
                showAccidentForm.classList.remove("accidentBox");
                fields.forEach(function(field) {
                    field.required = true;
                });
            } else {
                showAccidentForm.classList.add("accidentBox");
                fields.forEach(function(field) {
                    field.required = false;
                });
            }
        });
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


