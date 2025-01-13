const buttonNotification = document.querySelector('.ButtonNotif');
const buttonProfile = document.querySelector('.ImgName');

const modalNotificatin = document.querySelector('.Notifications');
const modalProfile = document.querySelector('.Popup');

const newNotif =  document.querySelector('.DotNotif');

function isClickOutside(element, target) {
    return !element.contains(target);
}


buttonNotification.addEventListener("click", (e) => {
    e.stopPropagation(); 
    if (modalNotificatin.style.display === "flex") {
        buttonNotification.style.background = "#fefefe";
        modalNotificatin.style.display = "none";
    } else {
        buttonNotification.style.background = "#f2f2f2";
        newNotif.style.display = "none";
        modalNotificatin.style.display = "flex";
        modalProfile.style.display = "none";
    }
});


buttonProfile.addEventListener("click", (e) => {
    e.stopPropagation(); 

    // se o modal estiver aberto, quando clicado ele fecha
    if (modalProfile.style.display === "flex") {
        buttonProfile.style.background = "#fefefe";
        modalProfile.style.display = "none";
    } else { //se o modal estiver fechado, quando clicado ele abre
        buttonProfile.style.background = "#f2f2f2";
        modalProfile.style.display = "flex";
        modalNotificatin.style.display = "none";
    }
});

document.addEventListener("click", (e) => {
    //se os modais estiverem abertos e o clique não foi em algum deles, é porque clicou fora, logo fecha
    if (modalNotificatin.style.display === "flex" && isClickOutside(modalNotificatin, e.target)) {
        buttonNotification.style.background = "#fefefe";
        modalNotificatin.style.display = "none";
    }
    if (modalProfile.style.display === "flex" && isClickOutside(modalProfile, e.target)) {
        buttonProfile.style.background = "#fefefe";
        modalProfile.style.display = "none";
    }
});
