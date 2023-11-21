from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
"""
- `django.test.TestCase`: This is a subclass of Python's `unittest.TestCase` specifically designed for testing 
Django applications. It provides additional features and assertions tailored for Django testing.

- `django.test.Client`: This is a class that provides a way to send HTTP requests to your Django application in 
tests. It allows you to simulate GET and POST requests and retrieve the response. 

- `django.urls.reverse`: This is a function that generates a URL by providing the view name as an argument. It 
helps in creating URLs for tests without hardcoding them. 
"""


class LandingViewTest(TestCase):
    def test_landing_view(self):
        response = self.client.get(reverse('landing_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/landing_page.html')


class SignInViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_signin_view_get(self):
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signin_signup.html')

    def test_signin_view_post_valid_credentials(self):
        response = self.client.post(reverse('signin'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_signin_view_post_invalid_credentials(self):
        response = self.client.post(reverse('signin'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signin_signup.html')


class SignUpViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup_view_get(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signin_signup.html')

    def test_signup_view_post_invalid_form(self):
        response = self.client.post(reverse('signup'), {'username': '', 'password1': 'newpassword', 'password2': 'newpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signin_signup.html')

class SignOutViewTest(TestCase):
    def test_signout_view(self):
        response = self.client.get(reverse('signout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('landing_view'))

"""
- `self.client.get`: This is a method provided by the `Client` class to simulate a GET request. It sends a GET 
request to the specified URL and returns the response. 

- `self.client.post`: This is a method provided by the `Client` class to simulate a POST request. It sends a POST 
request to the specified URL with the provided data and returns the response.

- `self.assertEqual`: This is an assertion method provided by the `TestCase` class. It checks if the two provided 
values are equal and raises an exception if they are not.

- `self.assertTemplateUsed`: This is an assertion method provided by the `TestCase` class. It checks if the 
response used the specified template.

- `self.assertRedirects`: This is an assertion method provided by the `TestCase` class. It checks if the response 
redirected to the specified URL.
"""

"""
To test the coverage:
> pip install coverage
> coverage run manage.py test
> coverage report
"""