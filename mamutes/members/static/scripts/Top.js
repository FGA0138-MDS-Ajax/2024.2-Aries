const button = document.querySelector('.ImgName');
const popup = document.querySelector('.Popup');
const notificationButton = document.querySelector('.ButtonNotif');
const notificationPopup = document.querySelector('.Notifications');


button.addEventListener('click', (event) => {
    // Evita que o clique na imagem feche o popup imediatamente
    event.stopPropagation();

    // Alterna a classe 'show' para mostrar/ocultar o popup
    popup.classList.toggle('show');
});

// Adiciona um evento de clique no documento para esconder o popup quando clicar fora
document.addEventListener('click', (event) => {
    // Verifica se o clique foi fora da imagem e do popup
    if (!button.contains(event.target) && !popup.contains(event.target)) {
        popup.classList.remove('show'); // Esconde o popup
    }
});

// Adiciona evento de clique no botão para alternar a visibilidade das notificações
notificationButton.addEventListener('click', (event) => {
    event.stopPropagation(); // Evita que o clique no botão feche a notificação

    // Alterna a classe 'is-visible' para mostrar/ocultar as notificações
    notificationPopup.classList.toggle('is-visible');
});

// Adiciona evento de clique no documento para esconder as notificações quando clicar fora
document.addEventListener('click', (event) => {
    // Verifica se o clique foi fora do botão de notificação e do popup
    if (!notificationButton.contains(event.target) && !notificationPopup.contains(event.target)) {
        notificationPopup.classList.remove('is-visible'); // Esconde o popup
    }
});


