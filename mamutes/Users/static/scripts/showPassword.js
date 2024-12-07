const passwordInput = document.querySelector('input[name="password"]');
const eyeOpen = document.getElementById('pwdEyeOpen');
const eyeClose = document.getElementById('pwdEyeClose');

eyeOpen.addEventListener('click', () => {
    passwordInput.type = 'text'; 
    eyeOpen.style.display = 'none';
    eyeClose.style.display = 'flex';
});

eyeClose.addEventListener('click', () => {
    passwordInput.type = 'password';
    eyeClose.style.display = 'none';
    eyeOpen.style.display = 'flex'; 
});
