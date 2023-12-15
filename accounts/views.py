from allauth.account.views import LoginView, SignupView, LogoutView, PasswordChangeView, PasswordResetView, \
    PasswordResetDoneView

"""
Used Views from allauth lib:
- `LoginView`: This view handles the sign-in functionality, security and validation.
- `SignupView`: This view handles the sign-up functionality, security and validation.
- `LogoutView`: This view handles the sign-out functionality, security and validation. 
- `PasswordChangeView`: This view handles the password change functionality, security and validation.
- `PasswordResetView`: This view handles the password reset functionality, security and validation.
- `PasswordResetDoneView`: This view handles the password reset done functionality, security and validation.
"""
from accounts.forms import CustomLoginForm

from django.shortcuts import render
from django.urls import reverse_lazy


def landing_view(request):
    return render(request, "accounts/landing_page.html")
"""
This is a function-based view that renders the "landing_page.html" template.
"""

# ======================================================================================================================
#
# New views for allauth authentication
# Additional functionality:
# get_context_data() is used to render 2 forms on the same page
#


class UserSigninView(LoginView):
    template_name = 'account/signin_signup.html'
    success_url = reverse_lazy('home')

    def get_form_class(self):
        return CustomLoginForm  # set remember=True by default

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_login'] = True
        context['form_login'] = context.pop('form')
        context['form_signup'] = SignupView.form_class()
        return context
"""
This class-based view extends `LoginView`(allauth lib) and handles the sign-in functionality.
It renders the "login_signup.html" template, uses the `LoginForm`(allauth lib) form class.
LoginView has a lot of functionality and security, so it is better to use it instead of creating your own view.
LoginForm has a lot of functionality and security, so it is better to use it instead of creating your own form.
You can check it in the source code of allauth lib.

get_context_data() is used to pass the signup form to the template when user clicks on "Sign up" button.
"""


class UserSignupView(SignupView):
    template_name = 'account/signin_signup.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_login'] = False
        context['form_signup'] = context.pop('form')
        context['form_login'] = LoginView.form_class()
        return context
"""
This class-based view extends `SignupView`(allauth lib) and handles the sign-up functionality.
It renders the "login_signup.html" template, uses the `SignupForm`(allauth lib) form class.
SignupView has a lot of functionality and security, so it is better to use it instead of creating your own view.
SignupForm has a lot of functionality and security, so it is better to use it instead of creating your own form.
You can check it in the source code of allauth lib.

get_context_data() is used to pass the login form to the template when user clicks on "Sign in" button.
"""


class UserLogoutView(LogoutView):
    url = reverse_lazy('landing_view')


class UserPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('landing_view')
    template_name = 'account/password_change.html'


class UserPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('landing_view')
    template_name = 'account/password_reset.html'


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'
