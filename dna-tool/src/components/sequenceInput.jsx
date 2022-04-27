import React, { Component } from "react";
import "./userview.css";

class SequenceInput extends Component {
  state = {
    seq: "",
  };

  handleChange = (seq) => {
    this.setState({ seq }, this.props.onChange(seq));
  };

  render() {
    return (
      <div className="seq-input">
        <input
          type="text"
          required
          value={this.state.seq}
          className="input-box"
          onChange={(e) => this.handleChange(e.target.value)}
        ></input>
      </div>
    );
  }
}

export default SequenceInput;
