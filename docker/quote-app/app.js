const express = require('express');
const app = express();

const quotes = [
    "Believe in yourself!",
    "Keep pushing forward.",
    "Failure is just a step to success.",
    "Stay positive, work hard, make it happen.",
    "Dream big and dare to fail."
];

app.get('/', (req, res) => {
    res.json({ message: "Welcome to the Random Quote API!" });
});

app.get('/quote', (req, res) => {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    res.json({ quote: quotes[randomIndex] });
});

app.listen(3000, '0.0.0.0', () => {
    console.log("Quote API running on port 3000");
});
