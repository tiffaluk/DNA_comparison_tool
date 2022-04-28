import React, { Component } from "react";
import CompanyCards from "../components/companyCards";
import CompanyCard from "../components/companyCard";

import { HomeButton, MoreButton } from "../components/iconButton";

class CompanyScreen extends Component {
  state = {};
  render() {
    return (
      <div className="company-screen">
        <HomeButton />
        <h1 className="title">Company Screen</h1>
        <CompanyCards />
        {/* <CompanyCard /> */}
      </div>
    );
  }
}

export default CompanyScreen;
