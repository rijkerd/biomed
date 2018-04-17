const mongoose = require("mongoose");
const bcrypt = require("bcrypt-nodejs");
const { Schema } = mongoose;

const userSchema = Schema({
  admissionNumber: {
    type: Number
  },
  email: {
    type: String,
    required: true
  },
  username: {
    type: String,
    required: true
  },
  password: {
    type: String,
    required: true
  }
});

const User = (module.exports = mongoose.model("Users", userSchema));

module.exports.getUserById = (id, cb) => {
  User.findById(id, cb);
};

module.exports.getUserByUsername = (username, cb) => {
  const query = { username: username };
  User.findOne(query, cb);
};

module.exports.getUserByAdmissionNumber = (admissionNumber, cb) => {
  const query = { admissionNumber: admissionNumber };
  User.findOne(query, cb);
};

module.exports.addUser = (newUser, cb) => {
  bcrypt.genSalt(10, (err, salt) => {
    bcrypt.hash(newUser.password, salt, (err, hash) => {
      if (err) throw err;
      newUser.password = hash;
      newUser.save(cb);
    });
  });
};

module.exports.comparePassword = (candidatePassword, hash, cb) => {
  bcrypt.compare(candidatePassword, hash, (err, isMatch) => {
    if (err) throw err;
    cb(null, isMatch);
  });
};
