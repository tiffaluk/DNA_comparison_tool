import React, { Component } from "react";

class RoundButton extends Component {
  state = {
    inputType: this.props.inputType,
  };

  onChangeValue = this.onChangeValue.bind(this);

  onChangeValue(event) {
    console.log(event.target.value);
  }

  render() {
    return (
      <div className="rb-container" onChange={this.onChangeValue}>
        <label> {this.state.inputType} </label>
        <input type="radio" className="round-btn" name="input-type" />
      </div>
    );
  }
}

export default RoundButton;
