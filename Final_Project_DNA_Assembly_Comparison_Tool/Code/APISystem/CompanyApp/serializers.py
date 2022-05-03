from rest_framework import serializers
from CompanyApp.models import Company,User

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=('CompanyId','CompanyName','Price_Per_BP','BP_Length_Minimum','BP_Length_Threshold','BP_Length_Maximum','BP_Length_PriceIncrease','GC_Content_Threshold','GC_Content_Maximum','GC_Content_PriceIncrease','Homology_Threshold','Homology_PriceIncrease','Double_Stranded_Price_Increase','AminoAcidSequence')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('CompanyName','Price')
