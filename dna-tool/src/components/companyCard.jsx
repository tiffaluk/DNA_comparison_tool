import React, { Component } from "react";
import "./companydetailsview.css";

class CompanyCard extends Component {
  state = {
    name: this.props.company.name,
    price: this.props.company.price,
    time: this.props.company.time,
    assembly: this.props.company.assembly,
    pricebp: this.props.company.pricebp,
    costpenalty: this.props.company.costpenalty,
  };
  render() {
    return (
      <div className="center">
        <div className="card">
          <div className="additional">
            <div className="user-card">
              <svg
                width="110"
                height="110"
                viewBox="0 0 250 250"
                xmlns="http://www.w3.org/2000/svg"
                role="img"
                aria-labelledby="title desc"
                className="center"
              >
                <defs>
                  <clipPath id="scene">
                    <circle cx="125" cy="125" r="115" />
                  </clipPath>
                </defs>
                <circle cx="125" cy="125" r="120" fill="rgba(0,0,0,0.15)" />
                <g stroke="none" stroke-width="0" clip-path="url(#scene)">
                  <rect x="0" y="0" width="250" height="250" fill="#b0d2e5" />
                </g>
              </svg>
            </div>
            <div className="more-info">
              <h1 id="name"></h1>
              <div className="coords">
                <span>
                  {"Price/bp: " + this.state.pricebp}
                  <label id="priceBp"></label>
                </span>
              </div>
              <div className="coords">
                <span>
                  {"Cost Penalties: " + this.state.costpenalty}
                  <label id="costPenalty"></label>
                </span>
              </div>
            </div>
          </div>
          <div className="general">
            <h1 id="name2"></h1>
            <p id="timeSignIn"></p>
            <p id="timeCheckedIn"> </p>
            <p>
              {"Company Name: " + this.state.name}
              <label id="companyName"></label>
            </p>
            <p>
              {"Price: " + this.state.price}
              <label id="price"></label>
            </p>
            <p>
              {"Turn Around Time: " + this.state.time}
              <label id="turnaroundTime"></label>
            </p>
            <p>
              {"Assembly Method: " + this.state.assembly}
              <label id="assemblyMethod"></label>
            </p>
            <span className="more">Hover over card for more info</span>
          </div>
        </div>
      </div>
    );
  }
}

export default CompanyCard;
