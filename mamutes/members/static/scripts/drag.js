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