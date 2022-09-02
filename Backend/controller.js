import bcrypt from 'bcryptjs'
import jwt from 'jsonwebtoken'
import cookieParser from 'cookie-parser'
import {User} from "./model.js";
export function Register(req,res){
    const {Username,Password}=req.body
    console.log(Username,Password)
    const mydata = new User({
        Username:Username,
        Password:bcrypt.hash(Password,10).then(g=>'hashed succesfully').catch(err=>'error occured')
    })
    mydata.save()
    // console.log(mydata)
    .then((dat)=>console.log(' The data has been been saved successfully'))
    .catch((err)=>console.log(err,'error was thrown'))
};
export  function Login(req,res){
    const {username,password}=req.body
    const user = User.findOne({Username:username},(err,item)=>{
        if (err){
            console.log(err)
        }else if (item){
            // console.log(item.Username,item.Password)
        const auth = bcrypt.compare(password,item.Password)
        if (auth){
          console.log('user is authenticated')
        }else {
            console.log('User entered invallid statement') 
        }}
        else if(!item){
           console.log('invalid')
        }
    })
   
  

        
    // }
    

}
export function profile(req,res){
    const Data={username:'Martin',password:'0549martin'}
    res.send(Data)
}
sds