import React, { Component } from "react";
import LoginBg from "../components/loginBackground";
import LoginButtons from "../components/loginButtons";

class LoginScreen extends Component {
  state = {};
  render() {
    return (
      <div>
        <LoginBg />
        <LoginButtons />
      </div>
    );
  }
}

export default LoginScreen;
