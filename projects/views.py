from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchProject, paginateProjects


def projects(request):
    projects, search_query = searchProject(request)
    custom_range, projects = paginateProjects(request, projects, 3)
    context = {'projects' : projects, 'search_query' : search_query, 'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)

def project(request,pk):
    projects = Project.objects.get(id = pk)
    tags = projects.tags.all()
    form = ReviewForm
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projects
        review.owner = request.user.profile
        review.save()
        projects.getVoteCount
        messages.success(request, 'Your review successfully completed!')
        return redirect('project', pk=projects.id)

    context = {'project' : projects, 'tags' : tags, 'form' : form}
    return render(request, 'projects/single-project.html', context)

@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()
    profile = request.user.profile
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.owner = profile
            project.save()
            return redirect('projects')

    context = {'form' : form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES ,instance= project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form' : form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    
    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object' : project}
    return render(request, 'delete_template.html', context)