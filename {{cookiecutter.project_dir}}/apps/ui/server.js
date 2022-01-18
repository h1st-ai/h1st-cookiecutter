const express = require('express');
const {createProxyMiddleware} = require('http-proxy-middleware');

const {API_HOST} = process.env;
const port = 5000;

const app = express();

app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    next();
});

app.use(createProxyMiddleware('/api/', {
    target: `http://${API_HOST}`,
    changeOrigin: true,
}));

app.use(express.json());
app.use(express.urlencoded({extended: false}));

app.listen(port, () => console.log(`ExpressJS app listening on port ${port}!`));