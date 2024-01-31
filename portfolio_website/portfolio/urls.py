from . import views
from django.urls import path

app_name= " portfolio"

urlpatterns = [
    path("",views.HomePage.as_view(),name="home"),
    path("contact/",views.contact,name="contact")
]
