from typing import Any
from unicodedata import category
from urllib import request
from colorama import init
from django import dispatch
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    FormView,
)
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import MarketplaceItemPost
from .forms import CreateMarketplacePostForm, SearchForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from dj_proj.mixins import AuthorOrStaffRequiredMixin
from django.urls import reverse


@method_decorator(login_required, name="dispatch")
class MarketplaceListView(ListView):
    model = MarketplaceItemPost
    template_name = "marketplace/marketplace_list.html"
    context_object_name = "marketposts"
    ordering = "-created_on"

"""
1. `@method_decorator(login_required, name="dispatch")`:
   - This decorator is used to apply the `login_required` decorator to the `dispatch` method of the view.
   - `login_required` is a decorator provided by Django that ensures the user must be logged in to access the view.

2. `class MarketplaceListView(ListView):`:
   - This line defines a class named `MarketplaceListView` that inherits from the `ListView` class.
   - By inheriting from `ListView`, the `MarketplaceListView` class inherits the functionality and attributes of 
   the `ListView` class.

3. `model = MarketplaceItemPost`:
   - This line defines the model that the `MarketplaceListView` view will operate on.
   - The view will work with the `MarketplaceItemPost` model.

4. `template_name = "marketplace/marketplace_list.html"`:
   - This line specifies the template that will be used to render the view.
   - The template is located at `marketplace/marketplace_list.html`.

5. `context_object_name = "marketposts"`:
   - This line sets the name of the variable that will be used to access the queryset in the template.
   - The queryset will be available as the `marketposts` variable in the template.

6. `ordering = "-created_on"`:
   - This line specifies the ordering of the queryset.
   - The queryset will be ordered in descending order based on the `created_on` field.
"""


@method_decorator(login_required, name="dispatch")
class MarketplaceDetailView(DetailView):
    model = MarketplaceItemPost
    template_name = "marketplace/marketplace_detail.html"
    context_object_name = "marketpost"

"""
1. `@method_decorator(login_required, name="dispatch")`:
   - This decorator is used to apply the `login_required` decorator to the `dispatch` method of the view.
   - `login_required` is a decorator provided by Django that ensures the user must be logged in to access the view.

2. `class MarketplaceDetailView(DetailView):`:
   - This line defines a class named `MarketplaceDetailView` that inherits from the `DetailView` class.
   - By inheriting from `DetailView`, the `MarketplaceDetailView` class inherits the functionality and attributes 
   of the `DetailView` class.

3. `model = MarketplaceItemPost`:
   - This line defines the model that the `MarketplaceDetailView` view will operate on.
   - The view will work with the `MarketplaceItemPost` model.

4. `template_name = "marketplace/marketplace_detail.html"`:
   - This line specifies the template that will be used to render the view.
   - The template is located at `marketplace/marketplace_detail.html`.

5. `context_object_name = "marketpost"`:
   - This line sets the name of the variable that will be used to access the object in the template.
   - The object will be available as the `marketpost` variable in the template.
"""


@method_decorator(login_required, name="dispatch")
class MarketplaceCreateView(CreateView):
    model = MarketplaceItemPost
    form_class = CreateMarketplacePostForm
    template_name = "marketplace/marketplace_create.html"
    success_url = "/marketplace/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

"""
1. `@method_decorator(login_required, name="dispatch")`:
   - This decorator is used to apply the `login_required` decorator to the `dispatch` method of the view.
   - `login_required` is a decorator provided by Django that ensures the user must be logged in to access the view.

2. `class MarketplaceCreateView(CreateView):`:
   - This line defines a class named `MarketplaceCreateView` that inherits from the `CreateView` class.
   - By inheriting from `CreateView`, the `MarketplaceCreateView` class inherits the functionality and attributes 
   of the `CreateView` class.

3. `model = MarketplaceItemPost`:
   - This line defines the model that the `MarketplaceCreateView` view will operate on.
   - The view will work with the `MarketplaceItemPost` model.

4. `form_class = CreateMarketplacePostForm`:
   - This line specifies the form class that will be used for creating new instances of the model.
   - The `CreateMarketplacePostForm` form class will be used.

5. `template_name = "marketplace/marketplace_create.html"`:
   - This line specifies the template that will be used to render the view.
   - The template is located at `marketplace/marketplace_create.html`.

6. `success_url = "/marketplace/"`:
   - This line specifies the URL to redirect to after a successful form submission.
   - The user will be redirected to the `/marketplace/` URL.

7. `def form_valid(self, form):`:
   - This method is called when the form is valid.
   - It is overridden to set the `author` attribute of the form instance to the currently logged-in user.

8. `form.instance.author = self.request.user`:
   - This line sets the `author` attribute of the form instance to the currently logged-in user.
   - The `request.user` attribute represents the user object associated with the current request.

9. `return super().form_valid(form)`:
   - This line calls the `form_valid` method of the parent class to perform the default behavior.
   - It returns the result of the parent's `form_valid` method.
"""


