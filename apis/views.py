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
"""
- The `ParentingAPIView` class is a view class that inherits from `generics.ListAPIView`, which provides a 
read-only endpoint for retrieving a list of objects.
- The `queryset` attribute is set to `Post.objects.all()`, which specifies the queryset of `Post` objects that 
will be returned by the view.
- The `serializer_class` attribute is set to `ParentingSerializer`, which specifies the serializer class that 
will be used to serialize the `Post` objects.
"""


class LaikaAPIView(generics.ListAPIView):
    queryset = LaikaPost.objects.all()
    serializer_class = LaikaSerializer
"""
- The `LaikaAPIView` class is a view class that inherits from `generics.ListAPIView`, which provides a read-only 
endpoint for retrieving a list of objects.
- The `queryset` attribute is set to `LaikaPost.objects.all()`, which specifies the queryset of `LaikaPost` 
objects that will be returned by the view.
- The `serializer_class` attribute is set to `LaikaSerializer`, which specifies the serializer class that will 
be used to serialize the `LaikaPost` objects.
"""


class MarketplaceAPIView(generics.ListAPIView):
    queryset = MarketplaceItemPost.objects.all()
    serializer_class = MarketplaceSerializer
"""
- The `MarketplaceAPIView` class is a view class that inherits from `generics.ListAPIView`, which provides a 
read-only endpoint for retrieving a list of objects.
- The `queryset` attribute is set to `MarketplaceItemPost.objects.all()`, which specifies the queryset of 
`MarketplaceItemPost` objects that will be returned by the view.
- The `serializer_class` attribute is set to `MarketplaceSerializer`, which specifies the serializer class that 
will be used to serialize the `MarketplaceItemPost` objects.
"""


class TennisAPIView(generics.ListAPIView):
    queryset = TennisPost.objects.all()
    serializer_class = TennisSerializer
"""
- The `TennisAPIView` class is a view class that inherits from `generics.ListAPIView`, which provides a read-only 
endpoint for retrieving a list of objects.
- The `queryset` attribute is set to `TennisPost.objects.all()`, which specifies the queryset of `TennisPost` 
objects that will be returned by the view.
- The `serializer_class` attribute is set to `TennisSerializer`, which specifies the serializer class that will 
be used to serialize the `TennisPost` objects.
"""


class ParentingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = ParentingSerializer
"""
- The `ParentingDetailAPIView` class is a view class that inherits from `generics.RetrieveUpdateDestroyAPIView`, 
which provides a read, update, and delete endpoint for a single object.
- The `queryset` attribute is set to `Post.objects.all()`, which specifies the queryset of `Post` objects that 
will be used to retrieve the single object.
- The `serializer_class` attribute is set to `ParentingSerializer`, which specifies the serializer class that 
will be used to serialize the `Post` objects.
"""


class LaikaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LaikaPost.objects.all()
    serializer_class = LaikaSerializer
"""
- The `LaikaDetailAPIView` class is a view class that inherits from `generics.RetrieveUpdateDestroyAPIView`, 
which provides a read, update, and delete endpoint for a single object.
- The `queryset` attribute is set to `LaikaPost.objects.all()`, which specifies the queryset of `LaikaPost` 
objects that will be used to retrieve the single object.
- The `serializer_class` attribute is set to `LaikaSerializer`, which specifies the serializer class that will 
be used to serialize the `LaikaPost` objects.
"""


class MarketplaceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarketplaceItemPost.objects.all()
    serializer_class = MarketplaceSerializer
"""
- The `MarketplaceDetailAPIView` class is a view class that inherits from `generics.RetrieveUpdateDestroyAPIView`, 
which provides a read, update, and delete endpoint for a single object.
- The `queryset` attribute is set to `MarketplaceItemPost.objects.all()`, which specifies the queryset of 
`MarketplaceItemPost` objects that will be used to retrieve the single object.
- The `serializer_class` attribute is set to `MarketplaceSerializer`, which specifies the serializer class that 
will be used to serialize the `MarketplaceItemPost` objects.
"""


class TennisDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TennisPost.objects.all()
    serializer_class = TennisSerializer
"""
- The `TennisDetailAPIView` class is a view class that inherits from `generics.RetrieveUpdateDestroyAPIView`, 
which provides a read, update, and delete endpoint for a single object.
- The `queryset` attribute is set to `TennisPost.objects.all()`, which specifies the queryset of `TennisPost` 
objects that will be used to retrieve the single object.
- The `serializer_class` attribute is set to `TennisSerializer`, which specifies the serializer class that will 
be used to serialize the `TennisPost` objects.
"""
