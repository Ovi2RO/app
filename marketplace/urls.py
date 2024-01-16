from django.urls import path
from .models import MarketplaceItemPost
from .views import (
    MarketplaceListView,
    MarketplaceDetailView,
    MarketplaceCreateView,
    MarketplaceDeleteView,
    MarketplaceUpdateView,
    MarketplaceSearchResultsView,
    MarketplaceMyPostsView,
)


urlpatterns = [
    path("", MarketplaceListView.as_view(), name="marketplace_list"),
    path("detail_post/<int:pk>/", MarketplaceDetailView.as_view(), name="marketplace_detail"),
    path("create/", MarketplaceCreateView.as_view(), name="marketplace_create"),
    path("delete_post/<int:pk>/", MarketplaceDeleteView.as_view(), name="marketplace_delete"),
    path("update_post/<int:pk>/", MarketplaceUpdateView.as_view(), name="marketplace_update"),
    path("search_results", MarketplaceSearchResultsView.as_view(), name="marketplace_search"),
    path("my_posts/<str:username>/", MarketplaceMyPostsView.as_view(), name="marketplace_my_posts"),
]

"""
1. `path("", MarketplaceListView.as_view(), name="marketplace_list")`:
   - URL pattern: an empty string, representing the root URL.
   - View: `MarketplaceListView.as_view()`, which is the view class that will be called when this URL is accessed.
   - Name: "marketplace_list", the name used to refer to this URL pattern in other parts of the code.

2. `path("detail_post//", MarketplaceDetailView.as_view(), name="marketplace_detail")`:
   - URL pattern: "detail_post//", where `` is a URL parameter representing an integer value.
   - View: `MarketplaceDetailView.as_view()`, the view class that will handle this URL pattern.
   - Name: "marketplace_detail", the name used to reference this URL pattern.

3. `path("create/", MarketplaceCreateView.as_view(), name="marketplace_create")`:
   - URL pattern: "create/".
   - View: `MarketplaceCreateView.as_view()`.
   - Name: "marketplace_create".

4. `path("delete_post//", MarketplaceDeleteView.as_view(), name="marketplace_delete")`:
   - URL pattern: "delete_post//", where `` represents an integer value.
   - View: `MarketplaceDeleteView.as_view()`.
   - Name: "marketplace_delete".

5. `path("update_post//", MarketplaceUpdateView.as_view(), name="marketplace_update")`:
   - URL pattern: "update_post//", where `` represents an integer value.
   - View: `MarketplaceUpdateView.as_view()`.
   - Name: "marketplace_update".

6. `path("search_results", MarketplaceSearchResultsView.as_view(), name="marketplace_search")`:
   - URL pattern: "search_results".
   - View: `MarketplaceSearchResultsView.as_view()`.
   - Name: "marketplace_search".

7. `path("my_posts//", MarketplaceMyPostsView.as_view(), name="marketplace_my_posts")`:
   - URL pattern: "my_posts//", where `` represents a string value.
   - View: `MarketplaceMyPostsView.as_view()`.
   - Name: "marketplace_my_posts".
"""
