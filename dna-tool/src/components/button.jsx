import React, { useEffect, useState, Component } from "react";
import { useNavigate } from "react-router-dom";

async function renderCompanies(users) {
  {
    console.log(users.CompanyName);
    console.log(users.Price);
  }
}

function Button(props) {
  //   state = {};
  //   render() {

  let navigate = useNavigate();

  var data = JSON.stringify({
    Sequence: props.inSeq,
    Type: props.inType,
    // "dsDNA":"Yes"
  });
  var head = { "Content-Type": "application/json" };

  const getApiData = async () => {
    const response = await fetch("http://localhost:8000/company", {
      method: "DELETE",
      headers: head,
      body: data,
    });
    const d = await response.json();
    const bestIndex=0;
    const bestPrice=Math.pow(10, 1000); //
    var a=d[0];
    for (let step = 0; step < 4; step++) {
      if(d[step].Price<bestPrice){
        if(d[step].Price>0){
          a=d[step];
        }
      }
    }
    localStorage.setItem("prices",JSON.stringify(d));
    console.log(d)
    props.onSubmit(a);
  };

  // useEffect(() => {
  //   getApiData();
  // }, []);
  return (

    <div className="submit-button">
      <button
        type="submit"
        className="submitButton"
        onClick={() => {
          getApiData();
        }}
      >
        Submit
      </button>
    </div>
  );
  //   }
}

export default Button;
