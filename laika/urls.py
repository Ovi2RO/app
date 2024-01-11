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