import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import LoginBg from "./components/loginBackground";
import LoginButton from "./components/loginButton";
import LoginButtons from "./components/loginButtons";
import LoginScreen from "./screens/loginScreen";
import SequenceInput from "./components/sequenceInput";
import OrderScreen from "./screens/orderScreen";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
    {/* <LoginScreen /> */}
    {/* <OrderScreen /> */}
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
