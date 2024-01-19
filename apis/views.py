from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from get_app.models import Post
from laika.models import Post as LaikaPost
from marketplace.models import MarketplaceItemPost
from tennis_app.models import Posts as TennisPost
from .serializers import ParentingSerializer, LaikaSerializer, MarketplaceSerializer, TennisSerializer


class ParentingAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = ParentingSerializer


class LaikaAPIView(generics.ListAPIView):
    queryset = LaikaPost.objects.all()
    serializer_class = LaikaSerializer


class MarketplaceAPIView(generics.ListAPIView):
    queryset = MarketplaceItemPost.objects.all()
    serializer_class = MarketplaceSerializer


class TennisAPIView(generics.ListAPIView):
    queryset = TennisPost.objects.all()
    serializer_class = TennisSerializer


class ParentingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = ParentingSerializer


class LaikaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LaikaPost.objects.all()
    serializer_class = LaikaSerializer


class MarketplaceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarketplaceItemPost.objects.all()
    serializer_class = MarketplaceSerializer


class TennisDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TennisPost.objects.all()
    serializer_class = TennisSerializer

