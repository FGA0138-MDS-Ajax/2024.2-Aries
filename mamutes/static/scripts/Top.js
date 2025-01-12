const button = document.querySelector('.ImgName');
const popup = document.querySelector('.Popup');
const notificationButton = document.querySelector('.ButtonNotif');
const notificationPopup = document.querySelector('.Notifications');

button.addEventListener('click', (event) => {
    // Evita que o clique na imagem feche o popup imediatamente
    event.stopPropagation();

    if (notificationPopup.classList.contains('is-visible')) {
        notificationPopup.classList.remove('is-visible');
        notificationButton.classList.remove('active');
    }

    // Alterna a classe 'active' para mudar o estilo da imagem
    button.classList.toggle('active');

    // // Alterna a classe 'show' para mostrar/ocultar o popup
    popup.classList.toggle('show');
});

notificationButton.addEventListener('click', (event) => {
    // Evita que o clique na imagem feche o popup imediatamente
    event.stopPropagation();

    if (popup.classList.contains('show')) {
        popup.classList.remove('show');
        button.classList.remove('active');
    }

    // Alterna a classe 'active' para mudar o estilo da imagem
    // button.classList.toggle('active');

    // // Alterna a classe 'show' para mostrar/ocultar o popup
    popup.classList.toggle('show');
});

// Adiciona um evento de clique no documento para esconder o popup quando clicar fora
document.addEventListener('click', (event) => {
    // Verifica se o clique foi fora da imagem e do popup
    if (!button.contains(event.target) && !popup.contains(event.target)) {
        popup.classList.remove('show'); // Esconde o popup
        button.classList.remove('active'); // Remove a classe 'active' da imagem
    }
});

// Adiciona evento de clique no botão para alternar a visibilidade das notificações
notificationButton.addEventListener('click', (event) => {
    event.stopPropagation(); // Evita que o clique no botão feche a notificação

    // Alterna a classe 'is-visible' para mostrar/ocultar as notificações
    notificationPopup.classList.toggle('is-visible');

    // Alterna a classe 'active' para mudar o estilo do botão de notificação
    notificationButton.classList.toggle('active');
});

// Adiciona evento de clique no documento para esconder as notificações quando clicar fora
document.addEventListener('click', (event) => {
    // Verifica se o clique foi fora do botão de notificação e do popup
    if (!notificationButton.contains(event.target) && !notificationPopup.contains(event.target)) {
        notificationPopup.classList.remove('is-visible'); // Esconde o popup
        notificationButton.classList.remove('active'); // Remove a classe 'active' do botão
    }
});
