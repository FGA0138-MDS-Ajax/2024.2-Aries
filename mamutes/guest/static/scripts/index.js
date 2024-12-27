const carouselTrack = document.querySelector('.carousel-track');
const carouselItems = document.querySelectorAll('.logo-apoiador');
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




document.addEventListener('DOMContentLoaded', () => {
    const tracker = document.querySelector('.apoiadores-tracker');
    const logos = Array.from(document.querySelectorAll('.logo-apoiador'));
    const prevButton = document.querySelectorAll('.seta-carrossel-apoi')[0];
    const nextButton = document.querySelectorAll('.seta-carrossel-apoi')[1];

    let currentIndex = 0; 
    const visibleLogos = 4; 
    const totalLogos = logos.length;
    const logoWidth = logos[0]?.offsetWidth || 0; 
    const gap = 16; 
    const autoSlideInterval = 3000; 

    
    const updateCarousel = () => {
        tracker.style.transition = 'transform 0.5s ease';
        const offset = currentIndex * (logoWidth + gap);
        tracker.style.transform = `translateX(-${offset}px)`;
    };

    const nextSlide = () => {
        currentIndex += 1;

        if (currentIndex >= totalLogos - visibleLogos + 1) {
            currentIndex = 0; 
        }

        updateCarousel();
    };

    const prevSlide = () => {
        if (currentIndex > 0) {
            currentIndex -= 1;
        } else {
            currentIndex = totalLogos - visibleLogos; 
        }
        updateCarousel();
    };

    nextButton.addEventListener('click', nextSlide);
    prevButton.addEventListener('click', prevSlide);

    let autoSlide = setInterval(nextSlide, autoSlideInterval);

    updateCarousel();
});


