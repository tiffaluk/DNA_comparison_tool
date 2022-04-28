import React, { Component } from "react";
import { FaHome } from "react-icons/fa";
import { MdReadMore } from "react-icons/md";
import { useNavigate } from "react-router-dom";
import "./userview.css";

export function HomeButton() {
  //   state = {
  //     icon: <FaHome size="3em" />,
  //   };
  let navigate = useNavigate();
  //   render() {
  return (
    <div className="home-button-container">
      <button
        type="submit"
        className="home-button"
        onClick={() => {
          navigate("/");
        }}
      >
        <i>
          <FaHome size="3em" />
        </i>
      </button>
    </div>
  );
  //   }
}

export function MoreButton() {
  let navigate = useNavigate();

  return (
    <div className="more-button-container-visible">
      <button
        type="submit"
        className="more-button"
        onClick={() => {
          navigate("/company");
        }}
      >
        <label>Company Details</label>
        <i>
          <MdReadMore size="3em" />
        </i>
      </button>
    </div>
  );
}
