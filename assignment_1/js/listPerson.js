
function selection() {
  var selected = document.getElementById('selectedFilter').value;
  var filterPerson = document.getElementById('filterOfPerson');
  var filterInterval = document.getElementById('filterOfIntervals');

   if (selected === "2") {
    filterPerson.style.display = "block";
    filterInterval.style.display = "none";
  } else if (selected === "3") {
    filterPerson.style.display = "none";
    filterInterval.style.display = "block";
    setMaxValue();
  } else if (selected === "0") {
    filterPerson.style.display = "none";
    filterInterval.style.display = "none";
  }
}

function updateRangeValue(elementId, value) {
  document.getElementById(elementId).textContent = value;
}

function setMaxValue() {
  var tableRows = document.getElementById('reportTable').getElementsByTagName('tr');
  var maxProjects = 0;

  for (var i = 1; i < tableRows.length; i++) {
    var projectsCell = tableRows[i].getElementsByTagName('td')[3];
    var projects = parseInt(projectsCell.textContent);

    if (projects > maxProjects) {
      maxProjects = projects;
    }
  }

  document.getElementById('numberProjects').max = maxProjects;

  // Llamar a updateRangeValue con el ID y el valor máximo del span correspondiente
  updateRangeValue('maxProjectsValue', maxProjects);
}

var table = document.getElementById('reportTable');
document.getElementById('listForm').addEventListener('submit', function (e) {
  var table = document.getElementById('reportTable');

  if (table.rows.length === 0) {
    alert('The table cannot be empty');
    e.preventDefault();
  }
});

const tableBody = document.getElementById('tableBody');

// Crear objetos para vincular los nombres con los apellidos y viceversa
const nameToLastName = {};
const lastNameToName = {};

function addTableRow(name, lastName, mail, projects, hours, homeworks) {
const newRow = document.createElement('tr');

const nameCell = document.createElement('td');
nameCell.textContent = name;
newRow.appendChild(nameCell);

const lastNameCell = document.createElement('td');
lastNameCell.textContent = lastName;
newRow.appendChild(lastNameCell);

const mailCell = document.createElement('td');
mailCell.textContent = mail;
newRow.appendChild(mailCell);

const projectsCell = document.createElement('td');
projectsCell.textContent = projects;
newRow.appendChild(projectsCell);

const hoursCell = document.createElement('td');
hoursCell.textContent = hours;
newRow.appendChild(hoursCell);

const homeworksCell = document.createElement('td');
homeworksCell.textContent = homeworks;
newRow.appendChild(homeworksCell);

tableBody.appendChild(newRow);

// Agregar el apellido al objeto de nombres
if (!nameToLastName[name]) {
  nameToLastName[name] = [];
}
nameToLastName[name].push(lastName);

// Agregar el nombre al objeto de apellidos
if (!lastNameToName[lastName]) {
  lastNameToName[lastName] = [];
}
lastNameToName[lastName].push(name);
}

addTableRow('John', 'Doe', 'johndoe@example.com', 5, 20, 2);
addTableRow('victor', 'sire', 'victormsire@gmail.com', 3, 12, 2);
addTableRow('camilo', 'chamorro', 'camilo@gmail.com', 4, 16, 1);
addTableRow('leonardo', 'perez', 'leonardo@gmail.com', 3, 14, 1);

const filterByNameSelect = document.getElementById('filterByName');
const filterByLastNameSelect = document.getElementById('filterByLastName');

const names = Array.from(tableBody.getElementsByTagName('td')).filter((cell, index) => index % 6 === 0).map((cell) => cell.textContent);
const uniqueNames = [...new Set(names)];

const lastNames = Array.from(tableBody.getElementsByTagName('td')).filter((cell, index) => index % 6 === 1).map((cell) => cell.textContent);
const uniqueLastNames = [...new Set(lastNames)];

uniqueNames.forEach((name) => {
const option = document.createElement('option');
option.textContent = name;
filterByNameSelect.appendChild(option);
});

uniqueLastNames.forEach((lastName) => {
const option = document.createElement('option');
option.textContent = lastName;
filterByLastNameSelect.appendChild(option);
});

filterByNameSelect.addEventListener('change', function () {
const selectedName = this.value;

if (selectedName === "Select Item") {
  // Restablecer los filtros de nombre y apellido a las opciones originales
  filterByNameSelect.innerHTML = originalNameOptions;
  filterByLastNameSelect.innerHTML = originalLastNameOptions;

  // Restablecer la tabla para mostrar todas las filas originales
  for (let i = 0; i < originalRows.length; i++) {
    originalRows[i].style.display = '';
  }
} else {
  filterByUser(selectedName, 'name');

  // Actualizar las opciones del filtro de apellidos
  const linkedLastNames = nameToLastName[selectedName] || [];
  filterByLastNameSelect.innerHTML = linkedLastNames.map(lastName => `<option>${lastName}</option>`).join('');
}
});

