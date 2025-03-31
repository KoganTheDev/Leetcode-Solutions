const express = require('express');
const fs = require('fs');
const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.static('public'));

const entriesFile = 'entries.json';

// Load entries from a file (if exists)
let entries = [];
if (fs.existsSync(entriesFile)) {
    const data = fs.readFileSync(entriesFile);
    entries = JSON.parse(data);
}

// Save entries to a file
function saveEntries() {
    fs.writeFileSync(entriesFile, JSON.stringify(entries, null, 2));
}

// Get all entries
app.get('/entries', (req, res) => {
    res.json(entries);
});

// Add a new entry
app.post('/entries', (req, res) => {
    const newEntry = req.body;
    entries.push(newEntry);
    saveEntries();
    res.status(201).json({ message: 'Entry added successfully', entry: newEntry });
});

// Delete an entry by ID
app.delete('/entries/:id', (req, res) => {
    const entryId = parseInt(req.params.id, 10);
    entries = entries.filter(entry => entry.id !== entryId);
    saveEntries();
    res.json({ message: 'Entry deleted successfully' });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});