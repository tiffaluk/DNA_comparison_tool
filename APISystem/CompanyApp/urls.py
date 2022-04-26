from django.urls import re_path as url
from CompanyApp import views
from django.urls import path
urlpatterns=[
    url(r'^company$',views.companyAPI),
    url(r'^company/([0-9]+)$',views.companyAPI)
]
