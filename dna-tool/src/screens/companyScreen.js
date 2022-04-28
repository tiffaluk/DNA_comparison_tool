import React, { Component } from "react";
import CompanyCard from "../components/companyCard";

class CompanyScreen extends Component {
  state = {};
  render() {
    return (
      <div className="company-screen">
        <h1>Company Screen</h1>
        <CompanyCard />
      </div>
    );
  }
}

export default CompanyScreen;
