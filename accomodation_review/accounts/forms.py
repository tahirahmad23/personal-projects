from django import forms
from .models import UserAccount
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username","email","password")
        widgets = {
             "username" : forms.TextInput(attrs={"class":"form-control usernameinput","placeholder":"Full name"}),
             "email" : forms.EmailInput(attrs={"class":"form-control emailinput","placeholder":"Email"}),
             "password" : forms.PasswordInput(attrs={"class":"form-control passwordinput","placeholder":"Password"})
        }
class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ("profile_pic","department")
        widgets = {
            "profile_pic" : forms.FileInput(attrs={"class":"form-control profilepicinput"}),
            "department": forms.TextInput(attrs={"class":"form-control departmentinput"})

        }
