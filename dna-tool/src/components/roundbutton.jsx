import React, { Component } from "react";

class RoundButton extends Component {
  state = {
    inputType: this.props.inputType,
  };
  render() {
    return (
      <div className="rb-container">
        <label> {this.state.inputType} </label>
        <input type="checkbox" id="round-btn" className="round-btn" />
      </div>
    );
  }
}

export default RoundButton;
