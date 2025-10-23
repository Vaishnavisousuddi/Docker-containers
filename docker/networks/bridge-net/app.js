const express = require("express");
const redis = require("redis");

const app = express();
const client = redis.createClient({
  host: "172.17.0.3",  // Redis container IP (get via docker inspect)
  port: 6379
});

client.on("error", (err) => console.log("Redis Client Error", err));

app.get("/", (req, res) => {
  client.incr("visits", (err, visits) => {
    res.send(`Number of visits: ${visits}`);
  });
});

app.listen(3000, () => console.log("Node app running on port 3000"));
