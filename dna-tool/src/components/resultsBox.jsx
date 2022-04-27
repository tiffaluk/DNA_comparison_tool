import React, { Component } from "react";

class ResultsBox extends Component {
  state = {};
  render() {
    return (
      <div className="results-box">
        <h3 id="CompanyName">Company:</h3>
        <h3>Price:</h3>
        <h3>Turnaround time:</h3>
        <h3>Assembly method:</h3>
      </div>
    );
  }
}

export default ResultsBox;
