// Função para ao clicar, os filtros mudarem de cor
function selectWord(clickedWord) {
    const tabContent = document.querySelectorAll('.tabContent');
    tabContent.forEach(word => word.classList.remove('active'));
    clickedWord.classList.add('active');
}

document.addEventListener("click", (e) => {
    const event = e.target;
    const announcements = document.querySelectorAll(".announcement");
    const events = document.querySelectorAll(".event");

    if (event.id === "announcement") {
        announcements.forEach(announcement => announcement.style.display = "flex");
        events.forEach(eventful => eventful.style.display = "none");
    } 
    else if (event.id === "event") {
        announcements.forEach(announcement => announcement.style.display = "none");
        events.forEach(eventful => eventful.style.display = "flex");
    } 
    else if (event.id === "all") {
        announcements.forEach(announcement => announcement.style.display = "flex");
        events.forEach(eventful => eventful.style.display = "flex");
    }
});