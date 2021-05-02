from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver



class Myloc(models.Model):
    my_area_name = models.CharField(max_length=60, null=True)
    location = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    my_area_image = models.ImageField(upload_to='images/',default='')
    description = models.TextField(default='')

    def create_myloc(self):
        self.save()

    def delete_myloc(self):
        self.delete()

    @classmethod
    def search_by_location(cls, search_term):
        certain_user=cls.objects.filter(location__icontains=search_term)
        return certain_user
    def __str__(self):
        return self.location

class Profile(models.Model):
    profile_image = models.ImageField(null=True,upload_to='profile_pic/')
    bio = models.CharField(max_length=200)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mylocs = models.ForeignKey(Myloc, on_delete=models.CASCADE, null=True)


    @classmethod
    def get_profile(cls):
        all_profiles = cls.objects.all()
        return all_profiles

    def save_profles(self):
        self.save()

    def delete_profiles(self):
        self.delete()

    def __str__(self):
        return str(self.user)
        
class Post(models.Model):
    post = models.CharField(max_length=200,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    myloc = models.ForeignKey(Myloc,on_delete=models.CASCADE,null=True,blank=True)


class Activity(models.Model):
    activity_name = models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=200,null=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    myloc = models.ForeignKey(Myloc, on_delete=models.CASCADE)
    email = models.EmailField()
    def create_activity(self):
        self.save()
    def delete_activity(self):
        self.delete()

