const express = require("express");
const app = express();
const PORT = process.env.PORT || 5000;
const mongoose = require('mongoose');
const passport = require('passport');
const flash = require('connect-flash');

const morgan = require('morgan');
const cookieParser = require('cookie-parser');
const bodyParser = require("body-parser");
const session = require("express-session");


const configDB = require("./config/keys");

mongoose.connect(configDB.url);

require('./services/passport')(passport);

app.use(morgan('dev'));
app.use(cookieParser());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));

app.set('view engine','ejs');

app.use(session({
  secret:'mdebwedokskadklaskldnasndsk',
  resave:true,
  saveUninitialized:true
}));
app.use(passport.initialize());
app.use(passport.session());
app.use(flash());



require("./routes/authRoutes")(app,passport);


app.listen(PORT, () => {
  console.log("App Listening on 5000");
});
