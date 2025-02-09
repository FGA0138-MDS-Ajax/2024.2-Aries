// Seleciona todos os botões de editar
const editBtns = document.querySelectorAll('.editBtn');
console.log(editBtns);

// Adiciona um evento de clique para cada botão de editar
editBtns.forEach(btn => {
  btn.addEventListener('click', function (event) {
    // Impede que o clique no botão de editar propague para o flightCard
    event.stopPropagation();

    // Encontra o card mais próximo do botão clicado
    const card = this.closest('.flightCard');
    
    // Encontra os modais de edição e visualização dentro do mesmo card
    const modalEdit = card.querySelector('.modalEditFlight');
    const modalView = card.querySelector('.modalViewFlight');
    
    // Fecha o modal de visualização, se ele estiver aberto
    if (modalView && modalView.style.display !== 'none') {
        modalView.style.display = 'none';
    }
    
    // Abre o modal de edição com display "flex"
    if (modalEdit) {
        modalEdit.style.display = 'block';
    }
  });
});
document.addEventListener("click", (e) => {
    if (e.target.classList.contains("closeModalBtnEdit")) {
      const modalEdit = e.target.closest(".modalEditFlight");
      if (modalEdit) {
        modalEdit.style.display = "none";
      }
    }
  });

  function fixNumberInputsInDocument() {
    // Seleciona todos os inputs do tipo number
    const numberInputs = document.querySelectorAll('input[type="number"]');

    numberInputs.forEach(function(input) {
      // Tenta obter o valor via propriedade; se estiver vazio (por conta de valor inválido), usa o atributo
      let currentValue = input.value || input.getAttribute('value');

      // Se existir valor e ele contiver vírgula, substitui por ponto
      if (currentValue && currentValue.indexOf(',') !== -1) {
        const newValue = currentValue.replace(/,/g, '.');
        input.value = newValue;
        input.setAttribute('value', newValue);
      }

      // Adiciona um listener para interceptar a digitação e substituir vírgulas por pontos
      input.addEventListener('input', function() {
        if (input.value.indexOf(',') !== -1) {
          input.value = input.value.replace(/,/g, '.');
        }
      });
    });
  }

  // Executa o método assim que o DOM estiver totalmente carregado
  document.addEventListener('DOMContentLoaded', fixNumberInputsInDocument);