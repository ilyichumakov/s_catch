from django.shortcuts import render, get_object_or_404

from endpoints.models import Project, EndPointGroup, EndPoint


def project_list(request):
    projects = Project.objects.all()
    context = {
        "user": request.user,
        "projects": projects,
    }
    return render(request, 'endpoints/project_list.html', context)


def group_list(request, project_name):
    project = get_object_or_404(Project, system_name=project_name)
    groups = EndPointGroup.objects.filter(project=project)

    context = {
        "user": request.user,
        "project": project,
        "groups": groups,
    }
    return render(request, 'endpoints/group_list.html', context)


def endpoint_list(request, project_name, group_name):
    group = get_object_or_404(EndPointGroup, system_name=group_name, project__system_name=project_name)
    endpoints = EndPoint.objects.filter(group=group)

    context = {
        "user": request.user,
        "group": group,
        "endpoints": endpoints,
    }
    return render(request, 'endpoints/endpoint_list.html', context)


def endpoint_detail(request, endpoint_id):
    endpoint = get_object_or_404(EndPoint, id=endpoint_id)
    context = {
        "user": request.user,
        "endpoint": endpoint,
    }
    return render(request, 'endpoints/endpoint_detail.html', context)
