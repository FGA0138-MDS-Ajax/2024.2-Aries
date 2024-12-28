const draggables = document.querySelectorAll(".card");
const droppables = document.querySelectorAll(".cards-scroll");
const apiBase = 'http://127.0.0.1:8000/members/api';

draggables.forEach((task) => {
  task.addEventListener("dragstart", () => {
    task.classList.add("is-dragging");
  });
  task.addEventListener("dragend", () => {
    task.classList.remove("is-dragging");
  });
});

droppables.forEach((zone) => {
  zone.addEventListener("dragover", (e) => {
    e.preventDefault();

    const bottomTask = insertAboveTask(zone, e.clientY);
    const curTask = document.querySelector(".is-dragging");


    if (!bottomTask) {
      zone.appendChild(curTask);
    } else {
      zone.insertBefore(curTask, bottomTask);
    }

    
  });

  zone.addEventListener("drop", async (e) => {
    const task = document.querySelector(".is-dragging");
    const newStatus = zone.getAttribute("data-status"); // Novo status da tarefa
    const taskId = task.getAttribute("data-id"); // ID da tarefa

    try {
      // Enviar atualização para o backend
      const response = await fetch(`/members/api/tasks/${taskId}/update-status/`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({ status: newStatus }),
      });

      if (!response.ok) {
        throw new Error("Erro ao atualizar o status no banco de dados.");
      }

      // Obter os dados atualizados do backend
      const updatedTask = await response.json();

      // Atualizar a label do status no HTML
      const labelDiv = task.querySelector(".label .div-wrapper");
      const textDiv = task.querySelector(".label .text-wrapper");

      if (updatedTask.status === "Concluída") {
        labelDiv.style.backgroundColor = "rgba(0, 117, 246, 0.20)";
        textDiv.style.color = "#0075F6";
        textDiv.textContent = "Concluída";
      } else if (updatedTask.status === "Pendente") {
        labelDiv.style.backgroundColor = "rgba(215, 0, 0, 0.20)";
        textDiv.style.color = "#D70000";
        textDiv.textContent = "A Começar";
      } else if (updatedTask.status === "Em Progresso") {
        labelDiv.style.backgroundColor = "rgba(255, 192, 57, 0.20)";
        textDiv.style.color = "#CF8E00";
        textDiv.textContent = "Em Progresso";
      }
    } catch (error) {
      console.error("Erro ao atualizar tarefa:", error);
    
    }
});

});

const insertAboveTask = (zone, mouseY) => {
  const els = zone.querySelectorAll(".card:not(.is-dragging)");

  let closestTask = null;
  let closestOffset = Number.NEGATIVE_INFINITY;

  els.forEach((task) => {
    const { top } = task.getBoundingClientRect();

    const offset = mouseY - top;

    if (offset < 0 && offset > closestOffset) {
      closestOffset = offset;
      closestTask = task;
    }
  });

  return closestTask;
};


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith(name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  
  const csrftoken = getCookie('csrftoken');