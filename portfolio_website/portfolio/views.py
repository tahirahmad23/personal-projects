from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.core.mail import send_mail
from .models import Project

# Create your views here.

# class HomePageView(TemplateView):
#     template_name = "portfolio/home.html"


class HomePageView(ListView):
    model = Project
    template_name = "portfolio/home.html"

class ProjectView(DetailView):
    model = Project
    template_name = "portfolio/project.html"

