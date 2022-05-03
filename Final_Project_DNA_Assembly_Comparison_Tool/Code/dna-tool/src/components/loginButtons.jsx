import React, { Component } from "react";
import LoginButton from "./loginButton";

class LoginButtons extends Component {
  state = {
    roles: ["Admin", "User"],
    routes: ["/admin", "/order"],
  };
  render() {
    return (
      <div className="login-button">
        {/* {this.state.roles.map((role) => (
          <LoginButton role={role} key={role} />
        ))} */}

        <LoginButton />

        {/* {this.state.routes.map((route) => (
          <LoginButton route={route} key={route} />
        ))} */}
      </div>
    );
  }
}

export default LoginButtons;
