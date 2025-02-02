// ! POR FAVOR NÃO MEXER NO JS de editCard e nem ViewCard se não souber oque está fazendo
// Objetivo do código:
// abre e fecha o modal viewCard e envia as atualizações da checkbox (se foi selecionada ou não) via AJAX (submissão de dados sem reload na atual página)

(function () {
    
    document.addEventListener("click", (e) => {
        let target = e.target;
        // Quando um botão de visualização de cartão é clicado
        if (target.classList.contains("btnModalViewCard")) {
            
            let modal = target.querySelector(".modalViewCard");
            if (!modalPrime.modalHTML) {
                modalPrime.modalHTML = modal.innerHTML;
            }
            if (modal) {
                modalPrime.card = target.closest('.card');
                modal.showModal();
                
            }
        }

        // Quando o botão de fechar é clicado
        if (target.classList.contains("btnCloseViewCard")) {
            let modal = target.closest(".modalViewCard");
            modal.close();
        }
    });



        //Script para abrir na taskBoard
        const tbViewCard = document.querySelectorAll('.modalViewCard');
const editCard = document.querySelectorAll('.editCardModal');
const taskRows = document.querySelectorAll('.btnModalViewCard');

taskRows.forEach((row) => {
    row.addEventListener("click", () => {
        // Verifica se algum modal de edição está aberto
        const isEditCardOpen = Array.from(editCard).some(modal => modal.open);
        
        if (!isEditCardOpen) {
            const modal = row.querySelector('.modalViewCard');
            if (modal) {
                modal.showModal(); // Abre o modal específico
            }
        }
    });
});

const tbBtnEditCard = document.querySelectorAll('.close-btn');
tbBtnEditCard.forEach((button) => {
    button.addEventListener("click", (event) => {
        event.stopPropagation(); // Evita que o clique no botão feche e reabra o modal
        tbViewCard.forEach((modal) => {
            modal.close(); // Fecha todos os modais
        });
    });
});



})();


document.addEventListener('DOMContentLoaded', function () {

  const forms = document.querySelectorAll('.formCheckbox');

    forms.forEach(form => {

      const checkboxes = form.querySelectorAll('.checkbox-subtask');

      checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {

          event.preventDefault();
          
          const formData = new FormData(form);

          fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
              'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
          })
          .then(response => response.json()) 
          .then(data => {
            console.log('Resposta recebida:', data);
          })
          .catch(error => {
            console.error('Erro ao enviar o formulário via AJAX:', error);
          });
        });
      });
    });
});

