from . import views
from django.urls import path

app_name= " portfolio"

urlpatterns = [
    path("",views.HomePageView.as_view(),name="home"),
    path("contact/",views.ContactPageView.as_view(),name="contact"),
    path("about/",views.AboutPageView.as_view(),name="about"),
    path("project_list/",views.ProjectListView.as_view(),name="project_list"),
    path("project/<int:pk>",views.ProjectView.as_view(),name="project")
]
