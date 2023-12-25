from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, mixins, forms,logout
from .models import UserAccount
from .forms import UserForm, UserAccountForm
# Create your views here.


class SignUp(CreateView):

    model = User
    template_name = "signup.html"
    form_class = UserForm
    success_url = reverse_lazy("accounts:user_account")

    def form_valid(self,form):

        self.object = form.save(commit=False)
        self.object.set_password(form.cleaned_data["password"])
        self.object.save()

        user = authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password"])

        if user is not None:
            login(self.request,user)

        return super().form_valid(form)


class CreateUserAccount(mixins.LoginRequiredMixin, CreateView):

    model = UserAccount
    template_name = "user_account.html"
    form_class = UserAccountForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

def logout_view(request):

    logout(request)
    return redirect("home")
