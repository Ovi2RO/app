from django.urls import path
from .models import MarketplaceItemPost
from .views import (
    MarketplaceListView,
    MarketplaceDetailView,
    MarketplaceCreateView,
    MarketplaceDeleteView,
    MarketplaceUpdateView,
    MarketplaceSearchResultsView,
)


urlpatterns = [
    path("", MarketplaceListView.as_view(), name="marketplace_list"),
    path("detail_post/<int:pk>/", MarketplaceDetailView.as_view(), name="marketplace_detail"),
    path("create/", MarketplaceCreateView.as_view(), name="marketplace_create"),
    path("delete_post/<int:pk>/", MarketplaceDeleteView.as_view(), name="marketplace_delete"),
    path("update_post/<int:pk>/", MarketplaceUpdateView.as_view(), name="marketplace_update"),
    path("search_results", MarketplaceSearchResultsView.as_view(), name="marketplace_search"),    
]
