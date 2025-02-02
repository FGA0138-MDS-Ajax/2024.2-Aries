document.addEventListener("click", (e) => {
    const clickedElement = e.target;
    const modalViewMembers = document.querySelector('.container-modal-members')
    if(clickedElement.classList.contains('btnModalViewMembers')){
        modalViewMembers.showModal()
    } else if (clickedElement.classList.contains('btnCloseViewMembers')){
        modalViewMembers.close()
    }
});


const searchers = document.querySelectorAll('.searchMember'); // Seleciona todos os inputs de busca

searchers.forEach(inputSearcher => {
    let lastValue = ""; // Armazena o último valor digitado

    inputSearcher.addEventListener('input', () => {
        const currentValue = inputSearcher.value.toLowerCase();
        
        if (currentValue !== lastValue) {
            lastValue = currentValue; // Atualiza o último valor
            const peopleList = document.querySelector('.peopleList');
            const items = peopleList.querySelectorAll('.person-item');
        
            items.forEach(item => {
                const username = item.querySelector('.person-data-names p:nth-child(1)').textContent.toLowerCase();
                const fullname = item.querySelector('.person-data-names p:nth-child(2)').textContent.toLowerCase();
    
                if (username.includes(currentValue) || fullname.includes(currentValue)) {
                    item.classList.remove('hidden');
                } else {
                    item.classList.add('hidden');
                }
            });
        }
    });
});
