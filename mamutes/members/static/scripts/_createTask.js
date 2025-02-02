document.addEventListener("DOMContentLoaded", function () {
    
    const openModalBtns = document.querySelectorAll("#buttonNewTask");
    const closeModalBtns = document.querySelectorAll("#close-modal");
    const modal = document.getElementById("modal");

    if (!modal) return;

    // Função para abrir o modal
    openModalBtns.forEach((btn) => {
        btn.addEventListener("click", function () {
            modal.style.display = "flex"; // Exibe o modal
        });
    });

    // Função para fechar o modal
    closeModalBtns.forEach((btn) => {
        btn.addEventListener("click", function () {
            modal.style.display = "none"; // Esconde o modal
        });
    });

    // Fechar o modal se clicar fora do conteúdo
    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.style.display = "none"; // Esconde o modal se clicar fora dele
        }
    });

    

    const subtaskContainer = modal.querySelector("#subtask-container");
    const form = modal.querySelector(".form");
    const inputSubtask = modal.querySelector(".inputSubTask");

    // Evento para adicionar/remover subtarefas
    subtaskContainer.addEventListener("keydown", function (e) {
        const currentInput = e.target;

        // Adicionar nova subtarefa ao pressionar Enter
        if (e.key === "Enter" && currentInput.classList.contains("label-subtask")) {
            e.preventDefault();

            if (currentInput.value.trim() === "") return;

            const newSubtask = document.createElement("label");
            newSubtask.className = "subtask-item";
            newSubtask.innerHTML = `
                <input type="checkbox" class="checkbox-subtask" name="checkbox-subtask" value="on">
                <span class="checkmark"></span>
                <input class="label-subtask" type="text" placeholder="Adicionar subtarefa..." value="" name="inputTask">
            `;
            subtaskContainer.appendChild(newSubtask);
            newSubtask.querySelector(".label-subtask").focus();
        }

        // Remover subtarefa ao pressionar Backspace
        if (e.key === "Backspace" && currentInput.classList.contains("label-subtask") && currentInput.value.length === 0) {
            e.preventDefault();
            const subtaskItem = currentInput.closest(".subtask-item");
            const allSubtasks = subtaskContainer.querySelectorAll(".subtask-item");
            if (allSubtasks.length > 1) {
                const previousSubtask = subtaskItem.previousElementSibling;
                subtaskItem.remove();
                if (previousSubtask) {
                    previousSubtask.querySelector(".label-subtask").focus();
                }
            }
        }
    });

    // Evento de submissão do formulário
    form.addEventListener("submit", (event) => {
        inputSubtask.value = "";
        const labelSubtaskList = form.querySelectorAll(".label-subtask");

        labelSubtaskList.forEach((element) => {
            if (element.value.trim() === "") {
                element.closest(".subtask-item").remove();
            }
        });

        const checkBoxList = form.querySelectorAll(".checkbox-subtask");
        checkBoxList.forEach((element) => {
            inputSubtask.value += element.checked ? "true," : "false,";
        });
        inputSubtask.value = inputSubtask.value.replace(/,$/, "");
    });
});




