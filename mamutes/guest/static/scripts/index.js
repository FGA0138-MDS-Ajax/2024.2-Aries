const carouselTrack = document.querySelector('.carousel-track');
const carouselItems = document.querySelectorAll('.carousel-item');
const totalItems = carouselItems.length;

const itemWidth = carouselItems[0].offsetWidth;
const gap = 16;
const fullItemWidth = itemWidth + gap;

let offset = 0;
const speed = 1;
let isPaused = false;

function moveCarousel() {
    if (!isPaused) {
        offset -= speed;

        if (offset <= -fullItemWidth) {
            carouselTrack.appendChild(carouselTrack.firstElementChild);
            offset += fullItemWidth;
        }

        carouselTrack.style.transition = 'none';
        carouselTrack.style.transform = `translateX(${offset}px)`;

        setTimeout(() => {
            carouselTrack.style.transition = 'transform 0.5s ease';
        }, 100);
    }

    requestAnimationFrame(moveCarousel);
}

carouselTrack.addEventListener('mouseover', () => {
    isPaused = true;
});

carouselTrack.addEventListener('mouseout', () => {
    isPaused = false;
});


moveCarousel();

