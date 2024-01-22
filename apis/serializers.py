from rest_framework import serializers
from get_app.models import Post
from laika.models import Post as LaikaPost
from marketplace.models import MarketplaceItemPost
from tennis_app.models import Posts as TennisPost


class ParentingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id',
                  'author', 
                  'title', 
                  'description', 
                  'created_at', 
                  'updated_at', 
                  'image')
"""
- The `ParentingSerializer` class is a serializer class that inherits from `serializers.ModelSerializer`.
- The `Meta` inner class is used to specify the metadata for the serializer.
- The `model` attribute is set to the `Post` model, indicating that this serializer will be used for serializing 
and deserializing `Post` objects.
- The `fields` attribute is a tuple that specifies the fields that should be included in the serialized 
representation of a `Post` object. These fields include `id`, `author`, `title`, `description`, `created_at`, 
`updated_at`, and `image`.
"""


class LaikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaikaPost
        fields = ('id',
                  'author', 
                  'image', 
                  'title', 
                  'description', 
                  'created_at', 
                  'updated_at')
"""
- The `LaikaSerializer` class is a serializer class that inherits from `serializers.ModelSerializer`.
- The `Meta` inner class is used to specify the metadata for the serializer.
- The `model` attribute is set to the `LaikaPost` model, indicating that this serializer will be used for 
serializing and deserializing `LaikaPost` objects.
- The `fields` attribute is a tuple that specifies the fields that should be included in the serialized 
representation of a `LaikaPost` object. These fields include `id`, `author`, `image`, `title`, `description`, 
`created_at`, and `updated_at`.
"""


class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketplaceItemPost
        fields = ('id',
                  'author', 
                  'created_on', 
                  'updated_on', 
                  'title', 
                  'description', 
                  'price', 
                  'location', 
                  'category', 
                  'image')
"""
- The `MarketplaceSerializer` class is a serializer class that inherits from `serializers.ModelSerializer`.
- The `Meta` inner class is used to specify the metadata for the serializer.
- The `model` attribute is set to the `MarketplaceItemPost` model, indicating that this serializer will be used 
for serializing and deserializing `MarketplaceItemPost` objects.
- The `fields` attribute is a tuple that specifies the fields that should be included in the serialized 
representation of a `MarketplaceItemPost` object. These fields include `id`, `author`, `created_on`, `updated_on`, 
`title`, `description`, `price`, `location`, `category`, and `image`.
"""


class TennisSerializer(serializers.ModelSerializer):
    class Meta:
        model = TennisPost
        fields = ('id',
                  'user_name', 
                  'user_last', 
                  'user_email', 
                  'user_gender', 
                  'birth_date', 
                  'phone', 
                  'description', 
                  'current_date', 
                  'play_date',
                  'image',
                  'level',
                  'language',
                  'type',
                  'club_name',
                  'author')
"""
- The `TennisSerializer` class is a serializer class that inherits from `serializers.ModelSerializer`.
- The `Meta` inner class is used to specify the metadata for the serializer.
- The `model` attribute is set to the `TennisPost` model, indicating that this serializer will be used for 
serializing and deserializing `TennisPost` objects.
- The `fields` attribute is a tuple that specifies the fields that should be included in the serialized 
representation of a `TennisPost` object. These fields include `id`, `user_name`, `user_last`, `user_email`, 
`user_gender`, `birth_date`, `phone`, `description`, `current_date`, `play_date`, `image`, `level`, `language`, 
`type`, `club_name`, and `author`.
"""
