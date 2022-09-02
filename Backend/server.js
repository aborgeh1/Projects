import express from "express";
import mongoose from "mongoose";
import Cors from 'cors'
import {route} from "./routing.js";
mongoose.connect("mongodb://127.0.0.1:27017/aborgeh",
    {
        useNewUrlParser:true,
        useUnifiedTopology:true
    }
).then(gh=>console.log('connection is successsfull')).catch(err=>console.log(err, 'ERROR OCCURED'))
const app= express();
app.use(Cors())
app.use(express.json());
app.use("/app",route);

app.listen(5000,()=>console.log('Sever is running at the moment'));