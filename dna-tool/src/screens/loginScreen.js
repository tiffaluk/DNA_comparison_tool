import React, { Component } from "react";
import { Nav } from "react-bootstrap";
import LoginBg from "../components/loginBackground";
import LoginButtons from "../components/loginButtons";
import NavBar from "../components/navBar";
//import FormButtons from "../components/formButtons";
class LoginScreen extends Component {
  state = {};
  render() {
    return (
      <div>
        {/* <NavBar /> */}
        <LoginBg />
        <LoginButtons />
      </div>
    );
  }
}

export default LoginScreen;
