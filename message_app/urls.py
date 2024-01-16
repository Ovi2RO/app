from django.urls import path

urlpatterns = [
    path("", MessageInboxView.as_view(), name="message_inbox"),
    path("topic/<str:app_name>/<str:post_name>/", MessageConvoView.as_view(), name="message_conversation"),

]

# there should be a page in which you can select which conversation to open
# then you should be redirected to a page that has all the messages regarding
# said conversation

# each conversation should be associated to a post, so that it's easier to organize