from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .models import Post, Comment


class PostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser', password='testpassword')

        Post.objects.create(author=user, title='Test Post 1', description='This is a test post 1')
        Post.objects.create(author=user, title='Test Post 2', description='This is a test post 2')
    """
    The `setUpTestData` class method is a special method that is called once to set up test data for the test 
    case. It creates a user and two `Post` objects tied to that user.
    """

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/parenting/', follow=True)
        self.assertEqual(response.status_code, 200)
    """
    The `test_view_url_exists_at_desired_location` method tests that the view URL exists at the desired location 
    ("/parenting/"). It makes a GET request to the URL and checks that the response status code is 200 (OK).
    """

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('post-list'), follow=True)
        self.assertEqual(response.status_code, 200)
    """
     The `test_view_url_accessible_by_name` method tests that the view URL is accessible by its name ("post-list"). 
     It uses the `reverse` function to get the URL based on its name and makes a GET request to that URL, checking 
     that the response status code is 200.
    """

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post-list'), follow=True)
        self.assertTemplateUsed(response, 'get_app/post_list.html')
    """
    The `test_view_uses_correct_template` method tests that the view uses the correct template 
    ("get_app/post_list.html"). It logs in the user, makes a GET request to the view URL, and checks that the 
    response uses the specified template.
    """

    def test_view_returns_queryset_filtered_by_search_words(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post-list'), {'search_words': 'Test Post 1'}, follow=True)
        self.assertContains(response, 'Test Post 1')
        self.assertNotContains(response, 'Test Post 3')
    """
     The `test_view_returns_queryset_filtered_by_search_words` method tests that the view returns a queryset 
     filtered by search words. It logs in the user, makes a GET request to the view URL with the search words 
     "Test Post 1" as a query parameter, and checks that the response contains the post with the title 
     "Test Post 1" and does not contain the post with the title "Test Post 3".
    """

    def test_view_returns_queryset_filtered_by_search_field(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post-list'), {'search_field': 'description', 'search_words': 'test post'})
        self.assertContains(response, 'Test Post 1')
        self.assertContains(response, 'Test Post 2')
    """
    The `test_view_returns_queryset_filtered_by_search_field` method tests that the view returns a queryset 
    filtered by search field and search words. It logs in the user, makes a GET request to the view URL with the 
    search field set to "description" and the search words set to "test post" as query parameters, and checks that 
    the response contains the posts with the titles "Test Post 1" and "Test Post 2".
    """

    def test_view_returns_queryset_filtered_by_search_date(self):
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post-list'), {'search_date': yesterday})
        self.assertContains(response, 'Test Post 1')
        self.assertContains(response, 'Test Post 2')
    """
    The `test_view_returns_queryset_filtered_by_search_date` method tests that the view returns a queryset 
    filtered by search date. It gets the current date using `datetime.now().date()` and calculates the date for 
    yesterday by subtracting `timedelta(days=1)` from the current date. It logs in the user, makes a GET request 
    to the view URL with the search date set to yesterday as a query parameter, and checks that the response 
    contains the posts with the titles "Test Post 1" and "Test Post 2".
    """

    def test_view_returns_all_queryset_when_no_filters_applied(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post-list'))
        self.assertContains(response, 'Test Post 1')
        self.assertContains(response, 'Test Post 2')
    """
    The `test_view_returns_all_queryset_when_no_filters_applied` method tests that the view returns the entire 
    queryset when no filters are applied. It logs in the user, makes a GET request to the view URL without any 
    query parameters, and checks that the response contains all the posts with titles "Test Post 1" and 
    "Test Post 2".
    """


class PostCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/parenting/create/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "get_app/post_create.html")
    """
    The `test_view_url_exists_at_desired_location` method tests that the view URL exists at the desired location 
    ("/parenting/create/"). It logs in the user, makes a GET request to the URL, and checks that the response 
    status code is 200 (OK).
    """

    def test_view_redirects_to_post_list_on_successful_creation(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse("post-create"), {
            "title": "Test Post",
            "description": "This is a test post"
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "get_app/post_list.html")
    """
    - The `test_view_redirects_to_post_list_on_successful_creation` method tests that the view redirects to the 
    post list on successful creation of a post.
    - The user is logged in using the `login` method with the provided username and password.
    - The `client.post` method is used to make a POST request to the `post-create` URL, which is obtained using 
    the `reverse` function. The request includes the necessary data for creating a post, such as the title and 
    description.
    - The `follow=True` argument is passed to the `client.post` method to follow any redirects that may occur.
    - The response object is then checked to ensure that the status code is 200 (OK) using the `assertEqual` method.
    - The `assertTemplateUsed` method is used to check that the response uses the specified template, 
    `get_app/post_list.html`.
    """

    def test_view_requires_authentication(self):
        response = self.client.get(reverse("post-create"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/signin_signup.html")
    """
    - The `test_view_requires_authentication` method tests that the view requires authentication to access.
    - The `client.get` method is used to make a GET request to the `post-create` URL, which is obtained using 
    the `reverse` function.
    - The `follow=True` argument is passed to the `client.get` method to follow any redirects that may occur.
    - The response object is then checked to ensure that the status code is 200 (OK) using the `assertEqual` method.
    - The `assertTemplateUsed` method is used to check that the response uses the specified template, 
    `account/signin_signup.html`.
    """


class PostUpdateViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.post = Post.objects.create(title='Test Post', description='This is a test post', author=cls.user)

    def test_view_updates_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            reverse('post-update', kwargs={'pk': self.post.pk}),
            {'title': 'Updated Post', 'description': 'This is an updated post'}
        )
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Post')
        self.assertEqual(self.post.description, 'This is an updated post')
    """
    - The `test_view_updates_post` method tests that the view updates the post. It logs in the user, makes a POST 
    request to the `post-update` URL, which is obtained using the `reverse` function and passing the post's 
    primary key as a keyword argument, and includes the updated data for the post in the request.
    - The response object is then checked to ensure that the status code is 302 (redirect) using the `assertEqual` 
    method.
    - The `refresh_from_db` method is called on the post object to refresh its data from the database.
    - The `assertEqual` method is used to check that the post's title and description have been updated as expected.
    """

    def test_view_redirects_to_post_detail(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            reverse('post-update', kwargs={'pk': self.post.pk}),
            {'title': 'Updated Post', 'description': 'This is an updated post'}
        )
        self.assertRedirects(response, reverse('post-detail', kwargs={'pk': self.post.pk}))
    """
    - The `test_view_redirects_to_post_detail` method tests that the view redirects to the post detail page after 
    updating a post.
    - The user is logged in using the `login` method with the provided username and password.
    - The `client.post` method is used to make a POST request to the `post-update` URL, which is obtained using 
    the `reverse` function and passing the post's primary key as a keyword argument. The request includes the 
    updated data for the post.
    - The response object is then checked to ensure that it redirects to the post detail page using the 
    `assertRedirects` method. The `reverse` function is used again to generate the URL for the post detail page, 
    passing the post's primary key as a keyword argument.
    """


class PostDeleteViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.post = Post.objects.create(title='Test Post', description='This is a test post', author=cls.user)

    def test_view_redirects_to_login_if_not_authenticated(self):
        response = self.client.get(reverse('post-delete', kwargs={'pk': self.post.pk}))
        self.assertRedirects(response, reverse('account_login') + '?next=' + reverse('post-delete', kwargs={'pk': self.post.pk}))
    """
    - The `test_view_redirects_to_login_if_not_authenticated` method tests that the view redirects to the login 
    page if the user is not authenticated. It makes a GET request to the `post-delete` URL, which is obtained 
    using the `reverse` function and passing the post's primary key as a keyword argument.
    - The response object is then checked to ensure that it redirects to the login page with the 'next' parameter 
    set to the `post-delete` URL using the `assertRedirects` method. The `reverse` function is used again to 
    generate the URL for the login page, and the `+` operator is used to concatenate it with the `post-delete` 
    URL and the 'next' parameter.
    """

    def test_view_returns_403_if_not_author_or_staff(self):
        user = User.objects.create_user(username='anotheruser', password='anotherpassword')
        self.client.login(username='anotheruser', password='anotherpassword')
        response = self.client.get(reverse('post-delete', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 403)
    """
    - The `test_view_returns_403_if_not_author_or_staff` method tests that the view returns a 403 Forbidden status 
    code if the user is not the author of the post or a staff member.
    - Another user is created using the `create_user` method of the `User` model. This user is not the author of 
    the post.
    - The `login` method of the `client` is used to log in as the another user.
    - A GET request is made to the `post-delete` URL with the post's primary key as a keyword argument.
    - The response object is then checked to ensure that the status code is 403 Forbidden using the `assertEqual` 
    method.
    """

    def test_view_deletes_post_if_author(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post-delete', kwargs={'pk': self.post.pk}))
        self.assertRedirects(response, reverse('post-list'))
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())
    """
    - The `test_view_deletes_post_if_author` method tests that the view deletes the post if the user is the author 
    of the post.
    - The `login` method of the `client` is used to log in as the author of the post.
    - A POST request is made to the `post-delete` URL with the post's primary key as a keyword argument.
    - The response object is then checked to ensure that it redirects to the `post-list` URL using the 
    `assertRedirects` method.
    - The `assertFalse` method is used to check that the post is deleted from the database by verifying that no 
    post with the same primary key exists.
    """

    def test_view_deletes_post_if_staff(self):
        user = User.objects.create_user(username='staffuser', password='staffpassword', is_staff=True)
        self.client.login(username='staffuser', password='staffpassword')
        response = self.client.post(reverse('post-delete', kwargs={'pk': self.post.pk}))
        self.assertRedirects(response, reverse('post-list'))
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())
    """
    - The `test_view_deletes_post_if_staff` method tests that the view deletes the post if the user is a staff 
    member.
    - A staff user is created using the `create_user` method of the `User` model. The `is_staff` flag is set to 
    `True` to indicate that the user is a staff member.
    - The `login` method of the `client` is used to log in as the staff user.
    - A POST request is made to the `post-delete` URL with the post's primary key as a keyword argument.
    - The response object is then checked to ensure that it redirects to the `post-list` URL using the 
    `assertRedirects` method.
    - The `assertFalse` method is used to check that the post is deleted from the database by verifying that no 
    post with the same primary key exists.
    """


class PostDetailViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.post = Post.objects.create(title='Test Post', description='This is a test post', author=cls.user)

    def test_view_returns_post_detail(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post-detail', kwargs={'pk': self.post.pk}), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'get_app/post_detail.html')
        self.assertEqual(response.context['post'], self.post)
    """
    - The `test_view_returns_post_detail` method tests that the view returns the post detail page with the correct 
    context.
    - The `login` method of the `client` is used to log in as the user.
    - A GET request is made to the `post-detail` URL with the post's primary key as a keyword argument.
    - The response object is then checked to ensure that the status code is 200 OK using the `assertEqual` method.
    - The `assertTemplateUsed` method is used to check that the correct template (`get_app/post_detail.html`) is 
    used.
    - The `assertEqual` method is used to check that the post object is passed in the context of the response.
    """

    def test_view_adds_comment_to_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post-detail', kwargs={'pk': self.post.pk}), {'content': 'New comment'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(self.post.comments.all()), 1)
        self.assertEqual(self.post.comments.first().content, 'New comment')
    """
    - The `test_view_adds_comment_to_post` method tests that the view adds a comment to the post.
    - The `login` method of the `client` is used to log in as the user.
    - A POST request is made to the `post-detail` URL with the post's primary key as a keyword argument and the 
    comment content as form data.
    - The response object is then checked to ensure that the status code is 302 (redirect) using the `assertEqual` 
    method.
    - The `len` function is used to check that the post has one comment by checking the length of the `comments` 
    queryset.
    - The `assertEqual` method is used to check that the comment content of the first comment in the `comments` 
    queryset is 'New comment'.
    """

    def test_view_deletes_comment(self):
        self.client.login(username='testuser', password='testpassword')
        comment = Comment.objects.create(post=self.post, content='Test comment', author=self.user)
        response = self.client.post(reverse('post-detail', kwargs={'pk': self.post.pk}), {'delete_comment_id': comment.id})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(id=comment.id).exists())
    """
    - The `test_view_deletes_comment` method tests that the view deletes a comment.
    - The `login` method of the `client` is used to log in as the user.
    - A comment is created for the post using the `Comment.objects.create` method.
    - A POST request is made to the `post-detail` URL with the post's primary key as a keyword argument and the 
    comment ID to delete as form data.
    - The response object is then checked to ensure that the status code is 302 (redirect) using the `assertEqual` 
    method.
    - The `Comment.objects.filter` method is used to check that the comment no longer exists in the database by 
    filtering for comments with the specified ID and checking if any results exist using the `exists` method.
    """

    def test_view_deletes_reply(self):
        self.client.login(username='testuser', password='testpassword')
        comment = Comment.objects.create(post=self.post, content='Test comment', author=self.user)
        reply = Comment.objects.create(post=self.post, content='Test reply', author=self.user, parent_comment=comment)
        response = self.client.post(reverse('post-detail', kwargs={'pk': self.post.pk}), {'delete_reply_id': reply.id})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(id=reply.id).exists())
    """
    - The `test_view_deletes_reply` method tests that the view deletes a reply.
    - The `login` method of the `client` is used to log in as the user.
    - A comment is created for the post using the `Comment.objects.create` method.
    - A reply to the comment is created using the `Comment.objects.create` method, with the `parent_comment` 
    parameter set to the comment object.
    - A POST request is made to the `post-detail` URL with the post's primary key as a keyword argument and the 
    reply ID to delete as form data.
    - The response object is then checked to ensure that the status code is 302 (redirect) using the `assertEqual` 
    method.
    - The `Comment.objects.filter` method is used to check that the reply no longer exists in the database by 
    filtering for comments with the specified ID and checking if any results exist using the `exists` method.
    """








