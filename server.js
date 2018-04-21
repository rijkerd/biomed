const express = require("express");
const path = require("path");
const app = express();
const mongoose = require("mongoose");
const passport = require("passport");
//const flash = require('connect-flash');

const morgan = require("morgan");
const cookieParser = require("cookie-parser");
const cors = require("cors");
const bodyParser = require("body-parser");
const session = require("express-session");

const keys = require("./config/keys");

mongoose.connect(keys.database, { useMongoClient: true });
mongoose.connection.on("connected", () => {
  console.log("Connected to Database" + keys.database);
});

mongoose.connection.on("error", err => {
  console.log("Database error" + err);
});


app.use(express.static(path.join(__dirname,'public')));
app.use(morgan("dev"));
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//app.set('view engine','ejs');

app.use(
  session({
    secret: "mdebwedokskadklaskldnasndsk",
    resave: true,
    saveUninitialized: true
  })
);
app.use(passport.initialize());
//app.use(passport.session());
//app.use(flash());

require("./services/passport")(passport);

require("./routes/authRoutes")(app);

app.get("/", (req, res) => {
  res.json({ status: true, msg: "It works" });
});
app.get("*",(req,res) => {
  res.sendFile(path.join(__dirname,'public/index.html'));
})

app.listen(keys.port, () => {
  console.log(`App Listening on ${keys.port} `);
});
