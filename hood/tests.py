from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Neighbourhood, Post, Business

# Create your tests here.


class ProfileTestClass(TestCase):
    '''
    Test case for the Profile class
    '''

    def setUp(self):
        '''
        Method that creates an instance of Profile class
        '''
        # Create instance of Profile class
        self.new_profile = Profile(bio="I am superwoman")

    def test_instance(self):
        '''
        Test case to check if self.new_profile in an instance of Profile class
        '''
        self.assertTrue(isinstance(self.new_profile, Profile))


    def test_get_other_profiles(self):
        '''
        Test case to check if all profiles are gotten from the database
        '''
        self.user = User(username="Diane")
        self.user.save()

        self.user = User(username="Uwase")
        self.user.save()

        self.test_profile = Profile(user=self.user, bio="Another Profile")
        gotten_profiles = Profile.get_other_profiles(self.user.id)
        profiles = Profile.objects.all()


class Neighbourhood(TestCase):
    '''
    Test case for the Neighbourhood class
    '''

    def setUp(self):
        '''
        Method that creates an instance of Profile class
        '''
        # Create a Image instance
        self.new_Image = Image(
            caption='hey')

    def test_instance(self):
        '''
        Test case to check if self.new_Image in an instance of Image class
        '''
        self.assertTrue(isinstance(self.new_Image, Image))


   



class Post(TestCase):
    '''
    Test case for the Comment class
    '''

    def setUp(self):
        '''
        Method that creates an instance of Comment class
        '''
        # Create a Comment instance
        self.post = post(
            post_content='hey')

    def test_instance(self):
        '''
        Test case to check if self.new_comment in an instance of Comment class
        '''
        self.assertTrue(isinstance(self.post))

    def test_get_Image_post(self):
        '''
        Test case to check if get Image comments is getting comments for a specific Image
        '''
        self.user = User(username="Diane")
        self.user.save()

        self.user = User(username="Uwase")
        self.user.save()

        self.test_profile = Profile(user=self.user, bio="Another Profile")

        self.test_Image = Image(user=self.user, caption="Another Profile")

     

        # No comments were saved so expect True
        self.assertTrue(len(gotten_posts) == len(posts))
