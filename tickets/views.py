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
    
class TicketCreateView(CreateView):
    '''Create a new Ticket'''

    model = Ticket
    template_name = 'ticket_create.html'
    fields = [
        "name",
        "description",
        "priority",
        "assigned_to",
        "complete_by",
        "completed",
    ]

    def get(self, request, project_pk, *args, **kwargs):
        '''Handle GET request'''

        self.project_pk = project_pk
        return super().get(request, project_pk, *args, **kwargs)
    
    def post(self, request, project_pk, *args, **kwargs):
        '''Handle POST request'''

        self.project_pk = project_pk
        return super().post(request, project_pk, *args, **kwargs)
    
    def get_context_data(self):
        '''Get Context Data'''

        context = super().get_context_data()
        context['project'] = Project.objects.get(pk=self.project_pk)
        return context 
    
    def form_valid(self, form):
        '''Validate Form'''

        form.instance.project = Project.objects.get(pk=self.project_pk)
        return super().form_valid(form)
    
    def get_success_url(self):
        '''Get Success URL'''

        messages.success(self.request, "Ticket Created Successfully!")
        return reverse("project_detail", kwargs={"pk": self.project_pk})


class TicketEditView(UpdateView):
    '''Edit a Ticket'''

    model = Ticket
    template_name = 'ticket_update.html'
    fields = [
        "name",
        "description",
        "priority",
        "assigned_to",
        "complete_by",
        "completed",
    ]

    def get(self, request, project_pk, *args, **kwargs):
        '''Handle GET request'''

        self.project_pk = project_pk
        return super().get(request, project_pk, *args, **kwargs)
    
    def post(self, request, project_pk, *args, **kwargs):
        '''Handle POST request'''

        self.project_pk = project_pk
        return super().post(request, project_pk, *args, **kwargs)
    
    def get_context_data(self):
        '''Get Context Data'''

        context = super().get_context_data()
        context['project'] = Project.objects.get(pk=self.project_pk)
        return context
    
    def get_success_url(self):
        '''Get Success URL'''

        messages.success(self.request, "Ticket Updated Successfully!")
        return reverse("project_detail", kwargs={"pk": self.project_pk})
