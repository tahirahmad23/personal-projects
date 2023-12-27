from django.db.models import Q
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse_lazy
from .models import House,Photo,Review
from accounts.models import UserAccount
from django.views.generic.edit import FormMixin
from .forms import HouseForm,PhotoForm,ReviewForm,HouseSearchForm
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings

class SuperuserOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class CreateHouse(SuperuserOnlyMixin,CreateView):
    model = House
    form_class = HouseForm
    template_name = "house_form.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["photoform"] = PhotoForm
        return context

    def form_valid(self,form):
        self.object = form.save()
        for image in self.request.FILES.getlist("images"):
            Photo.objects.create(image=image,house=self.object)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("accomodation:house_list")

class UpdateHouse(SuperuserOnlyMixin,UpdateView):
    model = House
    form_class = HouseForm
    template_name = "house_form.html"
    def get_success_url(self):
        return reverse_lazy("accomodation:house_detail",kwargs={"pk":self.kwargs.get("pk")})

class HouseList(ListView):
    model = House
    template_name = "house_list.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["media"] = settings.MEDIA_URL
        return context


class HouseDetail(FormMixin,DetailView):
    model = House
    template_name = "house_detail.html"
    form_class = ReviewForm

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["review_form"] = self.get_form()
        context["media"] = settings.MEDIA_URL
        return context

    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            form = self.get_form()
            self.object = self.get_object()
            if form.is_valid():
                review = form.save(commit=False)
                review.house = self.object
                review.user = get_object_or_404(UserAccount,user=self.request.user)
                review.save()
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            return redirect(self.request.path)

    def get_success_url(self):
        return self.request.path
class DeleteHouse(SuperuserOnlyMixin,DeleteView):
    model = House
    template_name = "house_confirm_delete.html"
    def get_success_url(self):
        return reverse_lazy("accomodation:house_list")




def search_house(request):
    form = HouseSearchForm(request.GET)
    houses = []

    if form.is_valid():

        query = form.cleaned_data.get('q')
        if query:
            houses = House.objects.filter(
                Q(name__icontains=query) |
                Q(address__icontains=query)
            ).distinct()

    return render(request, 'base.html', {'form': form, 'houses': houses})
