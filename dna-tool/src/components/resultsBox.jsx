import React, { Component } from "react";

class ResultsBox extends Component {
  state = {};
  render() {
    return (
      <div className={this.props.visibility}>
        <h1 className="output-title">Our Recommendation!</h1>
        <div className="results-box">
          <h3 id="CompanyName">{"Company: " + this.props.users.CompanyName}</h3>
          <h3>{"Price:$ " + this.props.users.Price}</h3>
          <h3>Turnaround time:</h3>
          <h3>Assembly method:</h3>
        </div>
      </div>
    );
  }
}

export default ResultsBox;
