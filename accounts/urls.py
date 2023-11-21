from django.urls import path
from .views import landing_view, SignInView, SignOutView, SignUpView
"""
1. `from django.urls import path`: This import is used to define URL patterns in Django.

2. `from .views import landing_view, SignInView, SignOutView, SignUpView`: These imports 
bring in the views (`landing_view`, `SignInView`, `SignOutView`, `SignUpView`) from the 
current package (module).
"""


urlpatterns = [
    path('', landing_view, name='landing_view'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signout/', SignOutView.as_view(), name='signout'),
]

"""
- `path('', landing_view, name='landing_view')`: This URL pattern maps the root URL to the `landing_view` 
function-based view. The `name` parameter sets the name of the URL pattern as 'landing_view'.

- `path('signin/', SignInView.as_view(), name='signin')`: This URL pattern maps the '/signin/' URL to the 
`SignInView` class-based view. The `name` parameter sets the name of the URL pattern as 'signin'.

- `path('signup/', SignUpView.as_view(), name='signup')`: This URL pattern maps the '/signup/' URL to the 
`SignUpView` class-based view. The `name` parameter sets the name of the URL pattern as 'signup'.

- `path('signout/', SignOutView.as_view(), name='signout')`: This URL pattern maps the '/signout/' URL to the 
`SignOutView` class-based view. The `name` parameter sets the name of the URL pattern as 'signout'.
"""


