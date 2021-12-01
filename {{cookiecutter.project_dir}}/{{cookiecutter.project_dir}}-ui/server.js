const express = require("express");
const path = require("path");
const app = express();
const port = 80;

const buildFolder = "./build";

const { API_HOST } = process.env;

app.set("views", path.join(__dirname, buildFolder));
app.engine("html", require("ejs").renderFile);

app.use(
  "/static",
  express.static(path.join(__dirname, `${buildFolder}/static`))
);

app.use(
  "/images",
  express.static(path.join(__dirname, `${buildFolder}/images`))
);

app.use("/__health", (req, res) => {
  res.header("Content-Type", "application/json");
  res.send({ status: "ok" });
});

app.get("/*", function (req, res) {
  res.render("index.html", {
    API_HOST,
  });
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));
