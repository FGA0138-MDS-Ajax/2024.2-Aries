document.addEventListener('DOMContentLoaded', () => {
    const responsiblesField = document.getElementById('responsibles');
    const plusMembers = document.querySelectorAll('.plus-members');
    

    plusMembers.forEach(member => {
        member.addEventListener('click', () => {
            const memberId = member.getAttribute('data-id');

            
            // Obtém o valor atual do campo
            let currentValues = responsiblesField.value ? responsiblesField.value.split(',') : [];
            
            // Adiciona o novo ID, se ainda não estiver na lista
            if (!currentValues.includes(memberId)) {
                currentValues.push(memberId);
            }
            // Atualiza o campo com os novos valores
            responsiblesField.value = currentValues.join(',');

            const personTeam = member.closest('.person-team'); // Encontra o elemento pai .person-team
            personTeam.classList.toggle('selected-person-team');
        });
    });
});  
