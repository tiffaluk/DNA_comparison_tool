import React, { Component } from "react";
import AssemblyCard from "./assemblyCard";
import "./assemblydetailsview.css";
function convertArray(sequence){
  if(typeof sequence === 'string'){
      return sequence;
  }
  else{
    var newsentence="";
    var partnumber="";
    for(let i=0;i<sequence.length;i++){

      newsentence=newsentence+sequence[i];
      newsentence=newsentence+"  ";
    }
    return newsentence;
  }
}
class AssemblyCards extends Component {
  constructor(props){
    super(props);
    this.state = {
      assemblies: [
      {
        name: "BiobRick",
        time: 2,
        extracost: "1",
        parts: "1",
      },
      {
        name: "",
        time: 2,
        extracost: "1",
        parts: "1",
      },
    ],
  }
}


componentDidMount(props) {
    var c=JSON.parse(localStorage.getItem("prices"));
    var d=c[4];
    var test=[
    {
      name: "BioBricks",
      time:d.BBtime ,
      extracost: d.BBCost,
      parts: convertArray(d.BBParts),
    },
    {
      name: "Gibson",
      time: d.Gibsontime,
      extracost: d.GibsonCost,
      parts: convertArray(d.GibsonParts),
    },
    {
      name: "Golden Gate",
      time: d.GGtime,
      extracost: d.GGCosts,
      parts:convertArray(d.GGParts),
    },
  ]
    this.setState({assemblies:test})




  }
  render() {
    return (
      <div className="assembly-cards">
        {this.state.assemblies.map((assembly) => (
          <AssemblyCard assembly={assembly} key={assembly.name} />
        ))}
      </div>
    );
  }
}

export default AssemblyCards;
