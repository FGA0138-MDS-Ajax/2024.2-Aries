document.addEventListener('DOMContentLoaded', () => {
    // Seleciona todos os botões de "adicionar membros"
    const plusMembers = document.querySelectorAll('.plus-members');

    plusMembers.forEach(member => {
        member.addEventListener('click', () => {
            const memberId = member.getAttribute('data-id');
            if (!memberId) {
                return;
            }

            // Encontra o input #responsibles mais próximo do clique
            const responsiblesField = member.closest('.form')?.querySelector('#responsibles');

            if (!responsiblesField) {
                return;
            }

            // Obtém o valor atual do campo
            let currentValues = responsiblesField.value ? responsiblesField.value.split(',') : [];

            // Adiciona o novo ID se ainda não estiver na lista
            if (!currentValues.includes(memberId)) {
                currentValues.push(memberId);
            }

            // Atualiza o campo com os novos valores
            responsiblesField.value = currentValues.join(',');

            const personTeam = member.closest('.person-team'); // Encontra o elemento pai .person-team
            if (personTeam) {
                personTeam.classList.toggle('selected-person-team');
            }
        });
    });
});

document.addEventListener("click", (e) => {
    let eve = e.target;

    // Verifica se o clique foi no botão que abre o mini modal
    if (eve.classList.contains("plus-people")) {
        let modal = eve.closest(".modal-form"); // Encontra o modal mais próximo do botão
        let miniModal = modal.querySelector(".mini-modal");

        if (miniModal) {
            // Fecha todos os modais antes de abrir o modal correspondente
            document.querySelectorAll('.mini-modal').forEach(modal => {
                modal.style.display = "none";
            });

            // Alterna a exibição do mini modal do botão clicado
            miniModal.style.display = miniModal.style.display === "flex" ? "none" : "flex";
        }
    } 
    // Fecha o mini modal se clicar fora dele ou no botão "okButton"
    else {
        document.querySelectorAll(".mini-modal").forEach(miniModal => {
            if (!miniModal.contains(eve) || eve.classList.contains("okButton")) {
                miniModal.style.display = "none";
            }
        });
    }
});

document.querySelectorAll('.searchToAddMember').forEach(inputSearcher => {
    let lastValue = ""; 

    inputSearcher.addEventListener('input', () => {
        const currentValue = inputSearcher.value.toLowerCase();
        
        if (currentValue !== lastValue) {
            lastValue = currentValue; 

            const modalContent = inputSearcher.closest('.mini-modal-content');
            const peopleList = modalContent.querySelector('.center-people-list'); 

            if (peopleList) {
                const items = peopleList.querySelectorAll('.person-team'); // Todos os membros

                items.forEach(item => {
                    const fullname = item.querySelector('.name .div')?.textContent.toLowerCase();
                    const email = item.querySelector('.name .text-email')?.textContent.toLowerCase();

                    if ((fullname && fullname.includes(currentValue)) || (email && email.includes(currentValue))) {
                        item.classList.remove('hidden'); 
                    } else {
                        item.classList.add('hidden'); 
                    }
                });
            }
        }
    });

    inputSearcher.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            inputSearcher.focus(); 
        }
    });
});