@method_decorator(login_required, name="dispatch")
class MarketplaceUpdateView(AuthorOrStaffRequiredMixin, UpdateView):
    model = MarketplaceItemPost
    template_name = "marketplace/marketplace_update.html"
    fields = [
        "title",
        "description",
        "price",
        "location",
        "category",
        "image",
    ]
    success_url = "/marketplace/"

"""
1. `@method_decorator(login_required, name="dispatch")`:
   - This decorator is used to apply the `login_required` decorator to the `dispatch` method of the view.
   - `login_required` is a decorator provided by Django that ensures the user must be logged in to access the view.

2. `class MarketplaceUpdateView(AuthorOrStaffRequiredMixin, UpdateView):`:
   - This line defines a class named `MarketplaceUpdateView` that inherits from the `UpdateView` class and the 
   `AuthorOrStaffRequiredMixin` mixin.
   - By inheriting from `UpdateView`, the `MarketplaceUpdateView` class inherits the functionality and attributes 
   of the `UpdateView` class.

3. `model = MarketplaceItemPost`:
   - This line defines the model that the `MarketplaceUpdateView` view will operate on.
   - The view will work with the `MarketplaceItemPost` model.

4. `template_name = "marketplace/marketplace_update.html"`:
   - This line specifies the template that will be used to render the view.
   - The template is located at `marketplace/marketplace_update.html`.

5. `fields = [...]`:
   - This line specifies the fields that will be editable in the form.
   - The specified fields (`title`, `description`, `price`, `location`, `category`, `image`) will be editable.

6. `success_url = "/marketplace/"`:
   - This line specifies the URL to redirect to after a successful form submission.
   - The user will be redirected to the `/marketplace/` URL.
"""


@method_decorator(login_required, name="dispatch")
class MarketplaceDeleteView(AuthorOrStaffRequiredMixin, DeleteView):
    model = MarketplaceItemPost
    template_name = "marketplace/marketplace_delete.html"
    success_url = "/marketplace/"
    context_object_name = "marketpost"      #

"""
1. `@method_decorator(login_required, name="dispatch")`:
   - This decorator is used to apply the `login_required` decorator to the `dispatch` method of the view.
   - `login_required` is a decorator provided by Django that ensures the user must be logged in to access the view.

2. `class MarketplaceDeleteView(AuthorOrStaffRequiredMixin, DeleteView):`:
   - This line defines a class named `MarketplaceDeleteView` that inherits from the `DeleteView` class and the 
   `AuthorOrStaffRequiredMixin` mixin.
   - By inheriting from `DeleteView`, the `MarketplaceDeleteView` class inherits the functionality and attributes 
   of the `DeleteView` class.

3. `model = MarketplaceItemPost`:
   - This line defines the model that the `MarketplaceDeleteView` view will operate on.
   - The view will work with the `MarketplaceItemPost` model.

4. `template_name = "marketplace/marketplace_delete.html"`:
   - This line specifies the template that will be used to render the view.
   - The template is located at `marketplace/marketplace_delete.html`.

5. `success_url = "/marketplace/"`:
   - This line specifies the URL to redirect to after a successful deletion.
   - The user will be redirected to the `/marketplace/` URL.
"""


