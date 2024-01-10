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
Django URL Patterns Documentation

path('', PostListView.as_view(), name='post_list')
This URL pattern maps to the PostListView class-based view, representing the list of all posts.
The empty string '' as the path means it corresponds to the base URL of the application.
The PostListView.as_view() method is used to convert the class-based view into a view callable for URL patterns.
The name='post_list' attribute provides a unique identifier for this URL pattern, which can be used in templates or other parts of the application.
path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail')
This URL pattern maps to the PostDetailView class-based view, representing the detail view for a specific post.
The path includes post/ followed by an integer parameter (<int:pk>) representing the primary key of the post.
The PostDetailView.as_view() method converts the class-based view into a view callable for URL patterns.
The name='post_detail' attribute provides a unique identifier for this URL pattern.
path('post/new/', PostCreateView.as_view(), name='post_create')
This URL pattern maps to the PostCreateView class-based view, representing the view for creating a new post.
The path includes post/new/ to indicate the creation of a new post.
The PostCreateView.as_view() method converts the class-based view into a view callable for URL patterns.
The name='post_create' attribute provides a unique identifier for this URL pattern.
path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit')
This URL pattern maps to the PostUpdateView class-based view, representing the view for updating/editing an existing post.
The path includes post/<int:pk>/edit/ where <int:pk> is an integer parameter representing the primary key of the post to be edited.
The PostUpdateView.as_view() method converts the class-based view into a view callable for URL patterns.
The name='post_edit' attribute provides a unique identifier for this URL pattern.
path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete')
This URL pattern maps to the PostDeleteView class-based view, representing the view for deleting an existing post.
The path includes post/<int:pk>/delete/ where <int:pk> is an integer parameter representing the primary key of the post to be deleted.
The PostDeleteView.as_view() method converts the class-based view into a view callable for URL patterns.
The name='post_delete' attribute provides a unique identifier for this URL pattern."""




