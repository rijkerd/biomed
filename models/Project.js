const mongoose = require('mongoose');
const {Schema} = mongoose;

var projectSchema = new Schema({
    title:{type:String,unigue:true},
    description:String,
    course:String,
    createdOn:new Date ('MMMM-DD-YYYY'),
    owner:{type:Schema.Types.ObjectId,ref:'User'}
});

module.exports = mongoose.model('project',projectSchema);





