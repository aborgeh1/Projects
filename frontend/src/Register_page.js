import axios from "axios";
import {useEffect,useState } from "react";
export function Register(){
   const [username,setusername]=useState('')
   const  [password,setpassword]=useState('')
   const Data = {
    Username:username,
    Password:password
   }

     const handlesubmit=(event)=>{
        event.preventDefault()
        // }catch(err){console.log(err)}
        console.log(Data)
        axios.post("http://localhost:5000/app/register",Data)
            .then((res)=>{
                    console.log(res.data)})
            .catch((e)=>{console.log('There was an error',e)})
     }
    return <div>
        <form onSubmit={handlesubmit}>
        <input  onChange={(e)=>setusername(e.target.value)} name = "Username" value={username} placeholder="Username" ></input>
        <input  onChange={(e) => setpassword(e.target.value)}  name = "Password" value={password} placeholder="Password" ></input>
        <input type='submit'></input>
    </form>
    </div>
    }
