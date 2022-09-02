import mongoose  from "mongoose";
const schema =  new mongoose.Schema({
    Username:{
        type:String,
        required:true,
    },
    Password:{
        type:String,
        default:0,
    },

})
console.log('successfully connected');
export const User= mongoose.model("martin2",schema);

 