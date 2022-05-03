import React, { Component } from "react";
import SequenceInput from "../components/sequenceInput";
import Button from "../components/button";
import RoundButtons from "../components/roundButtons";
import ResultsBox from "../components/resultsBox";
import {
  HomeButton,
  MoreButton,
  AssemblyButton,
} from "../components/iconButton";
import CompanyCards from "../components/companyCards";

class OrderScreen extends Component {
  state = {
    inSeq: "",
    inType: "",
    v: "result-container-hidden",
    // v2: "more-button-hidden",
    users: {
      CompanyName: "",
      Price: 0.0,
      AssemblyMethod:" ",
      turntime:"",
      length:0.0,
      gc:0.0,
      foldscore:0.0
    },
  };

  handleSubmit = (users) => {
    const v = "result-container-visible";
    // const v2 = "more-button";
    this.setState({ v, users });

    console.log("Handled submit");
  };

  handleSeqChange = (inSeq) => {
    this.setState({ inSeq });
  };

  handleTypeChange = (inType) => {
    this.setState({ inType });
  };

  render() {
    return (
      <div className="order-screen">
        <HomeButton />
        <h1 className="input-title">Please Input Sequence</h1>
        <SequenceInput onChange={this.handleSeqChange} />
        <RoundButtons onChange={this.handleTypeChange} />
        <Button
          inSeq={this.state.inSeq}
          inType={this.state.inType}
          onSubmit={this.handleSubmit}
        />
        <ResultsBox visibility={this.state.v} users={this.state.users} />
        <div className="icon-buttons">
          <MoreButton />
          <AssemblyButton />
        </div>
      </div>
    );
  }
}

export default OrderScreen;
