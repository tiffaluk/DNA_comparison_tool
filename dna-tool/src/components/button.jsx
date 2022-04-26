import React, { Component } from "react";
import { useNavigate } from "react-router-dom";

function Button() {
  //   state = {};
  //   render() {
  let navigate = useNavigate();

  return (
    <div className="submit-button">
      <button
        type="submit"
        className="submitButton"
        onClick={() => {
          navigate("/result");
        }}
      >
        Submit
      </button>
    </div>
  );
  //   }
}

export default Button;
