from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path("",PostListView.as_view(), name="post-list"),
    path('<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path("create/", PostCreateView.as_view(), name="post-create"),
    path('<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),    
] 

"""
- `path()` is a function from `django.urls` module that is used to define a URL pattern.

- `""` represents the root URL.

- `'<int:pk>/'` represents a URL pattern with a variable `pk` that expects an integer value.

- `"create/"` represents a URL pattern with the string "create".

- `PostListView.as_view()` is a class-based view that will be used to handle the request for the 
URL pattern. `PostListView` is the view class that will be used, and `.as_view()` method is called 
to convert the class-based view into a callable view.

- `name` is an optional parameter that provides a unique name for the URL pattern. It can be used to 
refer to the URL pattern in other parts of the Django application.
"""




