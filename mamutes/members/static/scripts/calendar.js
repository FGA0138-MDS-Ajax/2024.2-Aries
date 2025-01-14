document.addEventListener("DOMContentLoaded", function () {
    const dateElements = document.querySelectorAll(".dateWeek");

    dateElements.forEach(element => {
        element.addEventListener("click", function () {
            const selectedDate = this.dataset.date;

            dateElements.forEach(el => {
                el.querySelector('.day').classList.remove("daySemiSelected");
                el.querySelector('.textDate').classList.remove("textDateSemiSelected");
            });

            this.querySelector('.day').classList.add("daySemiSelected");
            this.querySelector('.textDate').classList.add("textDateSemiSelected");

            fetch(`/get-events-tasks/?date=${selectedDate}`)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        alert(data.error);
                        return;
                    }

                    const dateTitle = document.querySelector("#todayDate");
                    const [year, month, day] = selectedDate.split("-");
                    const monthNames = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];
                    dateTitle.innerHTML = `${day} de ${monthNames[parseInt(month) - 1]}`;

                    const taskContainer = document.querySelector(".todayEvents");
                    taskContainer.innerHTML = "";

                    if (data.tasks.length > 0) {
                        data.tasks.forEach(task => {
                            const taskDiv = document.createElement("div");
                            taskDiv.className = "taskCalendar";
                            taskDiv.innerHTML = `<div class="colorTeamBlue"></div><p>${task.title}</p>`;
                            taskContainer.appendChild(taskDiv);
                        });
                    } else {
                        taskContainer.innerHTML = "<div class='taskCalendar'><p>Nenhuma tarefa atribuída a você para este dia.</p></div>";
                    }

                    if (data.events.length > 0) {
                        data.events.forEach(event => {
                            const eventDiv = document.createElement("div");
                            eventDiv.className = "importantEvent";
                            eventDiv.innerHTML = `
                                <div class="borderImportantEvent"></div>
                                <div class="contentImportantEvent">
                                    <h4>${event.title}</h4>
                                    <p class="hourEvent">${event.time}</p>
                                </div>`;
                            taskContainer.appendChild(eventDiv);
                        });
                    }

                    if (data.meetings.length > 0) {
                        data.meetings.forEach(meeting => {
                            const meetingDiv = document.createElement("div");
                            meetingDiv.className = "importantEvent";
                            meetingDiv.innerHTML = `
                                <div class="borderImportantEvent" style="background: #0075F6;"></div>
                                <div class="contentImportantEvent">
                                    <h4>${meeting.title}</h4>
                                    <div class="moreInfoEvent">
                                        <p class="hourEvent">${meeting.time}</p>
                                        <div class="peopleMeeting">
                                            <div class="profilePic">
                                                <img class="profileImg" src="/static/img/tag-img.png" alt="Erro ao carregar imagem">
                                            </div>
                                            <div class="profilePic">
                                                <img class="profileImg" src="/static/img/tag-img (1).png" alt="Erro ao carregar imagem">
                                            </div>
                                            <div class="profilePic">
                                                <img class="profileImg" src="/static/img/tag-img (2).png" alt="Erro ao carregar imagem">
                                            </div>
                                            <div class="profilePic" style="background-color: #DDD;">
                                                <p class="textPlusPeople">+2</p>
                                            </div> 
                                        </div>                                      
                                    </div>`;
                            taskContainer.appendChild(meetingDiv);
                        });
                    }
                });
        });
    });
});
