from django.urls import path
from .views import home_page

urlpatterns = [
    path('', home_page, name='home'),
]

"""
- `from django.urls import path` imports the `path` function from Django's `urls` module. The `path` function 
is used to define URL patterns for your Django project.

- `from .views import home_page` imports the `home_page` view function from the local `views` module. This 
assumes that there is a `views.py` file in the same directory as this code and that `home_page` is a view 
function defined in that file.

- `urlpatterns` is a list that holds the URL patterns for your Django project. Each URL pattern is defined as 
an element in this list.

- `path('', home_page, name='home')` defines a URL pattern. It uses the `path` function to specify that the 
URL pattern matches the root URL (`''`). When a user visits the root URL of your project, the `home_page` view 
function will be called. The `name` parameter is used to provide a unique name for this URL pattern, which can 
be used to reference it in other parts of your Django project.
"""