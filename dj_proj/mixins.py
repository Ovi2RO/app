from django.contrib.auth.mixins import UserPassesTestMixin

class AuthorOrStaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        post = self.get_object()  # Assuming the post object is available in the view
        user = self.request.user
        return user.is_staff or post.author == user