const mongoose = require('mongoose');
const crypto = require('crypto');
const {Schema} = mongoose;

var userProfile = new Schema({
    _user:{type:Schema.Types.ObjectId,ref:'User'},
    about:{type:String,default:''},
    profilePic:{type:String,default:''},
    course:{type:String,default:''},
    department:{type:String,default:'Electrical'},
    email:{type:String,unique:true,lowercase:true},
    approved:Boolean,
    Username:String
});


//Save user profile once the gravator image is returned
userProfile.pre('save', (next) => {
    var userProfile =this;
    if(userProfile.gravatar){
        next();
    };
})

userProfile.methods.gravatar = (size) => {
    if(!this.size) size = 200
    if (!this._user) return 'https://gravator.com/avatar/?s' + size + '&d=retro';
    var md5 = crypto.createHash('md5').update(this._user).digest('hex');
    return 'https://gravator.com/avatar/' + md5 + '?s=' + size + '&d=retro';
}