filterByLastNameSelect.addEventListener('change', function () {
const selectedLastName = this.value;
filterByNameSelect.innerHTML = originalNameOptions;
  filterByLastNameSelect.innerHTML = originalLastNameOptions;

if (selectedLastName === "Select Item") {
  // Restablecer los filtros de nombre y apellido a las opciones originales
  filterByNameSelect.innerHTML = originalNameOptions;
  filterByLastNameSelect.innerHTML = originalLastNameOptions;

  // Restablecer la tabla para mostrar todas las filas originales
  for (let i = 0; i < originalRows.length; i++) {
    originalRows[i].style.display = '';
  }
} else {
  filterByUser(selectedLastName, 'lastName');

  // Actualizar las opciones del filtro de nombres
  const linkedNames = lastNameToName[selectedLastName] || [];
  filterByNameSelect.innerHTML = linkedNames.map(name => `<option>${name}</option>`).join('');
}
});

function filterByUser(selectedValue, type) {
const rows = tableBody.getElementsByTagName('tr');

for (let i = 0; i < rows.length; i++) {
  const row = rows[i];
  const nameCell = row.getElementsByTagName('td')[0];
  const lastNameCell = row.getElementsByTagName('td')[1];

  if (type === 'name' && (nameCell.textContent === selectedValue || selectedValue === '')) {
    row.style.display = '';
  } else if (type === 'lastName' && (lastNameCell.textContent === selectedValue || selectedValue === '')) {
    row.style.display = '';
  } else {
    row.style.display = 'none';
  }
}
}

// Almacenar las opciones originales de los filtros
const originalNameOptions = uniqueNames.map(name => `<option>${name}</option>`).join('');
const originalLastNameOptions = uniqueLastNames.map(lastName => `<option>${lastName}</option>`).join('');

// Almacenar las filas originales de la tabla
const originalRows = Array.from(tableBody.getElementsByTagName('tr'));

document.getElementById('selectedFilter').addEventListener('change', function () {
const selected = this.value;

if (selected === "0") {
  // Restablecer los filtros de nombre y apellido a las opciones originales
  filterByNameSelect.innerHTML = originalNameOptions;
  filterByLastNameSelect.innerHTML = originalLastNameOptions;

  // Restablecer la tabla para mostrar todas las filas originales
  for (let i = 0; i < originalRows.length; i++) {
    originalRows[i].style.display = '';
  }
}
});
function filterTableByProjects() {
var numberProjects = parseInt(document.getElementById('numberProjects').value);
var tableRows = document.getElementById('reportTable').getElementsByTagName('tr');

for (var i = 1; i < tableRows.length; i++) {
  var projectsCell = tableRows[i].getElementsByTagName('td')[3];
  var projects = parseInt(projectsCell.textContent);

  if (projects < numberProjects) {
    tableRows[i].style.display = 'none';
  } else {
    tableRows[i].style.display = '';
  }
}
updateRangeValue('numberValue', numberProjects);
}
function setMaxValue() {
var tableRows = document.getElementById('reportTable').getElementsByTagName('tr');
var maxProjects = 0;

for (var i = 1; i < tableRows.length; i++) {
  var projectsCell = tableRows[i].getElementsByTagName('td')[3];
  var projects = parseInt(projectsCell.textContent);

  if (projects > maxProjects) {
    maxProjects = projects;
  }
}

document.getElementById('numberProjects').max = maxProjects;
}
function filterTableByHours() {
var numberHours = document.getElementById('numberHours').value;
var tableRows = document.getElementById('reportTable').getElementsByTagName('tr');

for (var i = 1; i < tableRows.length; i++) {
  var hoursCell = tableRows[i].getElementsByTagName('td')[4];
  var hours = parseInt(hoursCell.textContent);

  if (hours > numberHours) {
    tableRows[i].style.display = '';
  } else {
    tableRows[i].style.display = 'none';
  }
}
updateRangeValue('hoursValue', numberHours);
}

function updateRangeValue(elementId, value) {
document.getElementById(elementId).textContent = value;
}
function filterTableByHomeworkDelay() {
var homeworkDelay = document.getElementById('homeworkDelay').value;
var tableRows = document.getElementById('reportTable').getElementsByTagName('tr');

for (var i = 1; i < tableRows.length; i++) {
  var homeworksCell = tableRows[i].getElementsByTagName('td')[5];
  var homeworks = parseInt(homeworksCell.textContent);

  if (homeworks > homeworkDelay) {
    tableRows[i].style.display = '';
  } else {
    tableRows[i].style.display = 'none';
  }
}

// Llamar a updateRangeValue con el ID y el valor actual del span correspondiente
updateRangeValue('homeworkDelayValue', homeworkDelay);
}