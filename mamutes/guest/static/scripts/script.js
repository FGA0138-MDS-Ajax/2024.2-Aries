document.addEventListener('DOMContentLoaded', () => {
    const groups = document.querySelectorAll('.grid-item');
    const balls = document.querySelectorAll('.moving-ball');

    balls.forEach((ball, index) => {
        const group = groups[Math.floor(index / 2)];
        const groupWidth = group.offsetWidth;
        const groupHeight = group.offsetHeight;
        const ballWidth = ball.offsetWidth;
        const ballHeight = ball.offsetHeight;

        let posX = Math.random() * (groupWidth - ballWidth);
        let posY = Math.random() * (groupHeight - ballHeight);

        let speedX = Math.random();
        let speedY = Math.random();

        speedX *= Math.random() < 0.5 ? 1 : -1;
        speedY *= Math.random() < 0.5 ? 1 : -1;

        function animateBall() {
            posX += speedX;
            posY += speedY;

            if (posX <= 0 || posX + ballWidth >= groupWidth) {
                speedX *= -1;
            }
            if (posY <= 0 || posY + ballHeight >= groupHeight) {
                speedY *= -1;
            }

            ball.style.transform = `translate(${posX}px, ${posY}px)`;

            requestAnimationFrame(animateBall);
        }

        animateBall();
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

