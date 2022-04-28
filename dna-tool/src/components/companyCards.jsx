import React, { Component } from "react";
import CompanyCard from "./companyCard";

class CompanyCards extends Component {
  state = {
    companies: [
      {
        name: "A",
        price: "1",
        time: "1",
        assembly: "m1",
        pricebp: "1",
        costpenalty: "-1",
      },
      {
        name: "B",
        price: "2",
        time: "2",
        assembly: "m2",
        pricebp: "2",
        costpenalty: "-2",
      },
      {
        name: "C",
        price: "3",
        time: "3",
        assembly: "m3",
        pricebp: "3",
        costpenalty: "-3",
      },
      {
        name: "D",
        price: "4",
        time: "4",
        assembly: "m4",
        pricebp: "4",
        costpenalty: "-4",
      },
    ],
  };
  render() {
    return (
      <div className="company-cards">
        {this.state.companies.map((company) => (
          <CompanyCard company={company} key={company.name} />
        ))}
      </div>
    );
  }
}

export default CompanyCards;
