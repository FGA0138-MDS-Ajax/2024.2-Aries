document.getElementById("toggleButton").addEventListener("click", function() {
    const userEdit = document.getElementById("userEdit");
    const userDetails = document.getElementById("userDetails");
    if (userEdit.style.display === "none") {
        userEdit.style.display = "flex";
        userDetails.style.display = "none";
    } else {
        userEdit.style.display = "none";
    }
  });

  document.getElementById("userCancelar").addEventListener("click", function() {
    const userEdit = document.getElementById("userEdit");
    const userDetails = document.getElementById("userDetails");
    if (userEdit.style.display === "flex") {
        userEdit.style.display = "none";
        userDetails.style.display = "flex";
    } else {
        userEdit.style.display = "flex";
    }
  });
  
  // Selecionar os elementos
const currentPassword = document.getElementById("currentPassword");
const newPassword = document.getElementById("newPassword");
const confirmPassword = document.getElementById("confirmPassword");
const submitButton = document.getElementById("submitButton");
const errorMessage = document.getElementById("errorMessage");

// Função para verificar se os campos estão preenchidos e corretos
function validateForm() {
  const currentPasswordValue = currentPassword.value.trim();
  const newPasswordValue = newPassword.value.trim();
  const confirmPasswordValue = confirmPassword.value.trim();

  // Condição para habilitar o botão
  if (
    currentPasswordValue !== "" &&
    newPasswordValue !== "" &&
    confirmPasswordValue !== "" &&
    newPasswordValue === confirmPasswordValue
  ) {
    submitButton.disabled = false;
    errorMessage.style.display = "none"; // Ocultar mensagem de erro
  } else {
    submitButton.disabled = true;
    // Mostrar mensagem de erro se as senhas não coincidirem
    if (newPasswordValue !== confirmPasswordValue && confirmPasswordValue !== "") {
      errorMessage.style.display = "flex";
    } else {
      errorMessage.style.display = "none";
    }
  }
}

// Adicionar evento de input para validar os campos dinamicamente
[currentPassword, newPassword, confirmPassword].forEach((input) =>
  input.addEventListener("input", validateForm)
);


  document.getElementById("submitButton").addEventListener("click", function() {
    const msg = document.getElementById("Message");
    msg.style.display = "flex";
        
  });