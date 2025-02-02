const buttonProfile = document.querySelector('.ImgName');
const modalProfile = document.querySelector('.Popup');

function isClickOutside(element, target) {
    return !element.contains(target);
}

buttonProfile.addEventListener("click", (e) => {
    e.stopPropagation(); 

    if (modalProfile.style.display === "flex") {
        buttonProfile.style.background = "#fefefe";
        modalProfile.style.display = "none";
    } else { 
        buttonProfile.style.background = "#f2f2f2";
        modalProfile.style.display = "flex";
    }
});

document.addEventListener("click", (e) => {
    if (modalProfile.style.display === "flex" && isClickOutside(modalProfile, e.target)) {
        buttonProfile.style.background = "#fefefe";
        modalProfile.style.display = "none";
    }
});
