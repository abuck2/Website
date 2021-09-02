from django.shortcuts import render
from django.http  import HttpResponse
from .models import Project

# Create your views here.

projects_list = [{'unique_id' : 1,
        'title' : 'agent-based model',
        'description' : 'Plants-Rabbits-Foxes ecosystem simulation'},
        {'unique_id' : 2,
        'title' : 'Time-series',
        'description' : 'Time-series simulations and prediction'}]



def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}


    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    #tags = Project.objects.tags.all()
    return render(request, "projects/single-project.html", {"project":projectObj, 'tags':tags})
