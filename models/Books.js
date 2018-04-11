const mongoose = require("mongoose");
const {Schema} = mongoose;

var bookSchema = new Schema({
    name:String,
    description:{type:String,minlength:10},
    course:String,
    module:String,
    moduleCode:String,
    uploadDate:new Date('MMM-DD-YYYY'),
    uploadedBy:{type:Schema.Types.ObjectId,ref:'User'},
    url:{type:String, required:true}
});

mongoose.model('books',bookSchema);