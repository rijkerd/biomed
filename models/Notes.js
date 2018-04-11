const mongoose = require('mongoose');
const {Schema} = mongoose;

var notesSchema = new Schema({
    course:String,
    moduleName:String,
    moduleCode:String,
    uploadedBy:{type:Schema.Types.ObjectId,ref:'User'},
    uploadedDate:new Date('MMM-DD-YYYY'),
    url:String
});

mongoose.model('notes',notesSchema);