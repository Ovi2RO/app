from django.urls import path
from .views import TestPostListView, TestPostDetailView, TestPostCreateView, TestPostUpdateView, TestPostDeleteView

urlpatterns = [
    path('', TestPostListView.as_view(), name='test-post-list'),
    path('<int:pk>/', TestPostDetailView.as_view(), name='test-post-detail'),
    path('create/', TestPostCreateView.as_view(), name='test-post-create'),
    path('<int:pk>/edit/', TestPostUpdateView.as_view(), name='test-post-edit'),
    path('<int:pk>/delete/', TestPostDeleteView.as_view(), name='test-post-delete'),

]


