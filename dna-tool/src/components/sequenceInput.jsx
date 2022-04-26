import React, { Component } from "react";
import "./userview.css";

class SequenceInput extends Component {
  state = {};
  render() {
    return (
      <div className="seq-input">
        <input
          type="text"
          //   id="seqInput"
          name="seqInput"
          className="input-box"
        ></input>
      </div>
    );
  }
}

export default SequenceInput;
