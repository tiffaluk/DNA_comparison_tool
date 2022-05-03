import React, { Component } from "react";
import AssemblyCard from "./assemblyCard";
import "./assemblydetailsview.css";

class AssemblyCards extends Component {
  state = {
    assemblies: [
      {
        name: "A",
        time: "1",
        extracost: "1",
        parts: "1",
      },
      {
        name: "B",
        time: "1",
        extracost: "1",
        parts: "1",
      },
      {
        name: "C",
        time: "1",
        extracost: "1",
        parts: "1",
      },
    ],
  };
  render() {
    return (
      <div className="assembly-cards">
        {this.state.assemblies.map((assembly) => (
          <AssemblyCard assembly={assembly} key={assembly.name} />
        ))}
      </div>
    );
  }
}

export default AssemblyCards;
