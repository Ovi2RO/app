import re
from typing import Any
from urllib import request
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
)
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import MarketplaceItemPost
from .forms import CreateMarketplacePostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from dj_proj.mixins import AuthorOrStaffRequiredMixin

# Create your views here.


@method_decorator(login_required, name="dispatch")
class MarketplaceListView(ListView):
    model = MarketplaceItemPost
    template_name = "marketplace/marketplace_list.html"
    context_object_name = "marketposts"


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

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     print(form)

    #     if "image" in request.POST:
    #         form.files["add_image"] = request.POST["image"]
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)


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
