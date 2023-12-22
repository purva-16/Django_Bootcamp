from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website',
        'topRated': True 
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work',
        'topRated': False
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community',
        'topRated': True 
    }
]

def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/projects.html', context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    #tags = projectObj.tags.all()
    #reviews = projectObj.reviews_set.all()
    context = {'project':projectObj}
    return render(request,'projects/single-projects.html', context) 

# Create your views here.
