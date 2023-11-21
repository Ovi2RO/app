from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, RedirectView


"""
1. `from django.shortcuts import render, redirect`: This import allows you to render HTML templates 
and redirect to another URL.

2. `from django.contrib.auth import authenticate, login, logout`: These imports provide 
authentication-related functionality. `authenticate` is used to verify a user's credentials, 
`login` is used to log in a user, and `logout` is used to log out a user.

3. `from django.contrib.auth.forms import AuthenticationForm, UserCreationForm`: These imports 
provide pre-defined forms for authentication. `AuthenticationForm` is a form for logging in, and 
`UserCreationForm` is a form for user registration.

4. `from django.urls import reverse_lazy`: This import provides a lazy version of URL reversing, 
which allows you to refer to URLs by their name instead of hard-coding them.

5. `from django.views.generic import CreateView, FormView, RedirectView`: These imports provide 
class-based views for creating forms, handling form submissions, and redirecting to a specific URL.
"""


def landing_view(request):
    return render(request, "accounts/landing_page.html")
"""
This is a function-based view that renders the "landing_page.html" template.
"""


class SignInView(FormView):
    template_name = 'accounts/signin_signup.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
"""
 This class-based view extends `FormView` and handles the sign-in functionality. 
 It renders the "signin_signup.html" template, uses the `AuthenticationForm` 
 form class, and redirects to the "home" URL upon successful form submission.
"""


class SignUpView(CreateView):
    template_name = 'accounts/signin_signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('signin')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response
"""
This class-based view extends `CreateView` and handles the sign-up functionality. 
It renders the "signin_signup.html" template, uses the `UserCreationForm` form class, 
and redirects to the "signin" URL upon successful form submission. It also logs in 
the user after successful registration.
"""


class SignOutView(RedirectView):
    url = reverse_lazy('landing_view')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
"""
This class-based view extends `RedirectView` and handles the sign-out functionality. 
It logs out the user and redirects to the "landing_view" URL.
"""
