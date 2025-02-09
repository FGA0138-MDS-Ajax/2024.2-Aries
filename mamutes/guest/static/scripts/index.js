const carouselTrack = document.querySelector('.carousel-track');
const carouselItems = document.querySelectorAll('.carousel-item');
const totalItems = carouselItems.length;

const itemWidth = carouselItems[0].offsetWidth;
const gap = 16; // Espaço entre os itens
const fullItemWidth = itemWidth + gap;

let offset = 0;
const speed = 1; // Velocidade do carrossel
let isPaused = false;

function moveCarousel() {
    if (!isPaused) {
        offset -= speed;

        // Quando o carrossel chegar ao final, move o primeiro item para o final
        if (offset <= -fullItemWidth) {
            carouselTrack.appendChild(carouselTrack.firstElementChild);
            offset += fullItemWidth;
        }

        // Aplica a transformação ao carrossel
        carouselTrack.style.transition = 'none';
        carouselTrack.style.transform = `translateX(${offset}px)`;

        // Adiciona uma transição suave após o movimento
        setTimeout(() => {
            carouselTrack.style.transition = 'transform 0.5s ease';
        }, 100);
    }

    requestAnimationFrame(moveCarousel);
}

// Pausa o carrossel quando o mouse está sobre ele
carouselTrack.addEventListener('mouseover', () => {
    isPaused = true;
});

// Retoma o carrossel quando o mouse sai
carouselTrack.addEventListener('mouseout', () => {
    isPaused = false;
});

// Inicia o carrossel
moveCarousel();