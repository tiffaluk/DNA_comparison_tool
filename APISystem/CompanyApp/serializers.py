from rest_framework import serializers
from CompanyApp.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=('CompanyId','CompanyName','Price_Per_BP','BP_Length_Minimum','BP_Length_Medium','BP_Length_Maximum','BP_Length_PriceIncrease','GC_Content_Minimum','GC_Content_Maximum','GC_Content_PriceIncrease','Homology_Min_Length_Minimum','Homology_Min_PriceIncrease','Double_Stranded_Price_Increase')
