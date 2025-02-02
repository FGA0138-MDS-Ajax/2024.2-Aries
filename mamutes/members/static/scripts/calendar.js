document.addEventListener("DOMContentLoaded", function () {
    const dateElements = document.querySelectorAll(".dateWeek");
    const currentDate = new URLSearchParams(window.location.search).get('date') || new Date().toISOString().split('T')[0];
    const [year, month] = currentDate.split("-");
    const monthNames = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];
    document.querySelector(".textmonthYear").innerHTML = `${monthNames[parseInt(month) - 1]} ${year}`;
    
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
                    document.querySelector(".textmonthYear").innerHTML = `${monthNames[parseInt(month) - 1]} ${year}`;

                    const taskContainer = document.querySelector(".todayEvents");
                    taskContainer.innerHTML = "";

                    if (data.tasks.length > 0) {
                        data.tasks.forEach(task => {
                            const taskDiv = document.createElement("div");
                            taskDiv.className = "taskCalendar";
                            taskDiv.innerHTML = `<div class="colorTeamBlue" style="background-color: ${userAreaColor};"></div><p>${task.title}</p>`;
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
                            const borderColor = meeting.multiple_teams ? '#0075F6' : userAreaColor;
                            meetingDiv.innerHTML = `
                                <div class="borderImportantEvent" style="background: ${borderColor};"></div>
                                <div class="contentImportantEvent">
                                    <h4>${meeting.title}</h4>
                                    <div class="moreInfoEvent">
                                        <p class="hourEvent">${meeting.time}</p>
                                        <div class="peopleMeeting">
                                            ${meeting.areas.length === 1 && meeting.areas[0].name === "Estabilidade" ? `
                                                <div class="profilePic" style="background-color: ${meeting.areas[0].color};">
                                                    <p class="textPlusPeople">E</p>
                                                </div>
                                            ` : meeting.areas.length > 3 ? `
                                                ${meeting.areas.slice(0, 3).map(area => `
                                                    <div class="profilePic" style="background-color: ${area.color};">
                                                        <p class="textPlusPeople">${area.name.charAt(0)}</p>
                                                    </div>
                                                `).join('')}
                                                <div class="profilePic" style="background-color: #DDD;">
                                                    <p class="textPlusPeople">+${meeting.areas.length - 3}</p>
                                                </div>
                                            ` : meeting.areas.map(area => `
                                                <div class="profilePic" style="background-color: ${area.color};">
                                                    <p class="textPlusPeople">${area.name.charAt(0)}</p>
                                                </div>
                                            `).join('')}
                                        </div>
                                    </div>
                                </div>`;
                            taskContainer.appendChild(meetingDiv);
                        });
                    }

                });
        });
    });

    const previousMonthButton = document.querySelector(".arrows-date .arrow-icon:first-child");
    const nextMonthButton = document.querySelector(".arrows-date .arrow-icon:last-child");

    previousMonthButton.addEventListener("click", function () {
        const currentDate = this.dataset.date;
        window.location.href = `/previous-month/?date=${currentDate}`;
    });

    nextMonthButton.addEventListener("click", function () {
        const currentDate = this.dataset.date;
        window.location.href = `/next-month/?date=${currentDate}`;
    });

});
