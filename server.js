const express = require("express");
const mongoose = require("mongoose");
const cookieSession = require("cookie-session");
const passport = require("passport");
const bodyParser = require("body-parser");
const keys = require("./config/dev");
// require("./models/User");
// require("./services/passport");

const app = express();
mongoose.connect(keys.mongoURI);

app.use(bodyParser.json());
// app.use(
//   cookieSession({
//     maxAge: 30 * 24 * 60 * 60 * 1000,
//     keys: [keys.cookieKey]
//   })
// );
//app.use(passport.initialize());
//app.use(passport.session());

//require("./routes/authRoutes")(app);

app.get("*", (req, res) => {
  res.send("Hello World");
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log("App Listening on 5000");
});
