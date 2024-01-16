from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home_page(request):
    return render(request, "home/home.html")

"""
- `from django.shortcuts import render` imports the `render` function from Django's `shortcuts` module. 
The `render` function is used to render a Django template with a given context and return an 
`HttpResponse` object.

- `from django.contrib.auth.decorators import login_required` imports the `login_required` decorator from 
Django's `auth.decorators` module. The `login_required` decorator is used to restrict access to a view to 
only authenticated users. If a user is not logged in, they will be redirected to the login page.

- `@login_required` is a decorator that is applied to the `home_page` view function. It ensures that only 
logged-in users can access the `home_page` view. If a user is not authenticated, they will be redirected to 
the login page before being able to access the view.

- `def home_page(request):` defines the `home_page` view function, which takes a `request` object as a 
parameter. This function is responsible for processing the request and returning the appropriate response.

- `return render(request, "home/home.html")` uses the `render` function to render the `home/home.html` 
template with the provided `request` object. The rendered template is then returned as the response.
"""
