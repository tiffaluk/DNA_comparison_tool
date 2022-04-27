import React, { useEffect, useState, Component } from "react";
import { useNavigate } from "react-router-dom";

async function getCompanies() {
  let url = "http://localhost:8000/company";
  try {
    let res = await fetch(url);
    return await res.json();
  } catch (error) {
    console.log(error);
  }
}

async function renderCompanies(users) {
  {
    users && users.map((user) => console.log(user.CompanyName));
  }
}

function Button() {
  //   state = {};
  //   render() {
  let navigate = useNavigate();
  const [users, setUsers] = useState();
  const getApiData = async () => {
    const response = await fetch("http://localhost:8000/company").then(
      (response) => response.json()
    );
    setUsers(response);
  };

  useEffect(() => {
    getApiData();
  }, []);
  return (
    <div className="submit-button">
      <button
        type="submit"
        className="submitButton"
        onClick={() => {
          navigate("/result");
          renderCompanies(users);
        }}
      >
        Submit
      </button>
    </div>
  );
  //   }
}

export default Button;
