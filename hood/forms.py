from django import forms
from django.forms import ModelForm,Textarea,IntegerField
from .models import Neighbourhood,Business,Post,Profile


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','neighbourhoods']
class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model=Neighbourhood
        fields = ['hood_name','location','hood_image','description','health_tell','police_number']
class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['business_name','description','email']
class NewPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['post']