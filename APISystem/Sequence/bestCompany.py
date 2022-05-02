import json
from decimal import Decimal
from Sequence import Sequence
class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)
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
    assembly_method, min_assembly_cost=Sequence.get_best_assembly_method()
    print(Sequence.name)
    test={
        "SequenceLength": len(Sequence.name),
        "GC_Content":Sequence.gc_content,
        "Folding_Score":Sequence.fold_score,
        "Best_Assembly":assembly_method
    }
    list.append(test)
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
        print(currentPrice);
        #currentPrice=currentPrice+min_assembly_cost;
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


    return json.dumps(list,cls=DecimalEncoder)

def PriceofCompany(Sequence,company,overLengthThreshold,overLengthMax,overGC_Max,overGC_Content,overFoldingScore):
    currentsequence=Sequence.name
    Sequence.get_gc_content()
    gc_content=Sequence.gc_content
    lengthofsequence=len(currentsequence)
    Sequence.get_folding_score()

    homology_score=Sequence.fold_score
    price=company.Price_Per_BP
    if((lengthofsequence>company.BP_Length_Maximum) or (lengthofsequence<company.BP_Length_Minimum)):
        price=-1
        overLengthMax=True
        return price,overLengthThreshold,overLengthMax,overGC_Max,overGC_Content,overFoldingScore
    elif ((lengthofsequence>company.BP_Length_Threshold) and (lengthofsequence<company.BP_Length_Maximum)):
        overLengthThreshold=True
        price=price+company.BP_Length_PriceIncrease
    if(gc_content>company.GC_Content_Maximum):
        price=-1
        overGC_Max=True
        return price,overLengthThreshold,overLengthMax,overGC_Max,overGC_Content,overFoldingScore
    elif ((gc_content>company.GC_Content_Threshold) and (gc_content<company.GC_Content_Maximum)):
        overGC_Content=True
        price=price+company.GC_Content_PriceIncrease
    if(homology_score>company.Homology_Threshold):
        overFoldingScore=True
        price=price+company.Homology_PriceIncrease
    if(Sequence.type=="dsDNA"):
        price=price+company.Double_Stranded_Price_Increase
    price=price*lengthofsequence
    return price,overLengthThreshold,overLengthMax,overGC_Max,overGC_Content,overFoldingScore
