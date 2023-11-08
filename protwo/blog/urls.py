from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<int:page_num>/",views.index,name="index"),
    path("<str:blogpost_title>/",views.entry,name="entry")
]
