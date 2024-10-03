const frameworksData = document.getElementById("frameworks-data").textContent;
const frameworks = JSON.parse(frameworksData);

const databaseSelect = document.getElementById("database-select");
const languageSelect = document.getElementById("language-select");
const frameworkContainer = document.getElementById("framework-container");

function createFrameworkDropdown() {
    const frameworkSelect = document.getElementById("framework-select");
    if (frameworkSelect)
        return frameworkSelect;

    const label = document.createElement("label");
    label.setAttribute("for", "framework-select");
    label.className = "form-label";
    label.textContent = "Framework:";

    const select = document.createElement("select");
    select.id = "framework-select";
    select.className = "form-select";

    frameworkContainer.appendChild(label);
    frameworkContainer.appendChild(select);
    return select;
}

function updateFramework() {
    const selectedLanguage = languageSelect.value;

    let frameworkSelect = createFrameworkDropdown();
    frameworkSelect.innerHTML = "";
    if (frameworks[selectedLanguage]) {
        frameworks[selectedLanguage].forEach(framework => {
            const option = document.createElement("option");
            option.value = framework.value;
            option.className = "form-option"
            option.text = framework.name;
            frameworkSelect.appendChild(option);
        });
    } else {
        frameworkContainer.innerHTML = "";
    }
}


function updateDatabase() {
    const selectedDatabase = databaseSelect.value;

    fetch(questionUrl.replace("placeholder", selectedDatabase))
        .then(response => {
            if (!response.ok) {
                throw new Error("Error while loading the questions");
            }
            return response.json();
        }).then(data => {
            if (data) {
                const questionExplorer = document.getElementById("question-explorer");
                questionExplorer.innerHTML = "";

                const ul = document.createElement("ul");
                data.forEach(question => {
                    const li = document.createElement("li");
                    li.value = question.q_no;
                    li.textContent = question.q_text.substring(0, 21);
                    ul.appendChild(li);
                });
                questionExplorer.appendChild(ul);
            }
        }).catch(error => {
            console.error('Fetch error:', error);
        });

}


function clearInput() {
    console.log("Clear...")
}


function submitForm() {
    console.log("Submit...")
}


document.addEventListener('DOMContentLoaded', function () {
    updateDatabase();
});
