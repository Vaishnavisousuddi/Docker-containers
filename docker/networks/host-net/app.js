const express = require("express");
const app = express();

app.get("/", (req, res) => {
    res.send("Hello from Node.js on Host Network!");
});

app.listen(5000, () => console.log("Node.js running on port 5000"));
