import React, { Component } from "react";
import SequenceInput from "../components/sequenceInput";
import Button from "../components/button";
import RoundButtons from "../components/roundButtons";
import ResultsBox from "../components/resultsBox";

class OrderScreen extends Component {
  state = {};
  render() {
    return (
      <div className="order-screen">
        <h1 className="input-title">Please Input Sequence</h1>
        <SequenceInput />
        <RoundButtons />
        <Button />
        {/* <h1 className="output-title">Our Recommendation!</h1>
        <ResultsBox /> */}
      </div>
    );
  }
}

export default OrderScreen;
