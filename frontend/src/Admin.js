import { useState, useEffect} from "react";
import axios from "axios"
export function User_details(){
    const [details, setdetails]=useState({
        Username:"4",
        Passord:"4"
    });
   const Onsubmit=(event)=>{
        event.preventDefaults()
    //   useEffect(axios.post("localhost:5000/app/home",details)
    //     ,[])  
    }
    console.log(details.Username)
    return <div>
        <form onSubmit={Onsubmit}>
            <input  onChange={(e)=>setdetails(e.target.value)} name = "Username" value={details.Username} placeholder="Username" ></input>
            <input  onChange={(e) => setdetails(e.target.value)}  name = "Password" value={details.Password} placeholder="Password" ></input>
            <button> Submit</button>
        </form>
    </div>
}
