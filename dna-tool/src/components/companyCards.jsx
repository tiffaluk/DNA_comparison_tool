import React, { Component } from "react";
import CompanyCard from "./companyCard";
import OrderScreen from "../screens/orderScreen"
class CompanyCards extends Component {
  constructor(props){
    super(props);
    this.state = {
      users: [],
      DataisLoaded:true,
      users2:[],
      DataisLoaded2:true,
      companies: [
        {
          name: "A",
          price: "1",
          time: "1",
          assembly: "m1",
          pricebp: "1",
          costpenalty: "1",
          sequencelength:"0",
          lengthpriceincrease:"0",
          gccontent: "0",
          gcpriceincrease:"0",
          foldingscore:"0",
          foldingpriceincrease:"0",
          aminoacid:"0",

        },
        {
          name: "B",
          price: "2",
          time: "2",
          assembly: "m2",
          pricebp: "2",
          costpenalty: "2",
          sequencelength:"0",
          lengthpriceincrease:"0",
          gccontent: "0",
          gcpriceincrease:"0",
          foldingscore:"0",
          foldingpriceincrease:"0",
          aminoacid:"0",
        },
        {
          name: "C",
          price: "3",
          time: "3",
          assembly: "m3",
          pricebp: "3",
          costpenalty: "3",
          sequencelength:"0",
          lengthpriceincrease:"0",
          gccontent: "0",
          gcpriceincrease:"0",
          foldingscore:"0",
          foldingpriceincrease:"0",
          aminoacid:"0",
        },
        {
          name: "D",
          price: "4",
          time: "4",
          assembly: "m4",
          pricebp: "4",
          costpenalty: "4",
          sequencelength:"0",
          lengthpriceincrease:"0",
          gccontent: "0",
          gcpriceincrease:"0",
          foldingscore:"0",
          foldingpriceincrease:"0",
          aminoacid:"0",
       },
       ],
     }
  }


  componentDidMount(props) {

      var head = { "Content-Type": "application/json" };
        fetch(
           "http://localhost:8000/company")
            .then((res) => res.json())
            .then((json) => {
                this.setState({
                    users: json,
                    DataisLoaded: true
                });

                var c=JSON.parse(localStorage.getItem("prices"));
                console.log(c);
                for (let step = 0; step < 4; step++) {
                  this.state.companies[step].assembly=c[0].Best_Assembly;
                  this.state.companies[step].time=c[0].Turn_time;
                  this.state.companies[step].pricebp=this.state.users[step].Price_Per_BP;
                  var bestPrice=Math.pow(10, 1000); //
                  var bestCompanyName="";
                  for (let step2 = 0; step2 < 4; step2++) {
                    if(c[step2].Price<bestPrice){
                      if(c[step2].Price>0){
                        bestPrice=c[step2].Price;
                        bestCompanyName=c[step2].CompanyName;
                      }
                    }
                  }
                  if(this.state.users[step].CompanyName==bestCompanyName){
                    this.state.companies[step].name=this.state.users[step].CompanyName + " (Best)";
                  }
                  else{
                    this.state.companies[step].name=this.state.users[step].CompanyName;
                  }
                  var index=0;
                  for( let i =1;i<5; i++){
                    if(this.state.users[step].CompanyName==c[i].CompanyName){
                      index=i;
                    }
                  }
                  if(c[index].Price==-1){
                      this.state.companies[step].price="Cant be synthesized"
                      this.state.companies[step].costpenalty="Can't be synthesized"
                  }
                  else{
                      this.state.companies[step].price=c[index].Price;
                      this.state.companies[step].costpenalty=(c[index].Price/c[0].SequenceLength)-this.state.users[step].Price_Per_BP
                  }
                  this.state.companies[step].sequencelength=this.state.users[step].BP_Length_Minimum + "-"+this.state.users[step].BP_Length_Threshold+"-"+this.state.users[step].BP_Length_Maximum
                  this.state.companies[step].gccontent=this.state.users[step].GC_Content_Threshold+ "-"+this.state.users[step].GC_Content_Maximum
                  this.state.companies[step].foldingscore=this.state.users[step].Homology_Threshold
                  this.state.companies[step].aminoacid=this.state.users[step].AminoAcidSequence
                  if(c[index].overLengthMax==true){
                    this.state.companies[step].lengthpriceincrease="Length too long/short"
                  }
                  else if (c[index].overLengthThreshold==true){
                    this.state.companies[step].lengthpriceincrease=this.state.users[step].BP_Length_PrinceIncrease
                  }
                  else{
                    this.state.companies[step].lengthpriceincrease=0;
                  }
                  if(c[index].overGC_Max==true){
                    this.state.companies[step].gcpriceincrease="Too much G-C BP"
                  }
                  else if (c[index].overGC_Content==true){
                    this.state.companies[step].gcpriceincrease=this.state.users[step].GC_Content_PriceIncrease
                  }
                  else{
                    this.state.companies[step].gcprinceincrease=0;
                  }
                  if(c[index].overFoldingScore==true){
                    this.state.companies[step].foldingpriceincrease=this.state.users[step].Homology_PriceIncrease
                  }


                }


            })



    }
  render() {
    return (
      <div className="company-cards">

      {this.state.companies.map((company) => (
        <CompanyCard company={company} key={company.name} />
      ))}
      </div>
    );
  }
}

export default CompanyCards;
