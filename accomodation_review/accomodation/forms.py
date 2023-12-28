from django import forms
from .models import House,Photo,Review



class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class FileFieldForm(forms.Form):
    file_field = MultipleFileField()
class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = "__all__"
try:

    class PhotoForm(forms.Form):
        class Meta:
            fields =["images"]
            widgets = {
                "images": forms.ClearableFileInput(attrs={"multiple":True})
            }
except:
    class PhotoForm(forms.Form):
        images = MultipleFileField()
    # class Meta:
    #     fields =["image"]
    #     widgets = {
    #         "image": forms.ClearableFileInput(attrs={"multiple":True})
    #     }

class ReviewForm(forms.ModelForm):
    ratings = [
    ("","Select a rating"),
    ("excellent","Excellent"),
    ("good","Good"),
    ("okay","Not bad"),
    ("bad","Bad"),
    ("poor","Very Poor"),
    ]
    rating = forms.ChoiceField(choices=ratings,widget=forms.Select(attrs={"class":"form-select ratinginput"}))
    class Meta:
        model = Review
        fields = ["rating","comment"]
        widgets = {
            "comment" : forms.Textarea(attrs={"class":"form-control commentinput","placeholder":"comment"})
        }

class HouseSearchForm(forms.Form):
    q = forms.CharField(label="Search",required = False ,widget=forms.TextInput(attrs={'class': 'form-control'}))
