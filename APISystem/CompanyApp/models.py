from django.db import models

# Create your models here.
class Company(models.Model):
    CompanyId= models.AutoField(primary_key=True)
    CompanyName=models.CharField(max_length=500)
    Price_Per_BP=models.DecimalField(max_digits=5, decimal_places=3)
    BP_Length_Minimum=models.BigIntegerField()
    BP_Length_Threshold=models.BigIntegerField()
    BP_Length_Maximum=models.BigIntegerField()
    BP_Length_PriceIncrease=models.DecimalField(max_digits=5, decimal_places=3)
    GC_Content_Threshold=models.DecimalField(max_digits=4, decimal_places=3)
    GC_Content_Maximum=models.DecimalField(max_digits=4, decimal_places=3)
    GC_Content_PriceIncrease=models.DecimalField(max_digits=5, decimal_places=3)
    Homology_Threshold=models.BigIntegerField()
    Homology_PriceIncrease=models.DecimalField(max_digits=5, decimal_places=3)
    Double_Stranded_Price_Increase=models.DecimalField(max_digits=5, decimal_places=3)
    AminoAcidSequence=models.BooleanField()
class User(models.Model):
    CompanyName=models.CharField(max_length=500)
    Price=models.DecimalField(max_digits=15, decimal_places=3)
