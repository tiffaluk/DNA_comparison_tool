import React, { useEffect, useState, Component } from "react";
import { useNavigate } from "react-router-dom";

function renderSequence(sequence,type) {
  {
    if(type=="Amino Acids"){
      sequence=convertAA(sequence);
    }
    console.log(sequence);
     sequence=sequence.toUpperCase();
     for( let i=0;i<sequence.length;i++){
        if ((sequence[i] !="G") &&(sequence[i] !="A") &&(sequence[i] !="T") &&(sequence[i] !="C") && (sequence[i]!="U")) {

            return false;
        }
     }
     return true;
  }
}
function convertAA(sequence){
  sequence=sequence.toUpperCase();
  var newsequence="";
  for(let i=0;i<sequence.length;i++){
    if(sequence[i]=="A"){
      newsequence=newsequence+"GCA";
    }
    else if (sequence[i]=="C"){
      newsequence=newsequence+"TGC";
    }
    else if (sequence[i]=="D"){
      newsequence=newsequence+"GAC";
    }
    else if (sequence[i]=="E"){
      newsequence=newsequence+"GAA";
    }
    else if (sequence[i]=="F"){
      newsequence=newsequence+"TTC";
    }
    else if (sequence[i]=="G"){
      newsequence=newsequence+"GGA";
    }
    else if (sequence[i]=="H"){
      newsequence=newsequence+"CAC";
    }
    else if (sequence[i]=="I"){
      newsequence=newsequence+"ATA";
    }
    else if (sequence[i]=="K"){
      newsequence=newsequence+"AAA";
    }
    else if (sequence[i]=="L"){
      newsequence=newsequence+"CTA";
    }
    else if (sequence[i]=="M"){
      newsequence=newsequence+"ATG";
    }
    else if (sequence[i]=="N"){
      newsequence=newsequence+"AAC";
    }
    else if (sequence[i]=="P"){
      newsequence=newsequence+"CCA";
    }
    else if (sequence[i]=="Q"){
      newsequence=newsequence+"CAA";
    }
    else if (sequence[i]=="R"){
      newsequence=newsequence+"AGA";
    }
    else if (sequence[i]=="S"){
      newsequence=newsequence+"AGC";
    }
    else if (sequence[i]=="T"){
      newsequence=newsequence+"ACA";
    }
    else if (sequence[i]=="V"){
      newsequence=newsequence+"GTA";
    }
    else if (sequence[i]=="W"){
      newsequence=newsequence+"TGG";
    }
    else if (sequence[i]=="Y"){
      newsequence=newsequence+"TAC";
    }
    else if (sequence[i]=="-"){
      newsequence=newsequence+"TAA";
    }

  }
  return newsequence;
}
function convertRNA(sequence){
  sequence=sequence.toUpperCase();
  var newsequence="";
  for( let i=0;i<sequence.length;i++){
    if(sequence[i]=="U"){
      newsequence=newsequence+"T"
    }
    else{
      newsequence=newsequence+sequence[i]
    }
  }
  return newsequence;
}

function Button(props) {
  //   state = {};
  //   render() {
  const falseSequence = async () => {
     var a={
       CompanyName: "Input has Error! Please Resubmit!",
       Price: 0,
       AssemblyMethod:" "
    }
    props.onSubmit(a);
  };
  var data="";
  let navigate = useNavigate();
  if(props.inType=="RNA"){
    var newsequence=convertRNA(props.inSeq);
    var data = JSON.stringify({
         Sequence: newsequence,
         Type: props.inType,

       });

  }
  else if(props.inType=="Amino Acids"){
    var newsequence=convertAA(props.inSeq);
    var data = JSON.stringify({
         Sequence: newsequence,
         Type: "ssDNA",

       });
  }
  else{
    var data = JSON.stringify({
         Sequence: props.inSeq,
         Type: props.inType,
       });
  }

     var head = { "Content-Type": "application/json" };

     const getApiData = async () => {
       const response = await fetch("http://localhost:8000/company", {
         method: "DELETE",
         headers: head,
         body: data,
       });
       const d = await response.json();
       const bestIndex=0;
       var bestPrice=Math.pow(10, 1000); //
       var a=d[0];
       for (let step = 0; step < 4; step++) {
         if(d[step].Price<bestPrice){
           if(d[step].Price>0){
             bestPrice=d[step].Price;
             a=d[step];
           }
         }
       }
       a={
         ...a,
         "AssemblyMethod":d[0].Best_Assembly,
         "turntime":d[0].Turn_time
       }

       localStorage.setItem("prices",JSON.stringify(d));
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

          if(renderSequence(props.inSeq,props.inType)==false){
            falseSequence();
          }
          else{
            getApiData();
          }
        }}
      >
        Submit
      </button>
    </div>
  );
  //   }
}

export default Button;
