from django.contrib.auth.models import User
from django.db import models

from marketplace.models import MarketplaceItemPost
from laika.models import Post as LaikaPost
from tennis_app.models import Posts as TennisPost
from get_app.models import Post as ParentPost
from django.urls import reverse


# Create your models here.
class Room(models.Model):
    # name = models.CharField(max_length=255)
    # slug = models.SlugField(unique=True)

    chat_initiator = models.ForeignKey(
        User, related_name="chat_initiator", on_delete=models.CASCADE
    )
    post_author = models.ForeignKey(
        User, related_name="post_author", on_delete=models.CASCADE
    )

    # there should be another field here that gets the post the room was created from
    # optionally the slug should be traded off for this post - instead of using the slug
    # it would use the post name/number/app in the url itself

    # room instantiation would occur from other apps
    # need to figure out how to block access to said room to the users that aren't supposed to be in the chat
    market_post = models.ForeignKey(MarketplaceItemPost, null=True)
    laika_post = models.ForeignKey(LaikaPost, null=True)
    tennis_post = models.ForeignKey(TennisPost, null=True)
    parent_post = models.ForeignKey(ParentPost, null=True)

    def get_absolute_url(self):
        return reverse("room", kwargs={"pk": self.pk})


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date_added",)
