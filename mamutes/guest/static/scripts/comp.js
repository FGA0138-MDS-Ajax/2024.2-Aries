const cardsContainer = document.querySelector('.carrosselAirPlaneCards');
const cards = document.querySelectorAll('.cardAirPlane');
let idx = 0;
const indicators = document.querySelectorAll('.indicator');

function carrossel() {
  idx++;
  if (idx > cards.length - 3) {
    idx = 0;
  }

  updateCarousel();
}

function updateCarousel() {
  const cardWidth = cards[0].offsetWidth + 24; 
  cardsContainer.style.transform = `translateX(${-idx * cardWidth}px)`;

  const middleCardIdx = idx + 1;

  cards.forEach((card, index) => {
    if (index === middleCardIdx) {
      card.classList.add('expanded');
    } else {
      card.classList.remove('expanded');
    }
  });

  const groupIdx = Math.floor(idx / 3); 
  indicators.forEach((indicator, index) => {
    indicator.classList.toggle('active', index === groupIdx);
  });
}

indicators.forEach((indicator, index) => {
  indicator.addEventListener('click', () => {
    idx = index * 3; 
    updateCarousel();
  });
});

setInterval(carrossel, 3000); 