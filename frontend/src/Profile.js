import axios from "axios";
import {useEffect,useState } from "react";
export function Profile(){
    const [username,setusername]=useState('')
    const [password,setpassword]=useState('')
useEffect(()=>{
    axios.get("http://localhost:5000/app/profile").then((res)=>{
    const Data = res.data
    setusername(Data?.username)
    setpassword(Data?.password)
}).catch(err=>console.log(err))
},[])
    return <div>
  <form >
        <input  onChange={(e)=>setusername(e.target.value)} name = "Username" value={username} placeholder="Username" ></input>
        <input  onChange={(e) => setpassword(e.target.value)}  name = "Password" value={password} placeholder="Password" ></input>
        <input type='submit'></input>
    </form>
    </div>
}