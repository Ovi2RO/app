from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    # there should be another field here that gets the post the room was created from
    # optionally the slug should be traded off for this post - instead of using the slug
    # it would use the post name/number/app in the url itself

    # room instantiation would occur from other apps
    # need to figure out how to block access to said room to the users that aren't supposed to be in the chat


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date_added",)
