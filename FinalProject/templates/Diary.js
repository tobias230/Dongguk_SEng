class Diary {

    constructor(language = "en-US") {
        this.entries = [];
        this.language = language;
    
        this.nameInput = document.getElementById("name");
        this.dateInput = document.getElementById("date");
        this.confirmButton = document.getElementById("confirm");
        this.printElement = document.getElementById("task-list");
        this.setEvents();
    }

    setEvents() {
        this.confirmButton.onclick = () => {
            const entry = new Entry(this.nameInput.value, this.dateInput.value);
            this.entries.push(entry);
            this.printEntries();
        };
    }

    printEntries() {
        this.printElement.innerHTML = "";
        for (let i = 0; i < this.entries.length; i++) {
            const entry = this.entries[i];
            this.printElement.innerHTML += `<h3>${entry.name}</h3>when: ${entry.date}<br>done: ${entry.done}`;
        }
    }
}
