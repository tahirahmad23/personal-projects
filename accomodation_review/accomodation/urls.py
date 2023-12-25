from django.urls import path
from . import views

app_name = "accomodation"
urlpatterns = [
    path("new_house/",views.CreateHouse.as_view(),name="create_house"),
    path("update_house/<int:pk>",views.UpdateHouse.as_view(),name="update_house"),
    path("delete_house/<int:pk>",views.DeleteHouse.as_view(),name="delete_house"),
    path("house_list/",views.HouseList.as_view(),name="house_list"),
    path("house_detail/<int:pk>",views.HouseDetail.as_view(),name="house_detail"),
    path("search/",views.search_house,name="search_house")
]
