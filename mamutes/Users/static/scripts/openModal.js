(function(){
    const btnModal = document.querySelector('#btnModal');
    const modal  = document.querySelector('#modal');
    const btnClose = document.querySelector('#btnClose');

    btnModal.addEventListener("click", ()=>{
        modal.showModal();
    });
    btnClose.addEventListener("click", ()=>{
        modal.close();
    })
})()