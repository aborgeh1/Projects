import axios from "axios";
import {useEffect,useState } from "react";
export function Login(){
    const [username,setusername]=useState('')
    const [password,setpassword]=useState('')
const Data={
    username,
    password,
}

function handlesubmit(event){
    event.preventDefault()
    console.log(Data)
axios.post("http://localhost:5000/app/login",Data)
.then((res)=>{console.log('Login details submited successfully')})
.catch(err=>console.log(err))
}
return <div>
    <form onSubmit={handlesubmit}>
    <input  onChange={(e)=>setusername(e.target.value)} name = "Username" value={username} placeholder="Username" ></input>
        <input  onChange={(e) => setpassword(e.target.value)}  name = "Password" value={password} placeholder="Password" ></input>
        <input type='submit'></input>
        </form>
</div>
}