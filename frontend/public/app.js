document.addEventListener("DOMContentLoaded", () => {
    const contentDiv = document.getElementById("content");

    // Hacer una solicitud al backend
    fetch("http://nanoserver.local:8000/")
        .then((response) => response.json())
        .then((data) => {
            contentDiv.innerHTML = `<p>${data.message}</p>`;
        })
        .catch((error) => {
            contentDiv.innerHTML = `<p>Error cargando el contenido: ${error.message}</p>`;
        });
});
