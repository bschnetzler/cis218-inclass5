from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from .models import Project, Ticket

class ProjectListView(ListView):
    '''Project List View'''

    model = Project
    template_name = "project_list.html"

class ProjectDetailView(DetailView):
    '''Project Detail View'''

    model = Project
    template_name = 'project_detail.html'

class ProjectDetailClosedView(DetailView):
    '''Project Detail Closed View'''

    model = Project
    template_name = "project_detail_closed.html"

class ProjectCreateView(CreateView):
    '''Project Create View'''

    model = Project
    template_name = "project_create.html"
    fields = [
        'name',
        'members',
    ]

    def get_success_url(self):
        '''Get success URL'''

        messages.success(
            self.request,
            "Project Created Successfully!",
        )

        return reverse("project_list")
    
class ProjectUpdateView(UpdateView):
    '''Project Update View'''

    model = Project
    template_name = "project_update.html"
    fields = [
        'name',
        'members',
    ]

    def get_success_url(self):
        '''Get success URL'''

        messages.success(
            self.request,
            "Project Updated Successfully!",
        )

        return reverse("project_list")