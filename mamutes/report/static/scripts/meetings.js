document.addEventListener("DOMContentLoaded", function () {
    const openModalAddBtn = document.getElementById("openModalAddBtn"); // js do modal add-reunião
    const closeModalAddBtn = document.getElementById("closeModalAddBtn");
    const modalAdd = document.getElementById("modalAdd");

    openModalAddBtn.addEventListener("click", function (event) {
        event.preventDefault();
        // console.log("abrindo o modal");
        modalAdd.style.display = "flex";
    });

    closeModalAddBtn.addEventListener("click", function () {
        // console.log("fechando o modal");
        modalAdd.style.display = "none";
    });

    window.addEventListener("click", function (event) {
        if (event.target === modalAdd) {
            modalAdd.style.display = "none";
        }
    });

    const meetingCards = document.querySelectorAll('.cardMeet');
    const modalcard = document.getElementById('modalcard');
    const closeModalEditBtn = document.getElementById('closeModalEditBtn');

    meetingCards.forEach(card => {
    card.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Verifica e loga os dados do dataset
        console.log('Card Dataset:', card.dataset);

        const id = card.dataset.id;
        const title = card.dataset.title;
        const description = card.dataset.description;
        const meetingDate = card.dataset.meetingDate;
        const meetingTimeBegin = card.dataset.meetingTimeBegin;
        const meetingTimeEnd = card.dataset.meetingTimeEnd;
        const local = card.dataset.local;
        const isRemote = card.dataset.isRemote;
        const link = card.dataset.link;
        const linkPauta = card.dataset.linkPauta;
        const other = card.dataset.otherParticipants;

        // Atualiza os elementos do modal
        document.getElementById('modalId').innerText = id || 'Sem id';
        document.getElementById('modalTitle').innerText = title || 'Sem Título';
        document.getElementById('modalDescription').innerText = description|| 'Sem Descrição';
        document.getElementById('modalDate').innerText = meetingDate || '';
        document.getElementById('modalTimeBegin').innerText = meetingTimeBegin || '';
        document.getElementById('modalTimeEnd').innerText = meetingTimeEnd || '';
        document.getElementById('modalLocal').innerText = local || '';
        
        document.getElementById('modallink_pauta').innerText = linkPauta || '';
        document.getElementById('modallink').innerText = link || '';
        document.getElementById('modalother_participants').innerText = other || ''; 

        const areasHTML = card.querySelector('.teamsMeeting').innerHTML;
        document.getElementById('uniqueModalAreas').innerHTML = areasHTML;

        const personHTML = card.querySelector('.personMeeting').innerHTML;
        document.getElementById('uniqueModalPerson').innerHTML = personHTML;
        // Exibe o modal
        modalcard.style.display = 'flex';
    });
    });

    // Fechar modal
    closeModalEditBtn.addEventListener('click', function() {
    modalcard.style.display = 'none';
    });
    window.addEventListener('click', function(event) {
    if (event.target === modalcard) {
        modalcard.style.display = 'none';
    }
    });

    const openModalFilterBtn = document.getElementById("openModalFilterBtn"); // js do modal filtro
    const closeModalFilterBtn = document.getElementById("closeModalFilterBtn");
    const modalFilter = document.getElementById("modalFilter");

    openModalFilterBtn.addEventListener("click", function (event) {
        event.preventDefault();
        // console.log("abrindo o modal");
        modalFilter.style.display = "flex";
    });

    closeModalFilterBtn.addEventListener("click", function () {
        // console.log("fechando o modal");
        modalFilter.style.display = "none";
    });

    window.addEventListener("click", function (event) {
        if (event.target === modalFilter) {
            modalFilter.style.display = "none";
        }
    });
});


