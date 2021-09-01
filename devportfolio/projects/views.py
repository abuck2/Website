from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

projects_list = [{'unique_id' : 1,
        'title' : 'agent-based model',
        'description' : 'Plants-Rabbits-Foxes ecosystem simulation'},
        {'unique_id' : 2,
        'title' : 'Time-series',
        'description' : 'Time-series simulations and prediction'}]



def projects(request):
    page = 'projects'
    number = 10
    context = {'page':page, 'number':number, 'projects':projects_list}


    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj = None
    for i in projects_list:
        print(i)
        if str(i["unique_id"]) == str(pk):
            projectObj = i
            print(projectObj)
    return render(request, "projects/single-project.html", {"project":projectObj})
