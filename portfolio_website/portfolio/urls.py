from . import views
from django.urls import path

app_name= " portfolio"

urlpatterns = [
    path("",views.HomePageView.as_view(),name="home"),
    # path("project_list/",views.ProjectListView.as_view(),name="project_list"),
    path("project/<int:pk>",views.ProjectView.as_view(),name="project")
]
