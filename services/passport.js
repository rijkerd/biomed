"use strict";
const passport = require("passport");
const keys = require("../config/dev");
const GoogleStrategy = require("passport-google-oauth20").Strategy;
const FacebookStrategy = require("passport-facebook").Strategy;
const mongoose = require("mongoose");


const User = mongoose.model("users");

passport.serializeUser((user, done) => {
  done(null, user.id);
});

passport.deserializeUser((id, done) => {
  User.findById(id).then(user => {
    done(null, user);
  });
});

passport.use(
  new GoogleStrategy(
    {
      clientID: keys.googleClientID,
      clientSecret: keys.googleClientSecret,
      callbackURL: "/auth/google/callback"
    },
    async (accessToken, refreshToken, profile, done) => {
      const existingUser = await User.findOne({ Id: profile.id });
      if (existingUser) {
        return done(null, existingUser);
      }
      const user = await new User({
        googleId: profile.id,
        name: profile.displayName,
        email: profile.emails[0].value
      }).save();
    }
  )
);

passport.use(
  new FacebookStrategy(
    {
      clientID:keys.facebookAppId,
      clientSecret:keys.facebookSecret,
      callbackURL:"/auth/facebook/callback"
    },
    (accessToken,refreshToken,profile,done) => {
      User.findOrCreate({id:profile.id}),(req,res) =>{
        return done(null,user);
      }

      console.log(profile);
    }
  )
)
