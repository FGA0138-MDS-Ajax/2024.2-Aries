function converterData(dataString) {
    const meses = {
        "janeiro": "01", "fevereiro": "02", "março": "03", "abril": "04",
        "maio": "05", "junho": "06", "julho": "07", "agosto": "08",
        "setembro": "09", "outubro": "10", "novembro": "11", "dezembro": "12"
    };

    const partes = dataString.toLowerCase().split(" de ");

    if (partes.length !== 3 || !meses[partes[1]]) return "Formato inválido"; 

    const dia = partes[0].padStart(2, '0'); 
    const mes = meses[partes[1]]; 
    const ano = partes[2]; 

    return `${ano}-${mes}-${dia}`;
}

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

    const openModalEditBtn = document.getElementById("openModalEditBtn"); // js do modal edit-reunião
    const closeModalEditBtn = document.getElementById("closeModalEditBtn");
    const modalEdit = document.getElementById("modalEdit");

    openModalEditBtn.addEventListener("click", function (event) {
        event.preventDefault();
        modalEdit.style.display = "flex";
    });
    
    closeModalEditBtn.addEventListener("click", function () {
        modalEdit.style.display = "none";
    });
    
    window,this.addEventListener("click", function (event) {
        if (event.target === modalEdit) {
            modalEdit.style.display = "none";
        }
    });
    
    const meetingCards = document.querySelectorAll('.cardMeet');
    const modalcard = document.getElementById('modalcard');
    const closeModalSeeBtn = document.getElementById('closeModalSeeBtn');
    
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
            const pauta = card.dataset.pauta;
            const other = card.dataset.otherParticipants;
            
            // Atualiza os elementos do modal
            document.getElementById('modalId').innerText = id || 'Sem id';
            document.getElementById('modalTitle').innerText = title || 'Sem Título';
            document.getElementById('modalDescription').innerText = description|| 'Sem Descrição';
            document.getElementById('modalDate').innerText = meetingDate || '';
            document.getElementById('modalTimeBegin').innerText = meetingTimeBegin || '';
            document.getElementById('modalTimeEnd').innerText = meetingTimeEnd || '';
            document.getElementById('modalLocal').innerText = local || '';

            document.getElementById('modallink_pauta').innerText = pauta || '';
            document.getElementById('modallink').innerText = link || '';
            document.getElementById('modalother_participants').innerText = other || ''; 
            
            // input do edit-modal
            // document.getElementById('id_meeting_id').value = id || 'Sem id';
            document.getElementById('id_title').value = title || 'Sem Título';
            document.getElementById('id_description').value = description || 'Sem Descrição';
            document.getElementById('id_meeting_date').value = converterData(meetingDate) || '';
            // console.log('meetingDate:', converterData(meetingDate));
            document.getElementById('id_meeting_time_begin').value = meetingTimeBegin || '';
            document.getElementById('id_meeting_time_end ').value = meetingTimeEnd || '';
            document.getElementById('id_local').value = local || '';
            document.getElementById('id_is_remote').value = isRemote || '';
            document.getElementById('id_link').value = link || '';
            document.getElementById('id_link_pauta').value = pauta || '';
            document.getElementById('id_other_participants').value = other || '';
            
            
            const areasHTML = card.querySelector('.teamsMeeting').innerHTML;
            document.getElementById('uniqueModalAreas').innerHTML = areasHTML;
            
            const personHTML = card.querySelector('.personMeeting').innerHTML;
            document.getElementById('uniqueModalPerson').innerHTML = personHTML;
            // Exibe o modal
            modalcard.style.display = 'flex';
        });
    });

    // Fechar modal
    closeModalSeeBtn.addEventListener('click', function() {
    modalcard.style.display = 'none';
    });
    window.addEventListener('click', function(event) {
    if (event.target === modalcard) {
        modalcard.style.display = 'none';
    }
    });

    const openModalFilterBtn = document.getElementById("openModalFilterBtn");
    const closeModalFilterBtn = document.getElementById("closeModalFilterBtn");
    const modalFilter = document.getElementById("modalFilter");

    const applyFiltersBtn = document.getElementById("applyFilters");
    const resetFiltersBtn = document.getElementById("resetFilters");
    const checkboxes = document.querySelectorAll(".team-checkbox");

    openModalFilterBtn.addEventListener("click", function (event) {
        event.preventDefault();
        modalFilter.style.display = "flex";
    });

    closeModalFilterBtn.addEventListener("click", function () {
        modalFilter.style.display = "none";
    });

    window.addEventListener("click", function (event) {
        if (event.target === modalFilter) {
            modalFilter.style.display = "none";
        }
    });

    applyFiltersBtn.addEventListener("click", function (event) {
        event.preventDefault(); 

        let selectedAreas = [];
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                selectedAreas.push(checkbox.value);
            }
        });

        if (selectedAreas.length === 0) {
            meetingCards.forEach(card => card.style.display = "block");
            modalFilter.style.display = "none"; 
            return;
        }

        meetingCards.forEach(card => {
            let cardAreas = card.getAttribute("data-areas").slice(0, -1).split(",");

            if (cardAreas.some(area => selectedAreas.includes(area))) {
                card.style.display = "block"; 
            } else {
                card.style.display = "none"; 
            }
        });

        modalFilter.style.display = "none"; 
    });

    resetFiltersBtn.addEventListener("click", function (event) {
        event.preventDefault(); 
        checkboxes.forEach(checkbox => checkbox.checked = false); 
        meetingCards.forEach(card => card.style.display = "block"); 
        modalFilter.style.display = "none"; 
    });
});
