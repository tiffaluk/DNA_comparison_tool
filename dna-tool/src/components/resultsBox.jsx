import React, { Component } from "react";

class ResultsBox extends Component {
  state = {

  };

  render() {
    return (
      <div className={this.props.visibility}>
        <h1 className="output-title">Our Recommendation!</h1>
        <div className="results-box">
          <h3 id="CompanyName">{"Company: " + this.props.users.CompanyName}</h3>
          <h3>{"Price:$ " + this.props.users.Price.toFixed(2)}</h3>
          <h3>{"Turnaround time (Days):" + this.props.users.turntime}</h3>
          <h3>{"Assembly method: " + this.props.users.AssemblyMethod}</h3>
        </div>
      </div>
    );
  }
}

export default ResultsBox;
