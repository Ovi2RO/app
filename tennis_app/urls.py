from django.urls import path
from tennis_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    #path('',views.HomeView.as_view(),name='home-view'),
    path('',views.PostListView.as_view(), name='tennis-post-list'),
    path('create/',views.PostCreateView.as_view(), name='tennis-post-create'),
    path('<int:pk>/update/',views.PostUpdateView.as_view(), name='tennis-post-update'),
    path('<int:pk>/delete/',views.PostDeleteView.as_view(),name='tennis-post-delete'),
    path('<int:pk>/detail/',views.PostDetailView.as_view(),name='tennis-post-detail'),
    #path('search/',views.PostSearchView.as_view(),name='post-search')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)