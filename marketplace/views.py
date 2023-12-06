from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .models import MarketplaceItemPost
from .forms import CreateMarketplacePostForm

# Create your views here.


class MarketplaceListView(ListView):
    model = MarketplaceItemPost
    template_name = "marketplace/marketplace_list.html"
    context_object_name = "marketposts"


class MarketplaceDetailView(DetailView):
    model = MarketplaceItemPost
    template_name = "marketplace/marketplace_detail.html"
    context_object_name = "marketpost"


class MarketplaceCreateView(CreateView):
    model = MarketplaceItemPost
    form_class = CreateMarketplacePostForm
    template_name = "marketplace/marketplace_create.html"
    success_url = "/marketplace/"


class MarketplaceUpdateView(UpdateView):
    model = MarketplaceItemPost
    template_name = "marketplace/marketplace_update.html"
    fields = [
        "title",
        "description",
        "price",
        "location",
        "category",
        # "image",
    ]
    success_url = "/marketplace/"


class MarketplaceDeleteView(DeleteView):
    model = MarketplaceItemPost
    template_name = "marketplace/marketplace_delete.html"
    success_url = "/marketplace/"
