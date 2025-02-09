const cardsContainer = document.querySelector('.carrosselAirPlaneCards');
const cards = Array.from(document.querySelectorAll('.cardAirPlane'));
const indicatorsContainer = document.querySelector('.carousel-indicators');

let idx = 1;

const firstClone = cards[0].cloneNode(true);
const lastClone = cards[cards.length - 1].cloneNode(true);

firstClone.classList.add('clone');
lastClone.classList.add('clone');

cardsContainer.appendChild(firstClone);
cardsContainer.prepend(lastClone);

const allCards = document.querySelectorAll('.carrosselAirPlaneCards .cardAirPlane');

cards.forEach((_, index) => {
    const indicator = document.createElement('span');
    indicator.classList.add('indicator');
    if (index === 0) indicator.classList.add('active');
    indicator.dataset.index = index;
    indicatorsContainer.appendChild(indicator);
});

const indicators = document.querySelectorAll('.indicator');

function updateCarousel(animated = true) {
    const cardWidth = allCards[0].offsetWidth;
    const offset = (cardsContainer.offsetWidth / 2) - (cardWidth / 2);

    if (animated) {
        cardsContainer.style.transition = "transform 0.5s ease-in-out";
    } else {
        cardsContainer.style.transition = "none";
    }

    cardsContainer.style.transform = `translateX(${-idx * cardWidth + offset}px)`;

    allCards.forEach((card, index) => {
        card.classList.toggle('expanded', index === idx);
    });

    indicators.forEach((indicator, index) => {
        indicator.classList.toggle('active', index === (idx - 1));
    });
}

indicators.forEach((indicator, index) => {
    indicator.addEventListener('click', () => {
        idx = index + 1;
        updateCarousel();
    });
});

setInterval(() => {
    idx++;
    updateCarousel();

    setTimeout(() => {
        if (idx >= allCards.length - 1) {
            idx = 1;
            updateCarousel(false);
        }
    }, 500);
}, 3000);

updateCarousel(false);
