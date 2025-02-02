// (
//     function(){
//         document.addEventListener("DOMContentLoaded", function () {
//             const arrowButton = document.querySelector(".arrow-icon");
//             const idAba = document.querySelectorAll(".idAba");
//             const abas = document.querySelectorAll(".abas");
//             const marker = document.querySelectorAll(".marker");
//             const sidebarCentral = document.querySelector(".sidebar-central");
//             const text = document.querySelectorAll(".texto");
//             const aba = document.querySelectorAll(".aba");
        
//             arrowButton.addEventListener("click", () => {
//                 arrowButton.classList.toggle("closed");
//                 sidebarCentral.classList.toggle("closed");
        
//                 marker.forEach((m) => {
//                     m.classList.toggle("closed");
//                 });
        
//                 aba.forEach((a) => {
//                     a.classList.toggle("closed");
//                 });
        
//                 text.forEach((t) => {
//                     t.classList.toggle("closed");
//                 });
//                 idAba.forEach((i) => {
//                     i.classList.toggle("closed");
//                 });
//                 abas.forEach((b) => {
//                     b.classList.toggle("closed");
//                 });
//             });
//         });
//     }


// )();

// (function () {
//     document.addEventListener("DOMContentLoaded", function () {
//         const arrowButton = document.querySelector(".arrow-icon");
//         const idAba = document.querySelectorAll(".idAba");
//         const abas = document.querySelectorAll(".abas");
//         const marker = document.querySelectorAll(".marker");
//         const sidebarCentral = document.querySelector(".sidebar-central");
//         const text = document.querySelectorAll(".texto");
//         const aba = document.querySelectorAll(".aba");

//         // Função para atualizar a classe `closed` com base no estado salvo
//         function restoreState() {
//             const isClosed = localStorage.getItem("sidebarClosed") === "true";
//             if (isClosed) {
//                 arrowButton.classList.add("closed");
//                 sidebarCentral.classList.add("closed");
//                 marker.forEach((m) => m.classList.add("closed"));
//                 aba.forEach((a) => a.classList.add("closed"));
//                 text.forEach((t) => t.classList.add("closed"));
//                 idAba.forEach((i) => i.classList.add("closed"));
//                 abas.forEach((b) => b.classList.add("closed"));
//             }
//         }

//         // Restaura o estado ao carregar a página
//         restoreState();

//         // Adiciona ou remove a classe `closed` e salva o estado no LocalStorage
//         arrowButton.addEventListener("click", () => {
//             const isClosed = !arrowButton.classList.contains("closed");
//             arrowButton.classList.toggle("closed");
//             sidebarCentral.classList.toggle("closed");

//             marker.forEach((m) => m.classList.toggle("closed"));
//             aba.forEach((a) => a.classList.toggle("closed"));
//             text.forEach((t) => t.classList.toggle("closed"));
//             idAba.forEach((i) => i.classList.toggle("closed"));
//             abas.forEach((b) => b.classList.toggle("closed"));

//             // Salva o estado atualizado
//             localStorage.setItem("sidebarClosed", isClosed);
//         });
//     });
// })();




(function () {
    document.addEventListener("DOMContentLoaded", function () {
        const arrowButton = document.querySelector(".arrow-icon");
        const idAba = document.querySelectorAll(".idAba");
        const abas = document.querySelectorAll(".abas");
        const marker = document.querySelectorAll(".marker");
        const sidebarCentral = document.querySelector(".sidebar-central");
        const text = document.querySelectorAll(".texto");
        const aba = document.querySelectorAll(".aba");

        // Desativa a transição temporariamente
        function disableTransition(elements) {
            elements.forEach((el) => {
                el.style.transition = "none";
            });
        }

        // Restaura a transição
        function restoreTransition(elements) {
            elements.forEach((el) => {
                el.style.transition = ""; // Retorna ao CSS original
            });
        }

        // Restaura o estado salvo sem animação
        function restoreState() {
            const isClosed = localStorage.getItem("sidebarClosed") === "true";
            if (isClosed) {
                // Desativar transições temporariamente
                disableTransition([arrowButton, sidebarCentral, ...marker, ...aba, ...text, ...idAba, ...abas]);

                // Adiciona a classe closed
                arrowButton.classList.add("closed");
                sidebarCentral.classList.add("closed");
                marker.forEach((m) => m.classList.add("closed"));
                aba.forEach((a) => a.classList.add("closed"));
                text.forEach((t) => t.classList.add("closed"));
                idAba.forEach((i) => i.classList.add("closed"));
                abas.forEach((b) => b.classList.add("closed"));

                // Reativa as transições
                requestAnimationFrame(() => {
                    restoreTransition([arrowButton, sidebarCentral, ...marker, ...aba, ...text, ...idAba, ...abas]);
                });
            }
        }

        // Restaura o estado ao carregar a página
        restoreState();

        // Adiciona ou remove a classe `closed` e salva o estado no LocalStorage
        arrowButton.addEventListener("click", () => {
            const isClosed = !arrowButton.classList.contains("closed");
            arrowButton.classList.toggle("closed");
            sidebarCentral.classList.toggle("closed");

            marker.forEach((m) => m.classList.toggle("closed"));
            aba.forEach((a) => a.classList.toggle("closed"));
            text.forEach((t) => t.classList.toggle("closed"));
            idAba.forEach((i) => i.classList.toggle("closed"));
            abas.forEach((b) => b.classList.toggle("closed"));

            // Salva o estado atualizado
            localStorage.setItem("sidebarClosed", isClosed);
        });
    });
})();

