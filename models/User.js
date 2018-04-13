const mongoose = require("mongoose");
const bcrypt = require("bcrypt-nodejs");
const { Schema } = mongoose;

const userSchema = new Schema({
  email: { type: String, unique: true },
  password: { type: String, required: true }
  //approved:Boolean
});

// Hash the password before saving it to the database
// userSchema.pre("save", next => {
//   var user = this;
//   bcrypt.genSalt(10, (err, salt) => {
//     if (err) return next(err);
//     bcrypt.hash(user.password, salt, null, (err, hash) => {
//       if (err) return next(err);
//       user.password = hash;
//       next();
//     });
//   });
// });

userSchema.methods.generateHash = password => {
  return bcrypt.hashSync(password, bcrypt.genSaltSync(8), null);
};

// Compare the password provided with the one in the database
userSchema.methods.comparePassword = password => {
  return bcrypt.compareSync(password, this.password);
};

module.exports = mongoose.model("User", userSchema);
