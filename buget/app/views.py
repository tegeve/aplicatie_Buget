from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from .models import Project


def project_list(request):
    return render(request, "app/project-list.html")


def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    return render(request, "app/project-detail.html", {'project': project, 'expenses_list': project.expenses.all()})


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'app/add-project.html'
    fields = ('name', 'budget')
