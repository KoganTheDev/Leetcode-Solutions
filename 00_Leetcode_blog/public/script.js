let entryCount = 0;

document.addEventListener('DOMContentLoaded', (event) => {
    setTodayDate();
    loadEntries();
});

function setTodayDate() {
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('entry-date').value = today;
}

function formatDate(dateString) {
    const [year, month, day] = dateString.split('-');
    return `${day}/${month}/${year}`;
}

function parseDate(dateString) {
    const [day, month, year] = dateString.split('/');
    return `${year}-${month}-${day}`;
}

function addEntry() {
    const entryContent = document.getElementById('entry-content').value;
    const entryDate = new Date().toLocaleDateString();
    entryCount++;

    const entry = {
        id: entryCount,
        date: entryDate,
        content: entryContent
    };

    displayEntry(entry);
    saveEntry(entry);

    // Clear the textarea after adding the entry
    document.getElementById('entry-content').value = '';
}

function saveEntry(entry) {
    fetch('/entries', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(entry)
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}

function loadEntries() {
    fetch('/entries')
    .then(response => response.json())
    .then(entries => {
        entries.forEach(entry => {
            if (entry.id > entryCount) {
                entryCount = entry.id;
            }
            displayEntry(entry);
        });
    })
    .catch(error => console.error('Error:', error));
}

function displayEntry(entry) {
    const entryContainer = document.getElementById('entries-container');
    const entryDiv = document.createElement('div');
    entryDiv.className = 'entry';
    entryDiv.id = `entry-${entry.id}`;
    entryDiv.innerHTML = `
        <div class="entry-serial">#${entry.id}</div>
        <div class="entry-date">${entry.date}</div>
        <div class="entry-content"><pre>${entry.content}</pre></div>
        <button type="button" onclick="deleteEntry(${entry.id})">Delete</button>
    `;
    entryContainer.appendChild(entryDiv);
}

function deleteEntry(entryId) {
    fetch(`/entries/${entryId}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        const entryDiv = document.getElementById(`entry-${entryId}`);
        if (entryDiv) {
            entryDiv.remove();
        }
    })
    .catch(error => console.error('Error:', error));
}

function filterEntriesByDate() {
    const filterDate = document.getElementById('filter-date').value;
    if (!filterDate) {
        alert('Please select a date to filter.');
        return;
    }

    const formattedFilterDate = formatDate(filterDate);

    fetch('/entries')
    .then(response => response.json())
    .then(entries => {
        const filteredEntries = entries.filter(entry => entry.date === formattedFilterDate);
        const entryContainer = document.getElementById('entries-container');
        entryContainer.innerHTML = ''; // Clear existing entries
        filteredEntries.forEach(entry => displayEntry(entry));
    })
    .catch(error => console.error('Error:', error));
}