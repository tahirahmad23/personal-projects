from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail

# Create your views here.

class HomePage(TemplateView):
    template_name = "portfolio/home.html"


def contact(request):
    return render(request,'portfolio/contact.html',{})
