import express from "express";
import {Register,Login,profile} from "./controller.js";
export const route = express.Router()
route.post("/register",Register);
route.post('/login',Login)
route.get('/profile',profile)
