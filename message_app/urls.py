from django.urls import path, include
from .views import MessageAppChatView, MessageAppInboxView

urlpatterns = [
    path("", MessageAppInboxView.as_view(), name="message_inbox"),
    path("chat/", MessageAppChatView, name="message_chat"),
]
# "topic/<str:app_name>/<str:post_name>/" - this should be the url name


# there should be a page in which you can select which conversation to open
# then you should be redirected to a page that has all the messages regarding
# said conversation

# each conversation should be associated to a post, so that it's easier to organize
