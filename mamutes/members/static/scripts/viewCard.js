// ! POR FAVOR NÃO MEXER NO JS de editCard e nem ViewCard se não souber oque está fazendo
// Objetivo do código:
// abre e fecha o modal viewCard e envia as atualizações da checkbox (se foi selecionada ou não) via AJAX (submissão de dados sem reload na atual página)

(function () {
    
    document.addEventListener("click", (e) => {
        let target = e.target;
        // Quando um botão de visualização de cartão é clicado
        if (target.classList.contains("btnModalViewCard")||target.classList.contains("btnTask")) {
            
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

