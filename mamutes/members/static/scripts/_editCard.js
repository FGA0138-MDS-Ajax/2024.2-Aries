

    // ! POR FAVOR NÃO MEXER NO JS de editCard e nem ViewCard se não souber oque está fazendo
    
    //Objetivo do código:
    //Além de abrir o modal correto, ele salva em um objeto global o card para poder saber qual editCard correto a se manipular,
    //Após isso ele recarrega os dados da data formatada e nas submissões ele exclui os input de checkbox zerados para não estragar o banco
    //também salva as checkbox selecionadas e não selecionadas de subtarefas em input oculto(display none), SETando com true ou false e enviando pro django
    //Além disso esse js faz com que quando  o usuario clicar a tecla 'enter' quando estiver em um input de subtarefa ele gere um proximo input, ou quando apagar a subtarefa, volte pro input anterior
    
    let modalPrime = {
        card: null
    };
    
    (function () {
        function formatDate(date) {
            date = date.replace(/\s+/g, ''); // Remove espaços extras
            let [d, m, y] = date.split("/");
    
            // Garantir que dia e mês tenham 2 dígitos
            d = d.padStart(2, '0'); // Adiciona 0 à esquerda se o dia tiver 1 dígito
            m = m.padStart(2, '0'); // Adiciona 0 à esquerda se o mês tiver 1 dígito
            
            // Garantir que o ano tenha 4 dígitos
            y = y.padStart(4, '0'); // Adiciona 0 à esquerda se o ano tiver menos de 4 dígitos
    
            return `${y}-${m}-${d}`;
        }
    
    
        function removeEmptySubtasks(editCard) {
            const subtaskItems = editCard.querySelectorAll('.subtask-item');
    
            subtaskItems.forEach(item => {
                const checkbox = item.querySelector('.checkbox-subtask');
                const inputTask = item.querySelector('.label-subtask');
    
                // Remove a subtarefa se estiver vazia e não estiver marcada
                if (!inputTask || inputTask.value.trim() === '') {
                    item.remove();
                }
            });
        }
    
        document.addEventListener("click", (e) => {
            let target = e.target;
    
    
            // Quando o ícone de edição é clicado
            if (target.classList.contains("edit-icon")) {
                let modalViewCard = target.closest(".modalViewCard");
                if (modalViewCard) {
                    modalViewCard.close(); // Fecha o modal de visualização
                }
    
                const card = modalPrime.card = target.closest(".btnModalViewCard"); // Define o card atual
                if (!card) return;
    
                const editCard = card.querySelector(".editCardModal");
                if (!editCard) return;
    
                editCard.showModal();
    
                let prazoData = card.querySelector('.prazo-data');
                if (prazoData) {
                    let prazoText = prazoData.textContent.trim(); // Remove espaços extras
                    prazoText = formatDate(prazoText); // Formata a data
                    
                    let prazoInput = editCard.querySelector('.data-input');
                    if (prazoInput) {
                        prazoInput.value = prazoText; // Define o valor do input
                    }
                }
    
                // Remove subtarefas vazias ao enviar o formulário
                const form = editCard.querySelector(".form");
                if (form) {
                    form.addEventListener('submit', function (event) {
                        removeEmptySubtasks(editCard);
    
                        const inputSubtask = editCard.querySelector(".inputSubTask");
                        if (inputSubtask) {
                            inputSubtask.value = "";
    
                            // Seleciona todos os checkboxes dentro do formulário
                            const checkBoxList = form.querySelectorAll(".checkbox-subtask");
                            checkBoxList.forEach((element) => {
                                inputSubtask.value += element.checked ? "true," : "false,";
                            });
    
                            // Remove a última vírgula, se necessário
                            inputSubtask.value = inputSubtask.value.replace(/,$/, "");
                        }
                    });
                }
    
                // Gerenciamento de subtarefas
                let subtaskContainer = editCard.querySelector("#subtask-container");
                if (subtaskContainer) {
                    // Substitui o container para remover event listeners duplicados
                    subtaskContainer.replaceWith(subtaskContainer.cloneNode(true));
                    subtaskContainer = editCard.querySelector("#subtask-container");
    
                    subtaskContainer.addEventListener("keydown", function (e) {
                        const currentInput = e.target;
    
                        // Verifica se o alvo do evento é um campo de subtarefa
                        if (!currentInput.classList.contains("label-subtask")) return;
    
                        // Adiciona nova subtarefa ao pressionar Enter
                        if (e.key === "Enter") {
                            e.preventDefault();
    
                            if (currentInput.value.trim() === "") return;
    
                            // Cria um novo subtask-item
                            const newSubtask = document.createElement("label");
                            newSubtask.className = "subtask-item";
                            newSubtask.innerHTML = `
                                <input type="checkbox" class="checkbox-subtask" name="checkbox-subtask" value="on">
                                <span class="checkmark"></span>
                                <input class="label-subtask" type="text" placeholder="Adicionar subtarefa..." value="" name="inputTask">
                            `;
    
                            subtaskContainer.appendChild(newSubtask);
    
                            // Foca no novo input
                            newSubtask.querySelector(".label-subtask").focus();
                        }
    
                        // Remove subtarefa ao pressionar Backspace, garantindo que sempre sobre pelo menos um input
                        if (e.key === "Backspace" && currentInput.value.trim().length === 0) {
                            e.preventDefault();
    
                            const subtaskItem = currentInput.closest(".subtask-item");
                            const allSubtasks = subtaskContainer.querySelectorAll(".subtask-item");
    
                            if (allSubtasks.length > 1) {
                                const previousSubtask = subtaskItem.previousElementSibling;
                                subtaskItem.remove();
    
                                if (previousSubtask) {
                                    const previousInput = previousSubtask.querySelector(".label-subtask");
                                    if (previousInput) previousInput.focus();
                                }
                            }
                        }
                    });
                }
            }
        });

        const editCard = document.querySelectorAll('.editCardModal');
        const btnEditCard = document.querySelectorAll('.close-btn');
        
        btnEditCard.forEach((button) => {
            button.addEventListener("click", () => {
                editCard.forEach((modal) => {
                    modal.close(); // Fecha todos os modais
                });
            });
        });
    })();
    


