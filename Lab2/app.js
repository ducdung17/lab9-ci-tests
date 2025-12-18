document.getElementById("addTaskBtn").addEventListener("click", addTask);

function addTask() {
    const taskInput = document.getElementById("taskInput");
    const taskText = taskInput.value.trim();

    if (taskText === "") {
        alert("Пожалуйста, введите задачу!");
        return;
    }
    const taskList = document.getElementById("taskList");
    const taskItem = document.createElement("li");
    const taskLabel = document.createElement("span");
    taskLabel.textContent = taskText;
    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Удалить";
    deleteBtn.className = "delete-btn";
    deleteBtn.addEventListener("click", deleteTask);
    taskItem.appendChild(taskLabel);
    taskItem.appendChild(deleteBtn);
    taskItem.addEventListener("click", toggleComplete);
    taskList.appendChild(taskItem);
    taskInput.value = "";
}

function deleteTask(event) {
    const taskItem = event.target.parentElement;
    taskItem.remove();
}

function toggleComplete(event) {
    const taskItem = event.target;
    taskItem.classList.toggle("completed");
}

const bugReports = [
    {
        title: "Нет уведомления при добавлении пустой задачи",
        steps: "1. Откройте приложение Todo List.\n2. Оставьте поле ввода пустым и нажмите 'Добавить задачу'.",
        expectedResult: "Должно появиться уведомление об ошибке или не разрешать добавить пустую задачу.",
        actualResult: "Нет уведомления, задача не добавляется.",
        severity: "Medium",
        priority: "High",
        environment: getEnvironment()
    },
    {
        title: "Задача не удаляется сразу",
        steps: "1. Откройте приложение Todo List.\n2. Добавьте задачу.\n3. Нажмите кнопку 'Удалить'.",
        expectedResult: "Задача должна быть удалена немедленно.",
        actualResult: "Задача не удаляется сразу, требуется перезагрузка страницы.",
        severity: "High",
        priority: "Medium",
        environment: getEnvironment()
    },
    {
        title: "Невозможно отметить задачу как выполненную",
        steps: "1. Откройте приложение Todo List.\n2. Добавьте задачу.\n3. Щелкните по задаче, чтобы отметить ее как выполненную.",
        expectedResult: "Задача должна быть отмечена как выполненная с зачеркнутым текстом и изменением фона.",
        actualResult: "Задача не изменяет состояние, не отображается как выполненная.",
        severity: "Critical",
        priority: "High",
        environment: getEnvironment()
    }
];

function exportToCSV() {
    const headers = ["Заголовок", "Шаги воспроизведения", "Ожидаемый результат", "Фактический результат", "Severity", "Priority", "Окружение"];
    const rows = bugReports.map(report => [
        report.title,
        report.steps,
        report.expectedResult,
        report.actualResult,
        report.severity,
        report.priority,
        report.environment
    ]);

    const BOM = "\uFEFF";
    let csvContent = BOM + headers.join(",") + "\n"; 
    rows.forEach(row => {
        csvContent += row.join(",") + "\n"; 
    });

    const encodedUri = "data:text/csv;charset=utf-8," + encodeURIComponent(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "bug_reports.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
function getEnvironment() {
    const userAgent = navigator.userAgent;
    let os = "Unknown OS";
    let browser = "Unknown Browser";
    if (userAgent.indexOf("Win") !== -1) os = "Windows 11";
    else if (userAgent.indexOf("Mac") !== -1) os = "MacOS";
    else if (userAgent.indexOf("X11") !== -1) os = "UNIX";
    else if (userAgent.indexOf("Linux") !== -1) os = "Linux";
    if (userAgent.indexOf("Chrome") !== -1) browser = "Chrome";
    else if (userAgent.indexOf("Firefox") !== -1) browser = "Firefox";
    else if (userAgent.indexOf("Safari") !== -1) browser = "Safari";
    else if (userAgent.indexOf("Edge") !== -1) browser = "Edge";
    return `${browser}, ${os}`;
}

const exportButton = document.createElement("button");
exportButton.textContent = "Скачать отчет об ошибках";
exportButton.style.marginTop = "20px";
exportButton.style.padding = "10px 20px";
exportButton.style.backgroundColor = "#4CAF50";
exportButton.style.color = "#fff";
exportButton.style.border = "none";
exportButton.style.borderRadius = "5px";
exportButton.style.cursor = "pointer";
exportButton.addEventListener("click", exportToCSV);
document.body.appendChild(exportButton);
