from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDetailView, PostDeleteView, LaikaProfileView


urlpatterns = [
    
    path('', PostListView.as_view(), name='laika-post-list'),
    path('create/', PostCreateView.as_view(), name='laika-post-create'),
    path('<int:pk>/', PostDetailView.as_view(), name = 'laika-post-detail'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name = 'laika-post-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name = 'laika-post-delete'),
    path('profile/', LaikaProfileView.as_view(), name = 'laika-profile'), 
]

"""

- `from django.urls import path` imports the `path` function from the `django.urls` module. This function is used 
to define URL patterns for your Django application.

- `from .views import PostListView, PostCreateView, PostUpdateView, PostDetailView, PostDeleteView, 
LaikaProfileView` imports the necessary view classes from the `views` module of the current package. These views 
handle different actions related to posts and user profiles in the Laika application.

- `urlpatterns` is a list of URL patterns for the Laika application. Each pattern is defined using the `path` 
function.

Breakdown for each URL pattern:

- `path('', PostListView.as_view(), name='laika-post-list')` maps the root URL (`/`) to the `PostListView` view 
class. The `as_view()` method is used to convert the view class into a callable view function. The `name` 
parameter assigns a unique name to this URL pattern, which can be used to refer to it in other parts of the code.

- `path('create/', PostCreateView.as_view(), name='laika-post-create')` maps the `/create/` URL to the 
`PostCreateView` view class. This view is responsible for creating new posts.

- `path('/', PostDetailView.as_view(), name='laika-post-detail')` maps URLs with an integer parameter (``) to the 
`PostDetailView` view class. This view is responsible for displaying the details of a specific post based on its 
primary key (`pk`).

- `path('/update/', PostUpdateView.as_view(), name='laika-post-update')` maps URLs with an integer parameter (``) 
followed by `/update/` to the `PostUpdateView` view class. This view is responsible for updating the details of a 
specific post.

- `path('/delete/', PostDeleteView.as_view(), name='laika-post-delete')` maps URLs with an integer parameter (``) 
followed by `/delete/` to the `PostDeleteView` view class. This view is responsible for deleting a specific post.

- `path('profile/', LaikaProfileView.as_view(), name='laika-profile')` maps the `/profile/` URL to the 
`LaikaProfileView` view class. This view is responsible for displaying the profile page of the current user.

By defining these URL patterns, you can map different URLs to the corresponding views in your Django application. 
This allows users to access different pages and perform various actions, such as creating, viewing, updating, and 
deleting posts, as well as viewing their profiles.
"""