from django.db import models

# Create your models here.
class Company(models.Model):
    CompanyId= models.AutoField(primary_key=True)
    CompanyName=models.CharField(max_length=500)
    Price_Per_BP=models.FloatField()
    BP_Length_Minimum=models.BigIntegerField()
    BP_Length_Medium=models.BigIntegerField()
    BP_Length_Maximum=models.BigIntegerField()
    BP_Length_PriceIncrease=models.DecimalField(max_digits=5, decimal_places=3)
    GC_Content_Minimum=models.DecimalField(max_digits=4, decimal_places=3)
    GC_Content_Maximum=models.DecimalField(max_digits=4, decimal_places=3)
    GC_Content_PriceIncrease=models.DecimalField(max_digits=5, decimal_places=3)
    Homology_Min_Length_Minimum=models.BigIntegerField()
    Homology_Min_PriceIncrease=models.DecimalField(max_digits=5, decimal_places=3)
    Double_Stranded_Price_Increase=models.DecimalField(max_digits=5, decimal_places=3)
