from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import get_user_model


class AuthorOrModeratorMixin(UserPassesTestMixin):
    # problem with this method is that the buttons still show up but then the user
    # isn't allowed to delete or modify the post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_moderator
