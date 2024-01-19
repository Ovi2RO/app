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

