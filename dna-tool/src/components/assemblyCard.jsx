import React, { Component } from "react";
import "./companydetailsview.css";
import { IoBusiness } from "react-icons/io5";
import "./assemblydetailsview.css";

class AssemblyCard extends Component {
  state = {
    name: this.props.assembly.name,
    turnaroundtime: this.props.assembly.time,
    extracost: this.props.assembly.extracost,
    parts: this.props.parts,
  };

  render() {
    return (
      <div className="center">
        <div className="assembly-card">
          <div className="additional">
            {/* <i>
              <IoBusiness size="5em" />
            </i> */}
            <div className="user-card">
              {/* <svg
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
                    <circle cx="130" cy="125" r="115" />
                  </clipPath>
                </defs>
                <circle cx="130" cy="125" r="120" fill="rgba(0,0,0,0)" />
                <g stroke="none" strokeWidth="0" clipPath="url(#scene)">
                  <rect x="0" y="0" width="250" height="250" fill="#b0d2e5" />
                </g>
              </svg> */}
            </div>
            <div className="more-info">
              <h1></h1>
              <div className="coords">
                <span>
                  {"Parts: " + this.state.parts}
                  <label id="parts"></label>
                </span>
              </div>
            </div>
          </div>
          <div className="general">
            <p>
              {"Assembly Method: " + this.state.name}
              <label id="assemblyMethod"></label>
            </p>
            <p>
              {"Turn Around Time: " + this.state.time}
              <label id="turnaroundTime"></label>
            </p>
            <p>
              {"Extra Cost($USD): " + this.state.extracost}
              <label id="extraCost"></label>
            </p>
            <span className="more">Hover over card for more info</span>
          </div>
        </div>
      </div>
    );
  }
}

export default AssemblyCard;
