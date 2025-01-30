
// função para ao clicar, os filtros mudarem de cor
function selectWord(clickedWord) {

    const tabContent = document.querySelectorAll('.tabContent');
    tabContent.forEach(word => word.classList.remove('active'));
    
    clickedWord.classList.add('active');
}

document.addEventListener("click", (e) => {
    const event = e.target;
    const announcement = document.querySelector(".announcement");
    const eventful = document.querySelector(".event");
    
    if (event.id == "announcement"){
        eventful.style.display = "none";
        announcement.style.display = "flex";
    }
    if (event.id == "event"){
        announcement.style.display = "none";
        eventful.style.display = "flex";
    }
    if (event.id == "all"){
        announcement.style.display = "flex";
        eventful.style.display = "flex";
    }

})
