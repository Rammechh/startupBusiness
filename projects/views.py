from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def projects(request):
    projects = Project.objects.all()
    context = {'projects' : projects}
    return render(request, 'projects/projects.html', context)

def project(request,pk):
    projects = Project.objects.get(id = pk)
    tags = projects.tags.all()
    context = {'projects' : projects, 'tags' : tags}
    return render(request, 'projects/single-project.html', context)
