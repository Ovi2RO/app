from django.urls import path
from .views import *
"""
1. `from django.urls import path`: This import is used to define URL patterns in Django.

2. `from .views import *`: This import is used to import all the views from the `views.py` file.
"""


urlpatterns = [
    path('signout/', UserLogoutView.as_view(), name='account_signout'),
    path('signin/', UserSigninView.as_view(), name='account_login'),
    path('signup/', UserSignupView.as_view(), name='account_signup'),
    path('password/reset/', UserPasswordResetView.as_view(), name='account_password_reset'),
    path('password/reset/done/', UserPasswordResetDoneView.as_view(), name='account_password_reset_done'),
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


