import logo from "./logo.svg";
import "./App.css";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginScreen from "./screens/loginScreen";
import OrderScreen from "./screens/orderScreen";
import CompanyScreen from "./screens/companyScreen";

function App() {
  return (
    // <div className="App">
    //   <header className="App-header">
    //     <img src={logo} className="App-logo" alt="logo" />
    //     <p>
    //       Edit <code>src/App.js</code> and save to reload.
    //     </p>
    //     <a
    //       className="App-link"
    //       href="https://reactjs.org"
    //       target="_blank"
    //       rel="noopener noreferrer"
    //     >
    //       Learn React
    //     </a>
    //   </header>
    // </div>

    <Router>
      <Routes>
        <Route exact path="/" element={<LoginScreen />} />
        <Route exact path="/order" element={<OrderScreen />} />
        <Route exact path="/company" element={<CompanyScreen />} />
      </Routes>
    </Router>
  );
}

export default App;
