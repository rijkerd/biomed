const mongoose = require("mongoose");
const { Schema } = mongoose;

const userSchema = new Schema({
  googleId:String,
  facebookId:String,
  username:String,
  email:String,
  photo:String,
  admin:Boolean
});

mongoose.model("users",userSchema);
