import React, { useEffect, useState, Component } from "react";
import { useNavigate } from "react-router-dom";


async function renderCompanies(users) {
  {
    console.log(users.CompanyName);
    console.log(users.Price);
  }
}

function Button() {
  //   state = {};
  //   render() {
  var data = JSON.stringify({
    "Sequence":"atgctcccaaacgatgaatggctccgtgataaccagccgtaaacttctctggaagcttcacattggagattggcaatcacggtctcattatttctctcacatgcgaaagttcatgtctactaacagttcttctaactcaagacaaacgatgtattacagactgacaggaggatgagctacagcttgactcgaaaatagctagccacccaccgacatatctgatacgccgcgtatcaaacgtctcgtgaggcggcacgcactgaatgtattgggtggagttattacatctagtatggggtgggcctagtccttaagcactacatcagttaggcggctttacgggggaaccccgatcctcccttgtaggaactcagcatctcggcgcagggtggtcaggtatcttcctgtacgggcaggactttgtattcgtaccaacgaccgtttgtattactgtctattggcctgagggcccgcactcgcctcttgctgcgttgggggatgcaacggtggccggccgactataatcagccgcggaatccgattcgagagagataaaatggtggcgcttaccgcttccttaggccctgttggcgatggagggacagtacaagatgtaccggataattggccatgtactacacggcaacgtatatatgtaaagccagtgggatagcacgcccgtcctattcaactaccgaaattaaaatagatgctcgtcctaaaaatgggaatgacacggggaatgccgaacatcattgcgtccaggtcgcggcgtcgcaaccgagactctgctgtttgaaacgagtaagcgcgctattatacgtgccaattttcgcttttggtatccgcttttgaggcccgcctggatacgctaacctggcctggaggtagggtataaactccggagaatgtgggtgtcgatcattaggaatctccaatcttgtaacaatgaccccccagacgtcgatatactttgacagcgcttcgagtattagtaacc",
    "Type":"DNA",
    "dsDNA":"Yes"
});
  var head = { "Content-Type" : "application/json" };
  let navigate = useNavigate();
  const [users, setUsers] = useState();
  const getApiData = async () => {
    const response = await fetch("http://localhost:8000/company", { method: "POST", headers: head, body: data }).then(
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
