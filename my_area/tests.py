from django.test import TestCase
from .models import Profile, Myloc, Post, Activity
from django.contrib.auth.models import User

class ProfileTestClass(TestCase):

   #Test case for the Profile class

    def setUp(self):
        # Create instance of Profile class
        self.new_profile = Profile(bio="My profile test")

    def test_instance(self):
       
        self.assertTrue(isinstance(self.new_profile, Profile))


class Myloc(TestCase):
    
    #Test case for the Myloc class
    
    def setUp(self):

        # Create a Image instance
        self.new_Image = Image(
            caption='hello')

    def test_instance(self):
        
        #Test to check an instance of Image class
        
        self.assertTrue(isinstance(self.new_Image, Image))


class Post(TestCase):
   
    def setUp(self):
       
        # Create a Comment instance
        self.post = post(
            post_content='hello')

    def test_instance(self):
       
        self.assertTrue(isinstance(self.post))

    def test_get_Image_post(self):
       
        self.test_profile = Profile(user=self.user, bio="New Profile")

        self.test_Image = Image(user=self.user, caption="Newer Profile")
self.assertTrue(len(gotten_posts) == len(posts))

