from django.contrib.auth.mixins import UserPassesTestMixin

class AuthorOrStaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        post = self.get_object()
        user = self.request.user
        return user.is_staff or post.author == user


"""
The `AuthorOrStaffRequiredMixin` is a custom mixin that inherits from the `UserPassesTestMixin` class 
provided by Django's `django.contrib.auth.mixins` module. 

This mixin is used to enforce a test condition before allowing access to a view. In this case, the 
`test_func` method is overridden to define the test condition. 

The `test_func` method checks if the logged-in user is a staff member (`user.is_staff`) or if the logged-in 
user is the author of the post (`post.author == user`). If either of these conditions is true, the test 
passes and the user is granted access to the view. 
"""
