(function(){
    const localization = window.location.pathname;
    if(localization == '#processoSeletivo'){
        const processoSeletivo = document.querySelector("#processoSeletivo");
        processoSeletivo.style.color = 'red';
    }
})()