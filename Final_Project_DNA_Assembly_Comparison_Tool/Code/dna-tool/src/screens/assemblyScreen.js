import React, { Component } from "react";
import AssemblyCards from "../components/assemblyCards";
import AssemblyCard from "../components/assemblyCard";

import { HomeButton, MoreButton } from "../components/iconButton";

class AssemblyScreen extends Component {
  state = {};
  render() {
    return (
      <div className="assembly-screen">
        <HomeButton />
        <h1 className="title">Assembly Screen</h1>
        <AssemblyCards />
      </div>
    );
  }
}

export default AssemblyScreen;
