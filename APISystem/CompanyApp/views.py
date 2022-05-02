from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.shortcuts import render
from CompanyApp.models import Company
from CompanyApp.serializers import CompanySerializer,UserSerializer
from Sequence.bestCompany import BestCompany, AllCompany
from Sequence.Sequence import Sequence
from django.http import HttpResponse
import json
@csrf_exempt

def companyAPI(request,id=0):
    if request.method=='GET':
        companies = Company.objects.all()
        companies_serializer=CompanySerializer(companies,many=True)
        return JsonResponse(companies_serializer.data, safe=False)
    elif request.method=='PUT':
        companies = Company.objects.all()
        user_data=JSONParser().parse(request)
        currentSequence=Sequence(user_data['Sequence'],user_data['Type'])
        company=BestCompany(currentSequence,companies)
        return JsonResponse(json.loads(company), safe=False)
    elif request.method=='POST':
        company_data=JSONParser().parse(request)
        companies_serializer=CompanySerializer(data=company_data)
        if companies_serializer.is_valid():
            companies_serializer.save()
            return JsonResponse("Added Succesfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='DELETE':
        # company=Company.objects.get(CompanyName=name)
        # company.delete()
        # return JsonResponse("Delete Company", safe=False)
        companies = Company.objects.all()
        user_data=JSONParser().parse(request)
        print(user_data['Sequence'])
        currentSequence=Sequence(user_data['Sequence'],user_data['Type'])
        company=AllCompany(currentSequence,companies)
        return JsonResponse(json.loads(company), safe=False)
# Create your views here.
