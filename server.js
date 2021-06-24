const express = require('express');
const multer = require('multer')
const session = require('express-session')
const flash = require('express-flash')

const upload = multer()

const methodOverride = require('method-override');
const basics = require('./src/basic')

const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

app.use(methodOverride('_method'));

app.use(flash())

app.use('/', basics)

app.listen(port, () => {
    console.log(`Server running on ${port}`);
});