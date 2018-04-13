const LocalStrategy = require("passport-local").Strategy;

var User = require("../models/User");

module.exports = passport => {

  /**
   * For Serializing the user for session
   */

  passport.serializeUser((user, done) => {
    done(null, user.id);
  });

  /**
   * For deserialize the user
   */

  passport.deserializeUser((id, done) => {
    User.findById(id, (err, user) => {
      done(err, user);
    });
  });

  /**
   * Handles user login email and password
   */

  passport.use(
    "local-login",
    new LocalStrategy(
      {
        usernameField: "email",
        passwordField: "password",
        passReqToCallback: true
      },
      async (req, email, password, done) => {
        if (email) email = email.toLowerCase();

        try {
          const existingUser = await User.findOne({ email: email });

          if (!existingUser)
            return done(
              null,
              false,
              req.flash("loginMessage", "No user found.")
            );

          if (!existingUser.comparePassword(password))
            return done(
              null,
              false,
              req.flash("loginMessage", "Wrong Password")
            );
          else return done(null, existingUser);
        } catch (e) {
          throw new Error("Error while trying to find User");
        }
      }
    )
  );
  /*
    local Strategy to enable user to Sign Up locally
    By passing email and password fields
  */
  passport.use(
    "local-signup",
    new LocalStrategy(
      {
        usernameField: "email",
        passwordField: "password",
        passReqToCallback: true
      },
      async (req, email, password, done) => {
        if (email) email = email.toLowerCase();

        let user = await req.user;
        if (!user) {
          try {
            const createUser = await User.findOne({ email: email });

            //Check if user Exists
            if (createUser) {
              return done(
                null,
                false,
                req.flash("signupMessage", "The email is already taken")
              );
            } else {
              try {
                const newUser = await new User({
                  email: email,
                  password: generateHash(password)
                }).save();

                return done(null, newUser);
              } catch (e) {
                throw new Error("Unable to save new User");
              }
            }
          } catch (e) {
            throw new Error("An error occured trying to sign up user");
          }
        }
      }
    )
  );
};
