document.getElementById("start_date").value = new Date().toISOString().split('T')[0];

// Obtener los elementos de fecha de inicio y fecha de vencimiento
let startDateInput = document.getElementById("start_date");
let dueDateInput = document.getElementById("due_date");

// Obtener la fecha de inicio
let startDate = new Date(startDateInput.value);

// Establecer la fecha mínima en el campo de fecha de vencimiento
dueDateInput.min = startDate.toISOString().slice(0, 10);

let timeInput = document.getElementById("time");

timeInput.addEventListener("input", function() {
    this.value = this.value.replace(/[^0-9]/g, "");
});

function validateForm() {
    var project = document.getElementById("project").value;
    var type = document.getElementById("type").value;
    var subject = document.getElementById("subject").value;
    var priority = document.getElementById("priority").value;

    if (project === "" || type === "" || subject === "" || priority === "") {
        alert("Todos los campos requeridos deben estar llenos.");
        return false; 
    }

    return true;
}