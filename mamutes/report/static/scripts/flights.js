const svg = document.querySelector("#svg")
const textFilter = document.querySelector(".cancelLabel")
const black = document.querySelector("#svgAlt")

const btnFilter = document.querySelector(".submitCancelBotao")
    btnFilter.addEventListener("click", () => {
        btnFilter.classList.toggle("clicked")
        if (btnFilter.style.border !== "none"){
            btnFilter.style.border = "none";
        } else{
            btnFilter.style.border = "1px solid #717171";
        }
        textFilter.classList.toggle("clickedText")
        if (svg.style.display !== "none"){
            svg.style.display = "none";
            black.style.display = "flex";
        }
        else if (black.style.display !== "none"){
            black.style.display = "none";
            svg.style.display = "flex";
        }
    })


const modal = document.getElementById('modal');
const openModalBtn = document.getElementById('openModalBtn');
const closeModalBtn = document.getElementById('closeModalBtn');
openModalBtn.addEventListener('click', () => {
modal.style.display = 'flex';
});

closeModalBtn.addEventListener('click', () => {
modal.style.display = 'none';
});

window.addEventListener('click', (event) => {
if (event.target === modal) {
    modal.style.display = 'none';
}
});