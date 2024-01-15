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

# Create your views here.


@method_decorator(login_required, name="dispatch")
class MarketplaceListView(ListView):
    model = MarketplaceItemPost
    template_name = "marketplace/marketplace_list.html"
    context_object_name = "marketposts"
    ordering = "-created_on"


@method_decorator(login_required, name="dispatch")
class MarketplaceDetailView(DetailView):
    model = MarketplaceItemPost
    template_name = "marketplace/marketplace_detail.html"
    context_object_name = "marketpost"


@method_decorator(login_required, name="dispatch")
class MarketplaceCreateView(CreateView):
    model = MarketplaceItemPost
    form_class = CreateMarketplacePostForm
    template_name = "marketplace/marketplace_create.html"
    success_url = "/marketplace/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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


@method_decorator(login_required, name="dispatch")
class MarketplaceDeleteView(AuthorOrStaffRequiredMixin, DeleteView):
    model = MarketplaceItemPost
    template_name = "marketplace/marketplace_delete.html"
    success_url = "/marketplace/"


@method_decorator(login_required, name="dispatch")
class MarketplaceSearchResultsView(ListView):
    model = MarketplaceItemPost
    template_name = "marketplace/marketplace_search_results.html"
    context_object_name = "posts"

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        posts = super().get_queryset()

        if form.is_valid():
            # need the clean form data
            title = form.cleaned_data.get("title")
            user = form.cleaned_data.get("user")
            category = form.cleaned_data.get("category")
            min_price = form.cleaned_data.get("min_price")
            max_price = form.cleaned_data.get("max_price")
            location = form.cleaned_data.get("location")
            init_post_date = form.cleaned_data.get("init_post_date")
            final_post_date = form.cleaned_data.get("final_post_date")

            # now we filter

            posts = MarketplaceItemPost.objects.all()

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


@method_decorator(login_required, name="dispatch")
class MarketplaceMyPostsView(ListView):
    model = MarketplaceItemPost
    template_name = "marketplace/marketplace_my_posts.html"
    context_object_name = "my_posts"
    ordering = "-created_on"

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


class MarketplaceUserMessagingView:
    pass
