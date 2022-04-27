from django.db import models

# Create your models here.
class Company(models.Model):
    CompanyId= models.AutoField(primary_key=True)
    CompanyName=models.CharField(max_length=500)
    Price_Per_BP=models.FloatField()
    BP_Length_Minimum=models.BigIntegerField()
    BP_Length_Threshold=models.BigIntegerField()
    BP_Length_Maximum=models.BigIntegerField()
    BP_Length_PriceIncrease=models.FloatField()
    GC_Content_Threshold=models.FloatField()
    GC_Content_Maximum=models.FloatField()
    GC_Content_PriceIncrease=models.FloatField()
    Homology_Threshold=models.BigIntegerField()
    Homology_PriceIncrease=models.FloatField()
    Double_Stranded_Price_Increase=models.FloatField()
    AminoAcidSequence=models.BooleanField()
class User(models.Model):
    CompanyName=models.CharField(max_length=500)
    Price=models.FloatField()
