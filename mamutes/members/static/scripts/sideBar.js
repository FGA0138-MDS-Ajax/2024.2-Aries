(
    function(){
        document.addEventListener("DOMContentLoaded", function () {
            const arrowButton = document.querySelector(".arrow-icon");
            const idAba = document.querySelectorAll(".idAba");
            const abas = document.querySelectorAll(".abas");
            const marker = document.querySelectorAll(".marker");
            const sidebarCentral = document.querySelector(".sidebar-central");
            const text = document.querySelectorAll(".texto");
            const aba = document.querySelectorAll(".aba");
        
            arrowButton.addEventListener("click", () => {
                arrowButton.classList.toggle("closed");
                sidebarCentral.classList.toggle("closed");
        
                marker.forEach((m) => {
                    m.classList.toggle("closed");
                });
        
                aba.forEach((a) => {
                    a.classList.toggle("closed");
                });
        
                text.forEach((t) => {
                    t.classList.toggle("closed");
                });
                idAba.forEach((i) => {
                    i.classList.toggle("closed");
                });
                abas.forEach((b) => {
                    b.classList.toggle("closed");
                });
            });
        });
    }


)();