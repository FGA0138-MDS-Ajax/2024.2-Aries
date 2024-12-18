document.addEventListener('DOMContentLoaded', () => {
    const groups = document.querySelectorAll('.grid-item');
    const balls = document.querySelectorAll('.moving-ball');

    balls.forEach((ball, index) => {
        const group = groups[Math.floor(index / 2)]; // Cada grupo contém 2 bolas
        const groupWidth = group.offsetWidth;
        const groupHeight = group.offsetHeight;
        const ballWidth = ball.offsetWidth;
        const ballHeight = ball.offsetHeight;

        // Posições iniciais aleatórias
        let posX = Math.random() * (groupWidth - ballWidth);
        let posY = Math.random() * (groupHeight - ballHeight);

        // Velocidades aleatórias para cada bola
        let speedX = Math.random(); // Entre 2 e 8
        let speedY = Math.random(); // Entre 2 e 8

        // Direções aleatórias
        speedX *= Math.random() < 0.5 ? 1 : -1;
        speedY *= Math.random() < 0.5 ? 1 : -1;

        function animateBall() {
            posX += speedX;
            posY += speedY;

            // Refletir nas bordas
            if (posX <= 0 || posX + ballWidth >= groupWidth) {
                speedX *= -1; // Inverte a direção horizontal
            }
            if (posY <= 0 || posY + ballHeight >= groupHeight) {
                speedY *= -1; // Inverte a direção vertical
            }

            // Atualiza a posição da bola
            ball.style.transform = `translate(${posX}px, ${posY}px)`;

            requestAnimationFrame(animateBall);
        }

        animateBall(); // Inicia a animação
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const closeIcon = document.querySelector(".closeIcon");
    const menu = document.querySelector(".menu");
    const sidebarMenu = document.querySelector(".sidebarMenu");
    const buttonHamb = document.querySelector(".hamb-navbar");
    const navSideBar = document.querySelectorAll(".navSideBar");
    const itemMenu = document.querySelector(".itemMenu");

    buttonHamb.addEventListener("click", () => {
        menu.classList.add("shown");
        sidebarMenu.classList.add("shown");
    });

    closeIcon.addEventListener("click", () => {
        menu.classList.remove("shown");
        sidebarMenu.classList.remove("shown");
    });

    navSideBar.forEach(itemMenu => {
        itemMenu.addEventListener("click", () => {
            menu.classList.remove("shown");
            sidebarMenu.classList.remove("shown");
        });
    });
});


const accordions = document.querySelectorAll(".accordion");

accordions.forEach(accordion => {
    accordion.addEventListener("click", () => {
        accordion.classList.toggle("active");
    })
})