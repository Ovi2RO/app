from django.urls import path
from .views import (ParentingAPIView, 
                    LaikaAPIView, 
                    MarketplaceAPIView, 
                    TennisAPIView,
                    ParentingDetailAPIView,
                    LaikaDetailAPIView,
                    MarketplaceDetailAPIView,
                    TennisDetailAPIView)

urlpatterns = [
    path('parenting/', ParentingAPIView.as_view(), name='parenting-api'),
    path('laika/', LaikaAPIView.as_view(), name='laika-api'),
    path('marketplace/', MarketplaceAPIView.as_view(), name='marketplace-api'),
    path('tennis/', TennisAPIView.as_view(), name='tennis-api'),
    path('parenting/<int:pk>/', ParentingDetailAPIView.as_view(), name='parenting-detail-api'),
    path('laika/<int:pk>/', LaikaDetailAPIView.as_view(), name='laika-detail-api'),
    path('marketplace/<int:pk>/', MarketplaceDetailAPIView.as_view(), name='marketplace-detail-api'),
    path('tennis/<int:pk>/', TennisDetailAPIView.as_view(), name='tennis-detail-api'),
]



