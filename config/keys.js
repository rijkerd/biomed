
module.exports = {
    database:'mongodb://localhost:27017/classDB1',
    secret:'jsdjfbsdf_DasdaASdsadmxzcndsufh'
}

// if(!createUser){
//     try{
//         const newUser = await new User({
//             email:email,
//             password:generateHash(password)
//         }).save();

//         return done(null,newUser);
//     }catch(e){
//         console.log(e);
//     }
// }else{
//     return done("The email already exists",false);
// }