
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/",views.SignUp.as_view(),name="signup"),
    path("moreinfo/",views.CreateUserAccount.as_view(),name="user_account"),
    path("login/",auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    path("logout/",views.logout_view,name="logout")
    # path("logout/",auth_views.LogoutView.as_view(),name="logout"),
]
