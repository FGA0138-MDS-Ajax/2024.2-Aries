document.addEventListener("DOMContentLoaded", () => {
    document.body.addEventListener("click", (e) => {
        const event = e.target;

        // lógica com os modais
        if (event.classList.contains("toOpen")) {
            const editAndRemove = event.querySelector(".twoButton");
            const editAndRemoveAll = document.querySelectorAll(".twoButton");
            
            //fecha todos os modais que podem estar abertos
            if (editAndRemove) {
                editAndRemoveAll.forEach(other => {
                    if (other !== editAndRemove) {
                        other.style.display = "none";
                    }
                });
                //abre somente o modal clicado
                if (editAndRemove.style.display === "none" || editAndRemove.style.display === "") {
                    editAndRemove.style.display = "flex";
                } else {
                    editAndRemove.style.display = "none";
                }
            }
        }
        
        //lógica para deixar os input desativados depois de salvar (somente a linha editada).
        if (event.id === "saveButton"){

            //faz o botão de salvar sumir
            if(event.style.display !== 'none'){
                event.style.display = 'none';
            }

            //acha um elemento pai suficiente para caçar os inputs da linha.
            let elemento = event;
            let pai = elemento; 

            for (let i = 1; i <= 2; i++) {
                pai = pai.parentElement;
            }
            //desabilita a edição dos inputs
            const inputs = pai.querySelectorAll('input');
            inputs.forEach((input) => {
                if (!input.disabled) { 
                    input.disabled = true; 
                }
            });
            //habilita o modal para poder editar novamente
            const modal = pai.querySelector(".toOpen");
            if (modal.style.display !== "flex") {
                modal.style.display = "flex";
            } 


            //lógica para fechar os modais que podem estar abertos
            const editAndRemove = pai.querySelector(".twoButton");
            const editAndRemoveAll = pai.querySelectorAll(".twoButton");
            
            if (editAndRemove) {
                editAndRemoveAll.forEach(other => {
                    if (other !== editAndRemove) {
                        other.style.display = "none";
                    }
                });
                //abre somente o modal clicado
                if (editAndRemove.style.display === "none" || editAndRemove.style.display === "") {
                    editAndRemove.style.display = "flex";
                } else {
                    editAndRemove.style.display = "none";
                }
            }
        }
        //lógica para habilitar os inputs para edição, (somente a linha da edição).
        if (event.id === "edit") {
            let elemento = event;
            let pai = elemento; 

            //acha um elemento pai suficiente para caçar os inputs da linha.
            for (let i = 1; i <= 4; i++) {
                pai = pai.parentElement;
            }

            //habilita os inputs para edição
            const inputs = pai.querySelectorAll('input'); 
            inputs.forEach((input) => {
                if (input.disabled) { 
                    input.disabled = false; 
                }
            });

            //faz o modal desaparecer
            const modal = pai.querySelector(".toOpen");

            if (modal.style.display !== "none") {
                modal.style.display = "none";
            } 
            //faz o botão para salvar aparecer
            const saveButton = pai.querySelector("#saveButton");
            if(saveButton.style.display !== "flex"){
                saveButton.style.display = "flex";
            } 
        }        

        if (event.id === "exclude") {
            //logica para excluir linha, caso a gente escolha fzr com js e não django.
        }
        
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const table = document.getElementById("data-table");
    const headers = table.querySelectorAll("thead th");
    const rows = Array.from(table.querySelectorAll("tbody tr"));

    headers.forEach((header, index) => {
        header.addEventListener("click", () => {
            const type = header.dataset.type;
            const isAscending = header.classList.contains("asc");

            // Remover classes de ordenação de outros cabeçalhos
            headers.forEach(h => h.classList.remove("asc", "desc"));

            // Ordenar as linhas
            const sortedRows = rows.sort((a, b) => {
                const aCell = a.cells[index].textContent.trim();
                const bCell = b.cells[index].textContent.trim();

                if (type === "number") {
                    return isAscending
                        ? bCell - aCell
                        : aCell - bCell;
                } else {
                    return isAscending
                        ? bCell.localeCompare(aCell)
                        : aCell.localeCompare(bCell);
                }
            });

            // Adicionar classe para indicar ordenação
            header.classList.toggle("asc", !isAscending);
            header.classList.toggle("desc", isAscending);

            // Atualizar a tabela com as linhas ordenadas
            const tbody = table.querySelector("tbody");
            tbody.innerHTML = "";
            sortedRows.forEach(row => tbody.appendChild(row));
        });
    });
});




document.addEventListener("DOMContentLoaded", () => {
// Seleciona o input de busca
    const searchInput = document.getElementById('search');

    // Quando o usuário interagir com o input, esta função será executada
    searchInput.addEventListener('input', (event) => {
        const value = formatString(event.target.value); // Armazena e formata o valor do input

        const items = document.querySelectorAll('.tableItens .teste'); // Seleciona todos os itens
        const noResults = document.getElementById('no_results'); // Seleciona o elemento da mensagem "nenhum resultado"
        let hasResults = false; // Indica se há resultados correspondentes

        // Se existir valor no input
        if (value !== '') {
            items.forEach(item => {
                const itemTitle = item.querySelector('.firtsItens').value; // Obtém o texto do título do item
                // const itemDescription = item.querySelector('.item-description').textContent; // Obtém o texto da descrição do item

                // Se o valor digitado está contido nesse texto
                if (formatString(itemTitle).indexOf(value) !== -1
                ) {
                    // Exibe o item
                    item.style.display = 'flex';

                    // Indica que existem resultados
                    hasResults = true;
                } else {
                    // Oculta o item
                    item.style.display = 'none';
                }
            });

            // Exibe ou oculta a mensagem "nenhum resultado"
            if (hasResults) {
                noResults.style.display = 'none';
            } else {
                noResults.style.display = 'block';
            }

        } else {
            // Sempre exibe todos os itens quando o input está vazio
            items.forEach(item => item.style.display = 'flex');
            noResults.style.display = 'none'; // Oculta a mensagem "nenhum resultado"
        }
    });

// Função para formatar strings: remove espaços em branco, transforma em lowercase e remove acentos
function formatString(value) {
    return value
        .trim() // Remove espaços em branco
        .toLowerCase() // Transforma em lowercase
        .normalize('NFD') // Normaliza para separar os acentos
        .replace(/[\u0300-\u036f]/g, ''); // Remove os acentos
}

});
















