import React, { Component, useState } from "react";
import { useNavigate } from "react-router-dom";

// function toComponentB() {
//   let navigate = useNavigate;
//   return navigate(this.props.route);
// }

function LoginButton() {
  // state = {
  //   role: this.props.role,
  //   route: this.props.route,
  // };
  let navigate = useNavigate();
  // render() {
  return (
    <div className="login-button">
      <button
        type="submit"
        className="login-page"
        onClick={() => {
          navigate("/order");
        }}
      >
        Assemble my sequence!
        {/* {this.state.role + " Login"} */}
      </button>
      {/* <form> */}
      {/* <input
            type="submit"
            value={this.state.role + " Login"}
            id="login-page"
          /> */}
      {/* </form> */}
    </div>
  );
  // }
}

export default LoginButton;
