from django.urls import path
from tennis_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('',views.PostListView.as_view(), name='tennis-post-list'),
    path('create/',views.PostCreateView.as_view(), name='tennis-post-create'),
    path('<int:pk>/update/',views.PostUpdateView.as_view(), name='tennis-post-update'),
    path('<int:pk>/delete/',views.PostDeleteView.as_view(),name='tennis-post-delete'),
    path('<int:pk>/detail/',views.PostDetailView.as_view(),name='tennis-post-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
1. `path('', views.PostListView.as_view(), name='tennis-post-list')`: This pattern maps the root URL to the 
`PostListView` view class, which is responsible for displaying a list of posts. The name of this URL pattern is 
'tennis-post-list'.

2. `path('create/', views.PostCreateView.as_view(), name='tennis-post-create')`: This pattern maps the URL with 
'create/' appended to the root URL to the `PostCreateView` view class, which handles the creation of new posts. 
The name of this URL pattern is 'tennis-post-create'.

3. `path('<int:pk>/update/', views.PostUpdateView.as_view(), name='tennis-post-update')`: This pattern captures an 
integer parameter (`<int:pk>`) from the URL and maps it to the `PostUpdateView` view class. This view is 
responsible for updating an existing post. The name of this URL pattern is 'tennis-post-update'.

4. `path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='tennis-post-delete')`: This pattern captures an 
integer parameter (`<int:pk>`) from the URL and maps it to the `PostDeleteView` view class. This view handles the 
deletion of a post. The name of this URL pattern is 'tennis-post-delete'.

5. `path('<int:pk>/detail/', views.PostDetailView.as_view(), name='tennis-post-detail')`: This pattern captures an 
integer parameter (`<int:pk>`) from the URL and maps it to the `PostDetailView` view class. This view displays the 
details of a specific post. The name of this URL pattern is 'tennis-post-detail'.

Additionally, the code checks if the project is in debug mode (`settings.DEBUG`) and, if so, adds a URL pattern to 
serve media files (`static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`).
"""