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
          <h3>{"Price: $" + this.props.users.Price.toFixed(2)}{" || Sequence Length: " + this.props.users.length}</h3>
          <h3>{"Turnaround time (Days): " + this.props.users.turntime}{" || Sequence G-C Content: " + this.props.users.gc.toFixed(3)}</h3>
          <h3>{"Assembly method: " + this.props.users.AssemblyMethod} {" || Sequence Fold Score: " + this.props.users.foldscore.toFixed(3)}</h3>

        </div>
      </div>
    );
  }
}

export default ResultsBox;
