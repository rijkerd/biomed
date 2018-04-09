const mongoose = require("mongoose");
const bcrypt = require('bcrypt-nodejs');
const crypto = require('crypto');
const { Schema } = mongoose;

const userSchema = new Schema({
  admissionNumber:{type:Number, unique:true, minlength:11},
  password:{type:String,unique:true},
  //approved:Boolean
});


// Hash the password before saving it to the database
userSchema.pre('save',(next) => {
  var user = this;
  if(!user.isModified('password')) return next();
  bcrypt.genSalt(10,(err,salt) => {
    if(err) return next(err);
    bcrypt.hash(user.password,salt,null,(err,hash) => {
      if(err) return next(err);
      user.password = hash;
      next();
    });
  });
});


// Compare the password provided with the one in the database
userSchema.methods.comparePassword = (password) => {
  return bcrypt.compareSync(password,this.password);
}

module.exports = mongoose.model("user",userSchema);