from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.core.mail import send_mail
from .models import Project
from django.forms import ModelForm

# form
class ProjectForm(ModelForm):
    model = Project
    fields = ["title","content"]

# Create your views here.

class HomePageView(TemplateView):
    template_name = "portfolio/home.html"

class AboutPageView(TemplateView):
    template_name = "portfolio/about.html"

class ContactPageView(TemplateView):
    template_name = "portfolio/contact.html"

class ProjectListView(ListView):
    model = Project
    template_name = "portfolio/project_list.html"

class ProjectView(DetailView):
    model = Project
    template_name = "portfolio/project.html"

# class CreateProjectView(CreateView):
#     model = Project
#     form_class = ProjectForm
#     template_name = "portfolio"