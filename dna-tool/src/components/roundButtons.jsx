import React, { Component } from "react";
import RoundButton from "./roundbutton";

class RoundButtons extends Component {
  state = {
    inputTypes: ["ssDNA", "dsDNA", "RNA", "Amino Acids"],
  };
  render() {
    return (
      <div className="round-buttons">
        {this.state.inputTypes.map((inputType) => (
          <RoundButton
            inputType={inputType}
            key={inputType}
            onChange={this.props.onChange}
          />
        ))}
      </div>
    );
  }
}

export default RoundButtons;
