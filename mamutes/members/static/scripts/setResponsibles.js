document.addEventListener('DOMContentLoaded', () => {
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

            // Atualresponsibles-containeriza o campo com os novos valores
            responsiblesField.value = currentValues.join(',');

            const personTeam = member.closest('.person-team'); // Encontra o elemento pai .person-team
            if (personTeam) {
                personTeam.classList.toggle('selected-person-team');
            }
        });
    });
});
