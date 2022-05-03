import json
from decimal import Decimal
from Sequence import Sequence
class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)
#did not use
def BestCompany(Sequence,Companies):
    bestPrice = float('inf')
    bestCompany=""
    for company in Companies.iterator():

        if(Sequence.type=="AA"):
            if(company.AminoAcidSequence==True):
                currentPrice=PriceofCompany(Sequence,company)
        else:
            currentPrice=PriceofCompany(Sequence,company)
        if ((currentPrice<bestPrice) and (currentPrice>0)):
            bestPrice=currentPrice
            bestCompany=company.CompanyName
    value = {
        "CompanyName":bestCompany,
        "Price" : bestPrice
    }

    return json.dumps(value,cls=DecimalEncoder)

def AllCompany(Sequence,Companies):
    bestPrice = float('inf')
    bestCompany=""
    list=[]
    Sequence.get_gc_content()
    Sequence.get_folding_score()
    assembly_method, min_assembly_cost,turntime=Sequence.get_best_assembly_method()
    #create an object with the sequence length, gc content, folding score, best assembly, and turn time to be put in list
    test={
        "SequenceLength": len(Sequence.name),
        "GC_Content":Sequence.gc_content,
        "Folding_Score":Sequence.fold_score,
        "Best_Assembly":assembly_method,
        "Turn_time":turntime
    }
    list.append(test)
    #check the price of each company and add an object to list
    for company in Companies.iterator():
        overLengthThreshold=False
        overLengthMax=False
        overGC_Content=False
        overGC_Max=False
        overFoldingScore=False
        if(Sequence.type=="Amino Acids"):
            if(company.AminoAcidSequence==True):
                currentPrice,overLengthThreshold,overLengthMax,overGC_Max,overGC_Content,overFoldingScore=PriceofCompany(Sequence,company,overLengthThreshold,overLengthMax,overGC_Max,overGC_Content,overFoldingScore)
        else:
            currentPrice,overLengthThreshold,overLengthMax,overGC_Max,overGC_Content,overFoldingScoree=PriceofCompany(Sequence,company,overLengthThreshold,overLengthMax,overGC_Max,overGC_Content,overFoldingScore)

        #currentPrice=currentPrice+min_assembly_cost;
        #object to be added to list
        value = {
            "CompanyName":company.CompanyName,
            "Price" : currentPrice,
            "overLengthThreshold":overLengthThreshold,
            "overLengthMax":overLengthMax,
            "overGC_Content":overGC_Content,
            "overGC_Max":overGC_Max,
            "overFoldingScore":overFoldingScore
            }
        list.append(value)
        for x in range(len(Sequence.assembly_cost)):
            if(Sequence.assembly_cost[x]==float('inf')):
                Sequence.assembly_cost[x]=0.0
            if(Sequence.turn_time[x]==float('inf')):
                Sequence.turn_time[x]=0.0
    #create a customized object of all asssembly parts, cost, and time to be added to list
    parts={
        "BBParts": Sequence.bb_parts,
        "BBCost":  Sequence.assembly_cost[0],
        "BBtime": Sequence.turn_time[0],
        "GibsonParts": Sequence.gibson_parts,
        "GibsonCost":Sequence.assembly_cost[2],
        "Gibsontime":Sequence.turn_time[2],
        "GGParts": Sequence.gg_parts,
        "GGCosts":Sequence.assembly_cost[1],
        "GGtime":Sequence.turn_time[1]
        }
    list.append(parts)
    #return list as json file
    return json.dumps(list,cls=DecimalEncoder)

def PriceofCompany(Sequence,company,overLengthThreshold,overLengthMax,overGC_Max,overGC_Content,overFoldingScore):
    currentsequence=Sequence.name
    Sequence.get_gc_content()
    gc_content=Sequence.gc_content
    lengthofsequence=len(currentsequence)
    Sequence.get_folding_score()

    homology_score=Sequence.fold_score
    price=company.Price_Per_BP
    #check the length of sequence compare to the company requires
    if((lengthofsequence>company.BP_Length_Maximum) or (lengthofsequence<company.BP_Length_Minimum)):
        #if the sequence is over max or under min, then just return price=-1 as sequence can't be synthesize
        price=-1
        overLengthMax=True
        return price,overLengthThreshold,overLengthMax,overGC_Max,overGC_Content,overFoldingScore
    elif ((lengthofsequence>company.BP_Length_Threshold) and (lengthofsequence<company.BP_Length_Maximum)):
        #if the sequence is over threshold but under max, then add price to orignal base pair price
        overLengthThreshold=True
        price=price+company.BP_Length_PriceIncrease
    if(gc_content>company.GC_Content_Maximum):
        #if sequence gc content is over the maximum, then return -1 as unable to synthesize
        price=-1
        overGC_Max=True
        return price,overLengthThreshold,overLengthMax,overGC_Max,overGC_Content,overFoldingScore
    elif ((gc_content>company.GC_Content_Threshold) and (gc_content<company.GC_Content_Maximum)):
        #if sequence gc content is over threshold but undermax, add price to oringal price
        overGC_Content=True
        price=price+company.GC_Content_PriceIncrease
    if(homology_score>company.Homology_Threshold):
        # if fold score is over threshold, add price to original price
        overFoldingScore=True
        price=price+company.Homology_PriceIncrease
    if(Sequence.type=="dsDNA"):
        #if type is dsdna, then add price
        price=price+company.Double_Stranded_Price_Increase
    price=price*lengthofsequence
    return price,overLengthThreshold,overLengthMax,overGC_Max,overGC_Content,overFoldingScore
