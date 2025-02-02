const showModalBtn = document.querySelector(".show-modal");
const bottomSheet = document.querySelector(".bottom-sheet");
const sheetOverlay = bottomSheet.querySelector(".sheet-overlay");
const sheetContent = bottomSheet.querySelector(".content");
const dragIcon = bottomSheet.querySelector(".drag-icon");

let isDragging = false, startY, startHeight;

const showBottomSheet = () => {
    bottomSheet.classList.add("show");
    document.body.style.overflowY = "hidden";
    
    const savedHeight = localStorage.getItem("bottomSheetHeight") || "50";
    updateSheetHeight(parseInt(savedHeight));

    localStorage.setItem("bottomSheetState", "open");
};

const hideBottomSheet = () => {
    bottomSheet.classList.remove("show");
    document.body.style.overflowY = "auto";
    localStorage.setItem("bottomSheetState", "closed");
};

const restoreBottomSheetState = () => {
    const savedState = localStorage.getItem("bottomSheetState");
    const savedHeight = localStorage.getItem("bottomSheetHeight");

    if (savedState === "open") {
        bottomSheet.classList.add("show");
        document.body.style.overflowY = "hidden";
        updateSheetHeight(parseInt(savedHeight) || 50);
    }
};

const updateSheetHeight = (height) => {
    sheetContent.style.height = `${height}vh`;
    bottomSheet.classList.toggle("fullscreen", height === 100);
    localStorage.setItem("bottomSheetHeight", height);
};

const dragStart = (e) => {
    isDragging = true;
    startY = e.pageY || e.touches?.[0].pageY;
    startHeight = parseInt(sheetContent.style.height);
    bottomSheet.classList.add("dragging");
};

const dragging = (e) => {
    if (!isDragging) return;
    const delta = startY - (e.pageY || e.touches?.[0].pageY);
    const newHeight = startHeight + (delta / window.innerHeight) * 100;
    updateSheetHeight(newHeight);
};

const dragStop = () => {
    isDragging = false;
    bottomSheet.classList.remove("dragging");
    const sheetHeight = parseInt(sheetContent.style.height);
    
    if (sheetHeight < 25) {
        hideBottomSheet();
    } else if (sheetHeight > 75) {
        updateSheetHeight(100);
    } else {
        updateSheetHeight(50);
    }
};

document.addEventListener("DOMContentLoaded", restoreBottomSheetState);

dragIcon.addEventListener("mousedown", dragStart);
document.addEventListener("mousemove", dragging);
document.addEventListener("mouseup", dragStop);
dragIcon.addEventListener("touchstart", dragStart);
document.addEventListener("touchmove", dragging);
document.addEventListener("touchend", dragStop);
sheetOverlay.addEventListener("click", hideBottomSheet);
showModalBtn.addEventListener("click", showBottomSheet);
