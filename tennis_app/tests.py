from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from tennis_app.models import Posts


class PostListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Posts.objects.create(
            user_name='John',
            user_last='Doe',
            user_email='johndoe@example.com',
            user_gender='M',
            birth_date='1990-01-01',
            phone='123456789',
            description='Lorem ipsum dolor sit amet',
            current_date='2021-01-01',
            play_date='2021-01-02 10:00:00',
            level='3',
            language='1',
            type='Singles',
            club_name='Tennis Club',
            author=self.user,
        )
    """
    The `setUp` method is used to set up the test data before each test method is run. It creates a test user 
    and a test post.
    """

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('tennis-post-list'), follow=True)
        self.assertEqual(response.status_code, 200)
    """
    - The `test_view_url_accessible_by_name` method tests that the URL for the tennis post list view is accessible 
    by its name.
    - A GET request is made to the tennis post list view using the `client.get` method and the `reverse` function 
    with the URL pattern name `tennis-post-list`.
    - The `follow=True` parameter is used to follow any redirects that may occur.
    - The `assertEqual` method is used to check that the response status code is 200 (OK).
    """

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('tennis-post-list'))
        self.assertTemplateUsed(response, 'tennis/post_search.html')
    """
    - The `test_view_uses_correct_template` method tests that the tennis post list view uses the correct template.
    - The test user is logged in using the `login` method of the client.
    - A GET request is made to the tennis post list view using the `client.get` method and the `reverse` 
    function with the URL pattern name `tennis-post-list`.
    - The `assertTemplateUsed` method is used to check that the correct template ('tennis/post_search.html') is 
    used for rendering the response.
    """

    def test_view_lists_empty(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('tennis-post-list'), follow=True)
        self.assertNotContains(response, self.post.user_name)
        self.assertNotContains(response, self.post.user_last)
    """
    - The `test_view_lists_empty` method tests that the tennis post list view does not list any posts when there 
    are no posts in the database.
    - The test user is logged in using the `login` method of the client.
    - A GET request is made to the tennis post list view using the `client.get` method and the `reverse` function 
    with the URL pattern name `tennis-post-list`.
    - The `assertNotContains` method is used to check that the response does not contain the user's name and last 
    name.
    """

    def test_view_requires_login(self):
        response = self.client.get(reverse('tennis-post-list'))
        self.assertEqual(response.status_code, 302)
    """
    - The `test_view_requires_login` method tests that the tennis post list view requires login.
    - A GET request is made to the tennis post list view using the `client.get` method and the `reverse` 
    function with the URL pattern name `tennis-post-list`.
    - The `assertEqual` method is used to check that the response status code is 302, which indicates a redirect 
    to the login page.
    """


class PostCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('tennis-post-create')
        self.post = Posts.objects.create(
            user_name='John',
            user_last='Doe',
            user_email='johndoe@example.com',
            user_gender='M',
            birth_date='1990-01-01',
            phone='123456789',
            description='Lorem ipsum dolor sit amet',
            current_date='2021-01-01',
            play_date='2021-01-02 10:00:00',
            level='3',
            language='1',
            type='Singles',
            club_name='Tennis Club',
            author=self.user,
        )

    def test_view_requires_login(self):
        self.client.logout()
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/signin_signup.html")
    """
    - The `test_view_requires_login` method tests that the view requires login and redirects to the login page 
    if the user is not authenticated.
    - The current user is logged out using the `logout` method of the client.
    - A GET request is made to the view's URL using the `client.get` method with the `follow=True` parameter to 
    follow any redirects.
    - The `assertEqual` method is used to check that the response status code is 200, indicating a successful 
    response.
    - The `assertTemplateUsed` method is used to check that the correct template ('account/signin_signup.html') 
    is used for rendering the response.
    """


class PostDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('tennis-post-create')
        self.post = Posts.objects.create(
            user_name='John',
            user_last='Doe',
            user_email='johndoe@example.com',
            user_gender='M',
            birth_date='1990-01-01',
            phone='123456789',
            description='Lorem ipsum dolor sit amet',
            current_date='2021-01-01',
            play_date='2021-01-02 10:00:00',
            level='3',
            language='1',
            type='Singles',
            club_name='Tennis Club',
            author=self.user,
        ) 
    
    def test_view_renders_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('tennis-post-detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tennis/post_detail.html')
    """
    - The `test_view_renders_template` method tests that the tennis post detail view renders the correct template.
    - The test user is logged in using the `login` method of the client.
    - A GET request is made to the tennis post detail view using the `client.get` method and the `reverse` 
    function with the URL pattern name `tennis-post-detail` and the post's primary key as an argument.
    - The `assertEqual` method is used to check that the response status code is 200, indicating a successful 
    response.
    - The `assertTemplateUsed` method is used to check that the correct template ('tennis/post_detail.html') is 
    used for rendering the response.
    """

    def test_view_displays_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('tennis-post-detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'], self.post)
    """
    - The `test_view_displays_post` method tests that the tennis post detail view correctly displays the expected 
    post.
    - The test user is logged in using the `login` method of the client.
    - A GET request is made to the tennis post detail view using the `client.get` method and the `reverse` 
    function with the URL pattern name `tennis-post-detail` and the post's primary key as an argument.
    - The `assertEqual` method is used to check that the response status code is 200, indicating a successful 
    response.
    - The `assertEqual` method is used again to check that the `post` object in the view's context is equal to 
    the expected `self.post` object.
    """

    def test_view_displays_404_for_invalid_post_id(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('tennis-post-detail', args=[999]))
        self.assertEqual(response.status_code, 404)
    """
    - The `test_view_displays_404_for_invalid_post_id` method tests that the tennis post detail view returns a 
    404 status code for an invalid post ID.
    - The test user is logged in using the `login` method of the client.
    - A GET request is made to the tennis post detail view using the `client.get` method and the `reverse` 
    function with the URL pattern name `tennis-post-detail` and an invalid post ID (999) as an argument.
    - The `assertEqual` method is used to check that the response status code is 404, indicating that the post 
    was not found.
    """


class PostUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('tennis-post-create')
        self.post = Posts.objects.create(
            user_name='John',
            user_last='Doe',
            user_email='johndoe@example.com',
            user_gender='M',
            birth_date='1990-01-01',
            phone='123456789',
            description='Lorem ipsum dolor sit amet',
            current_date='2021-01-01',
            play_date='2021-01-02 10:00:00',
            level='3',
            language='1',
            type='Singles',
            club_name='Tennis Club',
            author=self.user,
        ) 
    
    def test_view_renders_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('tennis-post-update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tennis/post_update.html')
    """
    - The `test_view_renders_template` method tests that the tennis post update view renders the correct template.
    - The test user is logged in using the `login` method of the client.
    - A GET request is made to the tennis post update view using the `client.get` method and the `reverse` 
    function with the URL pattern name `tennis-post-update` and the post's primary key as an argument.
    - The `assertEqual` method is used to check that the response status code is 200, indicating a successful 
    response.
    - The `assertTemplateUsed` method is used to check that the correct template ('tennis/post_update.html') is 
    used for rendering the response.
    """

    def test_view_displays_post_form(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('tennis-post-update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertIsNotNone(form)
        self.assertEqual(form.initial['description'], 'Lorem ipsum dolor sit amet')
    """
    - The `test_view_displays_post_form` method tests that the tennis post update view displays the post form 
    with the correct initial data.
    - The test user is logged in using the `login` method of the client.
    - A GET request is made to the tennis post update view using the `client.get` method and the `reverse` 
    function with the URL pattern name `tennis-post-update` and the post's primary key as an argument.
    - The `assertEqual` method is used to check that the response status code is 200, indicating a successful 
    response.
    - The form object is extracted from the view's context using `response.context['form']`.
    - The `assertIsNotNone` method is used to check that the form object is not None.
    - The `assertEqual` method is used to check that the initial value of the `description` field in the form 
    matches the expected value ('Lorem ipsum dolor sit amet').
    """


class PostDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('tennis-post-create')
        self.post = Posts.objects.create(
            user_name='John',
            user_last='Doe',
            user_email='johndoe@example.com',
            user_gender='M',
            birth_date='1990-01-01',
            phone='123456789',
            description='Lorem ipsum dolor sit amet',
            current_date='2021-01-01',
            play_date='2021-01-02 10:00:00',
            level='3',
            language='1',
            type='Singles',
            club_name='Tennis Club',
            author=self.user,
        ) 
    
    def test_view_renders_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('tennis-post-delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tennis/post_delete.html')
    """
    - The `test_view_renders_template` method tests that the tennis post delete view renders the correct template.
    - The test user is logged in using the `login` method of the client.
    - A GET request is made to the tennis post delete view using the `client.get` method and the `reverse` 
    function with the URL pattern name `tennis-post-delete` and the post's primary key as an argument.
    - The `assertEqual` method is used to check that the response status code is 200, indicating a successful 
    response.
    - The `assertTemplateUsed` method is used to check that the correct template ('tennis/post_delete.html') is 
    used for rendering the response.
    """

    def test_view_deletes_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('tennis-post-delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tennis-post-list'))
        
        post_exists = Posts.objects.filter(pk=self.post.pk).exists()
        self.assertFalse(post_exists)
    """
    - The `test_view_deletes_post` method tests that the tennis post delete view deletes the post and redirects 
    to the post list view.
    - The test user is logged in using the `login` method of the client.
    - A POST request is made to the tennis post delete view using the `client.post` method and the `reverse` 
    function with the URL pattern name `tennis-post-delete` and the post's primary key as an argument.
    - The `assertEqual` method is used to check that the response status code is 302, indicating a redirect.
    - The `assertRedirects` method is used to check that the response redirects to the tennis post list view.
    - The `filter` method is used to check if the post with the given primary key still exists in the database.
    - The `assertFalse` method is used to check that the post does not exist in the database.
    """

