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

  const [users, setUsers] = useState();
  const getApiData = async () => {
    const response = await fetch("http://localhost:8000/company", {
      method: "POST",
      headers: head,
      body: data,
    }).then((response) => response.json());
    setUsers(response);
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
          props.onSubmit();
          console.log("submitted");
          // navigate("/result");
          // renderCompanies(users);
        }}
      >
        Submit
      </button>
    </div>
  );
  //   }
}

export default Button;
