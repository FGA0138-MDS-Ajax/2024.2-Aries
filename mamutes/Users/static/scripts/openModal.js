(function(){
    const btnModal = document.querySelector('#btnModal');
    const modal  = document.querySelector('#modal');
    const btnClose = document.querySelector('#btnClose');
    const form = document.querySelector('#recoverAccountForm');
    const mensagemContainer = document.querySelector('#mensagemContainer');

    btnModal.addEventListener("click", ()=>{
        modal.showModal();
    });
    btnClose.addEventListener("click", ()=>{
        modal.close();
    });

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        const formData = new FormData(form);
        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
            },
        })
        .then(response => response.json())
        .then(data => {
            mensagemContainer.textContent = data.mensagem;
            if (data.success) {
                form.reset();
            }
        })
    });
})();