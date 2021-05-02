from django import forms
from django.forms import ModelForm,Textarea,IntegerField
from .models import Myloc,Activity,Post,Profile


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','mylocs']
class MylocForm(forms.ModelForm):
    class Meta:
        model=Myloc
        fields = ['my_area_name','location','my_area_image','description']
class NewActivityForm(forms.ModelForm):
    class Meta:
        model=Activity
        fields=['activity_name','description','email']
class NewPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['post']