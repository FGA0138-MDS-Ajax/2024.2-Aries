(function(){
    // document.body.addEventListener("click", (e)=>{
    //     const event = e.target;

    //     alert(event.outerHTML)

    // })
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