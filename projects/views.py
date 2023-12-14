from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse('this is our projects page')

def project(request,pk):
    return HttpResponse('projects page:'+ str(pk))

# Create your views here.
