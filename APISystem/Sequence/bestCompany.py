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

        if(Sequence.type=="Amino Acids"):
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



def PriceofCompany(Sequence,company):
    print(company.CompanyName)
    currentsequence=Sequence.name
    Sequence.get_gc_content()
    gc_content=Sequence.gc_content
    lengthofsequence=len(currentsequence)
    Sequence.get_folding_score()

    homology_score=Sequence.fold_score
    price=company.Price_Per_BP
    if((lengthofsequence>company.BP_Length_Maximum) or (lengthofsequence<company.BP_Length_Minimum)):
        return -1
    elif ((lengthofsequence>company.BP_Length_Threshold) and (lengthofsequence<company.BP_Length_Maximum)):
        #print('hit bp')
        price=price+company.BP_Length_PriceIncrease
    if(gc_content>company.GC_Content_Maximum):
        return -1
    elif ((gc_content>company.GC_Content_Threshold) and (gc_content<company.GC_Content_Maximum)):
        #print('hitgc')
        price=price+company.GC_Content_PriceIncrease
    if(homology_score>company.Homology_Threshold):
        #print('hit homo')
        price=price+company.Homology_PriceIncrease
    if(Sequence.type=="dsDNA"):
        #print('hitdna')
        price=price+company.Double_Stranded_Price_Increase
    print(price)
    price=price*lengthofsequence
    return price
