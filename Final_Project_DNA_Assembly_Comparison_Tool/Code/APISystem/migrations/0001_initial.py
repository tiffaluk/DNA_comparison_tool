# Generated by Django 4.0.4 on 2022-04-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('CompanyId', models.AutoField(primary_key=True, serialize=False)),
                ('CompanyName', models.CharField(max_length=500)),
                ('Price_Per_BP', models.FloatField()),
                ('BP_Length_Minimum', models.BigIntegerField()),
                ('BP_Length_Medium', models.BigIntegerField()),
                ('BP_Length_Maximum', models.BigIntegerField()),
                ('BP_Length_PriceIncrease', models.DecimalField(decimal_places=3, max_digits=5)),
                ('GC_Content_Minimum', models.DecimalField(decimal_places=3, max_digits=4)),
                ('GC_Content_Maximum', models.DecimalField(decimal_places=3, max_digits=4)),
                ('GC_Content_PriceIncrease', models.DecimalField(decimal_places=3, max_digits=5)),
                ('Homology_Min_Length_Minimum', models.BigIntegerField()),
                ('Homology_Min_PriceIncrease', models.DecimalField(decimal_places=3, max_digits=5)),
                ('Double_Stranded_Price_Increase', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
    ]
