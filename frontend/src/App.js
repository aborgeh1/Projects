import logo from './logo.svg';
import './App.css';
import {User_details} from "./Admin.js";
import {Product_Display} from "./Product_Page.js"
import {Product_details} from "./Product_Details.js"
import {Register} from "./Register_page.js"
import {NoPage} from "./empty.js"
import {Login} from './Login_Page.js'
import {Profile} from './Profile.js'
import { BrowserRouter, Route,Switch} from "react-router-dom";

function App() {
  return (
<BrowserRouter>
<Switch>
    <Route exact path='/adminPage' ><User_details/></Route>
    <Route exact path='/profile' ><Profile/></Route>
    <Route exact path='/login' ><Login/></Route>
    <Route  path='/producDisplay' ><Product_Display/></Route>
    <Route path='/productDetails' ><Product_details/></Route>
    <Route path='/register' ><Register/></Route>
    <Route path='*' ><NoPage/></Route>   
</Switch>
</BrowserRouter>  
  );
}

export default App;