@method_decorator(login_required, name="dispatch")
class MarketplaceSearchResultsView(ListView):
    model = MarketplaceItemPost
    template_name = "marketplace/marketplace_search_results.html"
    context_object_name = "posts"

    def get_queryset(self):
         form = SearchForm(self.request.GET)
         posts = super().get_queryset()

         if form.is_valid():
            #need the clean form data
            cln_dt = form.cleaned_data
            title = form.cleaned_data.get("title")
            user = form.cleaned_data.get("user")
            category = form.cleaned_data.get("category")
            min_price = form.cleaned_data.get("min_price")
            max_price = form.cleaned_data.get("max_price")
            location = form.cleaned_data.get("location")
            init_post_date = form.cleaned_data.get("init_post_date")
            final_post_date = form.cleaned_data.get("final_post_date")
            print(self.request.GET)

            # now we filter

            if title:
                  posts = posts.filter(title__icontains=title)
            if user:
                  posts = posts.filter(user__username__icontains=user)
            if category != "":
                  posts = posts.filter(category=category)
            if min_price is not None:
                  posts = posts.filter(price__gte=min_price)
            if max_price is not None:
                  posts = posts.filter(price__lte=max_price)
            if location:
                  posts = posts.filter(location__icontains=location)
            if init_post_date:
                  posts = posts.filter(created_at__date__gte=init_post_date)
            if final_post_date:
                  posts = posts.filter(created_at__date__lte=final_post_date)
         return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SearchForm(self.request.GET)
        return context

"""
1. `@method_decorator(login_required, name="dispatch")`:
   - This decorator is used to apply the `login_required` decorator to the `dispatch` method of the view.
   - `login_required` is a decorator provided by Django that ensures the user must be logged in to access the view.

2. `class MarketplaceSearchResultsView(ListView):`:
   - This line defines a class named `MarketplaceSearchResultsView` that inherits from the `ListView` class.
   - By inheriting from `ListView`, the `MarketplaceSearchResultsView` class inherits the functionality and 
   attributes of the `ListView` class.

3. `model = MarketplaceItemPost`:
   - This line defines the model that the `MarketplaceSearchResultsView` view will operate on.
   - The view will work with the `MarketplaceItemPost` model.

4. `template_name = "marketplace/marketplace_search_results.html"`:
   - This line specifies the template that will be used to render the view.
   - The template is located at `marketplace/marketplace_search_results.html`.

5. `context_object_name = "posts"`:
   - This line sets the context object name for the list of objects.
   - The list of objects will be available in the template context as `posts`.

6. `get_queryset(self)`:
   - This method is overridden to customize the queryset used to retrieve the list of objects.
   - It creates an instance of the `SearchForm` form using the `GET` data from the request.
   - The method then filters the queryset based on the form data, applying various filters such as title, user, 
   category, price, location, and post dates.

7. `get_context_data(self, **kwargs)`:
   - This method is overridden to add additional context data to the template context.
   - It creates an instance of the `SearchForm` form using the `GET` data from the request and adds it to the 
   context.
"""


@method_decorator(login_required, name="dispatch")
class MarketplaceMyPostsView(ListView):
    model = MarketplaceItemPost
    template_name = "marketplace/marketplace_my_posts.html"
    context_object_name = "my_posts"
    ordering = "-created_on"

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

"""
1. `@method_decorator(login_required, name="dispatch")`:
   - This decorator is used to apply the `login_required` decorator to the `dispatch` method of the view.
   - `login_required` is a decorator provided by Django that ensures the user must be logged in to access the view.

2. `class MarketplaceMyPostsView(ListView):`:
   - This line defines a class named `MarketplaceMyPostsView` that inherits from the `ListView` class.
   - By inheriting from `ListView`, the `MarketplaceMyPostsView` class inherits the functionality and attributes 
   of the `ListView` class.

3. `model = MarketplaceItemPost`:
   - This line defines the model that the `MarketplaceMyPostsView` view will operate on.
   - The view will work with the `MarketplaceItemPost` model.

4. `template_name = "marketplace/marketplace_my_posts.html"`:
   - This line specifies the template that will be used to render the view.
   - The template is located at `marketplace/marketplace_my_posts.html`.

5. `context_object_name = "my_posts"`:
   - This line sets the context object name for the list of objects.
   - The list of objects will be available in the template context as `my_posts`.

6. `ordering = "-created_on"`:
   - This line specifies the ordering of the queryset.
   - The queryset will be ordered in descending order based on the `created_on` field of the 
   `MarketplaceItemPost` model.

7. `get_queryset(self)`:
   - This method is overridden to customize the queryset used to retrieve the list of objects.
   - It calls the `get_queryset` method of the parent class (`super()`) and applies an additional filter to only 
   include objects where the `author` field is equal to the current user (`self.request.user`).
"""


class MarketplaceUserMessagingView:
    pass

