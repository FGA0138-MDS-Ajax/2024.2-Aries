const apiBase = 'http://127.0.0.1:8000/members/api'; // URL base da API

// Função para buscar colunas e tarefas
async function fetchKanbanData() {
  try {
    const columnsResponse = await fetch(`${apiBase}/columns/`);
    const columns = await columnsResponse.json();

    const kanban = document.getElementById('kanban');
    kanban.innerHTML = ''; // Limpar o conteúdo antes de renderizar

    for (const column of columns) {
      // Criar coluna
      const columnDiv = document.createElement('div');
      columnDiv.classList.add('column');
      columnDiv.innerHTML = `<h2>${column.name}</h2>`;

      // Buscar tarefas da coluna
      const tasksResponse = await fetch(`${apiBase}/tasks/?column=${column.id}`);
      const tasks = await tasksResponse.json();

      // Adicionar tarefas à coluna
      for (const task of tasks) {
        const taskDiv = document.createElement('div');
        taskDiv.classList.add('task');
        taskDiv.innerHTML = `<strong>${task.title}</strong><p>${task.description}</p>`;
        columnDiv.appendChild(taskDiv);
      }

      kanban.appendChild(columnDiv);
    }
  } catch (error) {
    console.error('Erro ao buscar dados:', error);
  }
}

// Executar a função ao carregar a página
fetchKanbanData();
