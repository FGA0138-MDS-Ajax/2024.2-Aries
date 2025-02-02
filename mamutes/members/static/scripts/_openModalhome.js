(function(){
    const btnModal = document.querySelector('#btnModal');
    const modal  = document.querySelector('#modal');
    const btnClose = document.querySelector('#btnClose');

    btnModal.addEventListener("click", ()=>{
        modal.showModal();
    });
    btnClose.addEventListener("click", ()=>{
        modal.close();
    });
    
})();

const input = document.querySelector('.inputDescriptionPost');

    input.addEventListener('input', () => {
      input.style.height = 'auto'; 
      input.style.height = input.scrollHeight + 'px'; 
    });


const eventCheckbox = document.getElementById("eventcheckbox");
const additionalInputs = document.querySelector(".eventBox");
    
    eventCheckbox.addEventListener("change", () => {
        if (eventCheckbox.checked) {
            additionalInputs.style.display = "flex";
        } else {
            additionalInputs.style.display = "none";
        }
    });
    

const onlineCheckbox = document.getElementById("onlineCheckbox");
const locationInput = document.getElementById("locationEvent");

    onlineCheckbox.addEventListener("change", () => {
        if (onlineCheckbox.checked) {
            locationInput.disabled = true; 
            locationInput.value = ""; 
        } else {
            locationInput.disabled = false; 
        }
    });
    
    document.addEventListener("DOMContentLoaded", function() {
        const eventCheckbox = document.getElementById("eventcheckbox");
        const dateInput = document.getElementById("dateEvent");

        // Função para alternar o atributo 'required' no input de data
        function toggleRequired() {
            if (eventCheckbox.checked) {
                dateInput.setAttribute("required", "required");
            } else {
                dateInput.removeAttribute("required");
            }
        }

        // Atualiza ao carregar a página
        toggleRequired();

        // Atualiza ao mudar o estado do checkbox
        eventCheckbox.addEventListener("change", toggleRequired);
    });