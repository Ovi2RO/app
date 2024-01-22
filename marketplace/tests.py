from urllib import response
from django.test import TestCase
from django.urls import reverse

from marketplace.models import MarketplaceItemPost
from django.contrib.auth.models import User
from marketplace.forms import CreateMarketplacePostForm

# Create your tests here.


class MarketplaceListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post1 = MarketplaceItemPost.objects.create(
            author=self.user,
            title='Test Post 1',
            description='Description for Test Post 1',
            price=10.0,
            location='Test Location 1',
            category='technology'
        )
        self.post2 = MarketplaceItemPost.objects.create(
            author=self.user,
            title='Test Post 2',
            description='Description for Test Post 2',
            price=20.0,
            location='Test Location 2',
            category='services'
        )
    """
    The `setUp` method is used to set up the test data before each test method is run. It creates a test user 
    and two `MarketplaceItemPost` instances.
    """

    def test_view_url_exists(self):
        response = self.client.get(reverse('marketplace_list'), follow=True)
        self.assertEqual(response.status_code, 200)
    """
    - The `test_view_url_exists` method tests that the marketplace list view URL exists.
    - The `client.get` method is used to send a GET request to the marketplace list URL using the `reverse` 
    function to retrieve the URL by its name.
    - The response status code is checked using the `assertEqual` method to ensure it is 200 (OK).
    """
    
    def test_view_uses_correct_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('marketplace_list'))
        self.assertTemplateUsed(response, 'marketplace/marketplace_list.html')
    """
    - The `test_view_uses_correct_template` method tests that the marketplace list view uses the correct template.
    - The user is logged in using the `login` method of the client.
    - A GET request is made to the marketplace list URL using the `client.get` method, with the URL pattern name 
    `reverse('marketplace_list')`.
    - The `assertTemplateUsed` method is used to check that the response uses the correct template, which is 
    `'marketplace/marketplace_list.html'`.
    """

    def test_marketplace_list_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('marketplace_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marketplace/marketplace_list.html')
        self.assertContains(response, 'Test Post 1')
        self.assertContains(response, 'Test Post 2')
    """
    - The `test_marketplace_list_view_authenticated` method tests the marketplace list view when the user is 
    authenticated.
    - The user is logged in using the `login` method of the client.
    - A GET request is made to the marketplace list URL using the `client.get` method, with the URL pattern name 
    `reverse('marketplace_list')`.
    - The `assertEqual` method is used to check that the response status code is 200 (OK).
    - The `assertTemplateUsed` method is used to check that the correct template is used, which is 
    `'marketplace/marketplace_list.html'`.
    - The `assertContains` method is used to check that the response contains the titles of the test posts, 
    which are `'Test Post 1'` and `'Test Post 2'`.
    """
    
    def test_marketplace_list_view_unauthenticated(self):
        response = self.client.get(reverse('marketplace_list'))
        self.assertEqual(response.status_code, 302)
    """
    - The `test_marketplace_list_view_unauthenticated` method tests the marketplace list view when the user is 
    unauthenticated.
    - A GET request is made to the marketplace list URL using the `client.get` method, with the URL pattern name 
    `reverse('marketplace_list')`.
    - The `assertEqual` method is used to check that the response status code is 302 (Redirect).
    """


class MarketplaceDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = MarketplaceItemPost.objects.create(
            author=self.user,
            title='Test Post',
            description='Description for Test Post',
            price=10.0,
            location='Test Location',
            category='technology'
        )

    def test_marketplace_detail_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('marketplace_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marketplace/marketplace_detail.html')
        self.assertEqual(response.context['marketpost'], self.post)
    """
    - The `test_marketplace_detail_view_authenticated` method tests the marketplace detail view when the user is 
    authenticated.
    - The user is logged in using the `login` method of the client.
    - A GET request is made to the marketplace detail URL using the `client.get` method, with the URL pattern 
    name `reverse('marketplace_detail')` and the post's primary key as a parameter.
    - The `assertEqual` method is used to check that the response status code is 200 (OK).
    - The `assertTemplateUsed` method is used to check that the correct template is used, which is 
    `'marketplace/marketplace_detail.html'`.
    - The `assertEqual` method is used to check that the marketplace post in the context is the same as the 
    test post.
    """

    def test_marketplace_detail_view_unauthenticated(self):
        response = self.client.get(reverse('marketplace_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 302)
    """
    - The `test_marketplace_detail_view_unauthenticated` method tests the marketplace detail view when the user 
    is unauthenticated.
    - A GET request is made to the marketplace detail URL using the `client.get` method, with the URL pattern 
    name `reverse('marketplace_detail')` and the post's primary key as a parameter.
    - The `assertEqual` method is used to check that the response status code is 302 (Redirect).
    """


class MarketplaceCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_marketplace_create_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('marketplace_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marketplace/marketplace_create.html')
        self.assertIsInstance(response.context['form'], CreateMarketplacePostForm)
    """
    - The `test_marketplace_create_view_authenticated` method tests the marketplace create view when the user is 
    authenticated.
    - The user is logged in using the `login` method of the client.
    - A GET request is made to the marketplace create URL using the `client.get` method, with the URL pattern 
    name `reverse('marketplace_create')`.
    - The `assertEqual` method is used to check that the response status code is 200 (OK).
    - The `assertTemplateUsed` method is used to check that the correct template is used, which is 
    `'marketplace/marketplace_create.html'`.
    - The `isinstance` function is used to check that the form in the context is an instance of 
    `CreateMarketplacePostForm`.
    """

    def test_marketplace_create_view_unauthenticated(self):
        response = self.client.get(reverse('marketplace_create'))
        self.assertEqual(response.status_code, 302)
    """
    - The `test_marketplace_create_view_unauthenticated` method tests the marketplace create view when the user 
    is unauthenticated.
    - A GET request is made to the marketplace create URL using the `client.get` method, with the URL pattern 
    name `reverse('marketplace_create')`.
    - The `assertEqual` method is used to check that the response status code is 302 (Redirect).
    """

    def test_marketplace_create_view_post_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        form_data = {
            'title': 'Test Post',
            'description': 'Description for Test Post',
            'price': 10.0,
            'location': 'Test Location',
            'category': 'technology',
        }
        response = self.client.post(reverse('marketplace_create'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/marketplace/')
        self.assertEqual(MarketplaceItemPost.objects.count(), 1)
    """
    - The `test_marketplace_create_view_post_authenticated` method tests the marketplace create view when the 
    user is authenticated and submits a POST request.
    - The user is logged in using the `login` method of the client.
    - The `form_data` dictionary is prepared with the necessary data for the marketplace post.
    - A POST request is made to the marketplace create URL using the `client.post` method, with the URL pattern 
    name `reverse('marketplace_create')` and the form data.
    - The `assertEqual` method is used to check that the response status code is 302 (Redirect).
    - The `assertRedirects` method is used to check that the response redirects to the marketplace URL, which is 
    `'/marketplace/'`.
    - The `assertEqual` method is used to check that a new marketplace item post has been created in the database.
    """

    def test_marketplace_create_view_post_unauthenticated(self):
        form_data = {
            'title': 'Test Post',
            'description': 'Description for Test Post',
            'price': 10.0,
            'location': 'Test Location',
            'category': 'technology',
        }
        response = self.client.post(reverse('marketplace_create'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(MarketplaceItemPost.objects.count(), 0)
    """
    - The `test_marketplace_create_view_post_unauthenticated` method tests the marketplace create view when the 
    user is unauthenticated and submits a POST request.
    - The `form_data` dictionary is prepared with the necessary data for the marketplace post.
    - A POST request is made to the marketplace create URL using the `client.post` method, with the URL pattern 
    name `reverse('marketplace_create')` and the form data.
    - The `assertEqual` method is used to check that the response status code is 302 (Redirect).
    - The `assertEqual` method is used to check that no new marketplace item post has been created in the database.
    """


class MarketplaceUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = MarketplaceItemPost.objects.create(
            author=self.user,
            title='Test Post',
            description='Description for Test Post',
            price=10.0,
            location='Test Location',
            category='technology'
        )

    def test_marketplace_update_view_authenticated_author(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('marketplace_update', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marketplace/marketplace_update.html')
        self.assertEqual(response.context['object'], self.post)
    """
    - The `test_marketplace_update_view_authenticated_author` method tests the marketplace update view when the 
    user is authenticated as the author of the post.
    - The user is logged in using the `login` method of the client.
    - A GET request is made to the marketplace update URL using the `client.get` method, with the URL pattern 
    name `reverse('marketplace_update')` and the post's primary key as a URL parameter.
    - The `assertEqual` method is used to check that the response status code is 200 (OK).
    - The `assertTemplateUsed` method is used to check that the template used for the response is 
    'marketplace/marketplace_update.html'.
    - The `assertEqual` method is used to check that the 'object' attribute in the response's context is equal 
    to the post.
    """

    def test_marketplace_update_view_authenticated_non_author(self):
        self.client.login(username='anotheruser', password='anotherpassword')
        response = self.client.get(reverse('marketplace_update', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 302)
    """
    - The `test_marketplace_update_view_authenticated_non_author` method tests the marketplace update view when 
    the user is authenticated as a non-author of the post.
    - Another user is logged in using the `login` method of the client.
    - A GET request is made to the marketplace update URL using the `client.get` method, with the URL pattern 
    name `reverse('marketplace_update')` and the post's primary key as a URL parameter.
    - The `assertEqual` method is used to check that the response status code is 302 (Redirect).
    """

    def test_marketplace_update_view_unauthenticated(self):
        response = self.client.get(reverse('marketplace_update', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 302)
    """
    - The `test_marketplace_update_view_unauthenticated` method tests the marketplace update view when the user 
    is unauthenticated.
    - A GET request is made to the marketplace update URL using the `client.get` method, with the URL pattern 
    name `reverse('marketplace_update')` and the post's primary key as a URL parameter.
    - The `assertEqual` method is used to check that the response status code is 302 (Redirect).
    """

    def test_marketplace_update_view_post_authenticated_non_author(self):
        self.client.login(username='anotheruser', password='anotherpassword')
        form_data = {
            'title': 'Updated Post',
            'description': 'Updated description',
            'price': 20.0,
            'location': 'Updated Location',
            'category': 'updated_category',
        }
        response = self.client.post(reverse('marketplace_update', kwargs={'pk': self.post.pk}), data=form_data)
        self.assertEqual(response.status_code, 302)
    """
    - The `test_marketplace_update_view_post_authenticated_non_author` method tests the marketplace update view 
    when the user is authenticated as a non-author of the post and submits a POST request.
    - Another user is logged in using the `login` method of the client.
    - The form data is prepared with updated values for the post.
    - A POST request is made to the marketplace update URL using the `client.post` method, with the URL pattern 
    name `reverse('marketplace_update')` and the post's primary key as a URL parameter, along with the form data.
    - The `assertEqual` method is used to check that the response status code is 302 (Redirect).
    """

    def test_marketplace_update_view_post_unauthenticated(self):
        form_data = {
            'title': 'Updated Post',
            'description': 'Updated description',
            'price': 20.0,
            'location': 'Updated Location',
            'category': 'updated_category',
        }
        response = self.client.post(reverse('marketplace_update', kwargs={'pk': self.post.pk}), data=form_data)
        self.assertEqual(response.status_code, 302)
    """
    - The `test_marketplace_update_view_post_unauthenticated` method tests the marketplace update view when the 
    user is unauthenticated and submits a POST request.
    - The form data is prepared with updated values for the post.
    - A POST request is made to the marketplace update URL using the `client.post` method, with the URL pattern 
    name `reverse('marketplace_update')` and the post's primary key as a URL parameter, along with the form data.
    - The `assertEqual` method is used to check that the response status code is 302 (Redirect).
    """


class MarketplaceDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = MarketplaceItemPost.objects.create(title='Test Post', description='Test description', price=10.0, location='Test Location', category='test_category', author=self.user)

    def test_marketplace_delete_view_post_authenticated_author(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('marketplace_delete', kwargs={'pk': self.post.pk}))
        self.assertRedirects(response, reverse('marketplace_list'))
        self.assertFalse(MarketplaceItemPost.objects.filter(pk=self.post.pk).exists())
    """
    - The `test_marketplace_delete_view_post_authenticated_author` method tests the marketplace delete view when 
    the user is authenticated as the author of the post and submits a POST request.
    - The author of the post is logged in using the `login` method of the client.
    - A POST request is made to the marketplace delete URL using the `client.post` method, with the URL pattern 
    name `reverse('marketplace_delete')` and the post's primary key as a URL parameter.
    - The `assertRedirects` method is used to check that the response redirects to the marketplace list page.
    - The `assertFalse` method is used to check that the post no longer exists in the database by filtering the 
    `MarketplaceItemPost` model with the post's primary key.
    """

    def test_marketplace_delete_view_post_unauthenticated(self):
        response = self.client.post(reverse('marketplace_delete', kwargs={'pk': self.post.pk}))
        self.assertTrue(MarketplaceItemPost.objects.filter(pk=self.post.pk).exists())
    """
    - The `test_marketplace_delete_view_post_unauthenticated` method tests the marketplace delete view when the 
    user is unauthenticated and submits a POST request.
    - A POST request is made to the marketplace delete URL using the `client.post` method, with the URL pattern 
    name `reverse('marketplace_delete')` and the post's primary key as a URL parameter.
    - The `assertTrue` method is used to check that the post still exists in the database by filtering the 
    `MarketplaceItemPost` model with the post's primary key.
    """


class MarketplaceSearchResultsViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = MarketplaceItemPost.objects.create(title='Test Post', author=self.user, category='Test Category', price=10.99)

    def test_view_with_valid_search_form(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('marketplace_search')
        response = self.client.get(url, {'title': 'Test', 'category': 'Test Category'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
    """
    - The `test_view_with_valid_search_form` method tests the marketplace search view with a valid search form.
    - A user is logged in using the `login` method of the client.
    - The URL for the marketplace search view is obtained using the `reverse` function with the URL pattern name 
    `marketplace_search`.
    - A GET request is made to the marketplace search view using the `client.get` method, with the URL and the 
    search form parameters ('title' and 'category').
    - The `assertEqual` method is used to check that the response status code is 200 (OK).
    - The `assertContains` method is used to check that the response contains the expected content ('Test Post').
    """

    def test_view_with_invalid_search_form(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('marketplace_search')
        response = self.client.get(url, {'title': '', 'category': 'Test Category'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
    """
    - The `test_view_with_invalid_search_form` method tests the marketplace search view with an invalid search form.
    - A user is logged in using the `login` method of the client.
    - The URL for the marketplace search view is obtained using the `reverse` function with the URL pattern name 
    `marketplace_search`.
    - A GET request is made to the marketplace search view using the `client.get` method, with the URL and the 
    search form parameters ('title' and 'category').
    - The `assertEqual` method is used to check that the response status code is 200 (OK).
    - The `assertContains` method is used to check that the response contains the expected content ('Test Post').
    """

    def test_view_requires_login(self):
        url = reverse('marketplace_search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
    """
    - The `test_view_requires_login` method tests that the marketplace search view requires the user to be logged 
    in.
    - The URL for the marketplace search view is obtained using the `reverse` function with the URL pattern name 
    `marketplace_search`.
    - A GET request is made to the marketplace search view using the `client.get` method, with the URL.
    - The `assertEqual` method is used to check that the response status code is 302 (redirect).
    """


class MarketplaceMyPostsViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.other_user = User.objects.create_user(username='otheruser', password='testpassword')
        self.post = MarketplaceItemPost.objects.create(title='Test Post', author=self.user, price=10.99)

    def test_view_with_authenticated_user(self):
        url = reverse('marketplace_my_posts', kwargs={'username': 'testuser'})
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
    """
    - The `test_view_with_authenticated_user` method tests the marketplace my posts view with an authenticated user.
    - The URL for the marketplace my posts view is obtained using the `reverse` function with the URL pattern 
    name `marketplace_my_posts` and the username as a URL parameter.
    - A user is logged in using the `login` method of the client.
    - A GET request is made to the marketplace my posts view using the `client.get` method, with the URL.
    - The `assertEqual` method is used to check that the response status code is 200 (OK).
    - The `assertContains` method is used to check that the response contains the expected content ('Test Post').
    """

    def test_view_with_other_user(self):
        url = reverse('marketplace_my_posts', kwargs={'username': 'testuser'})
        self.client.login(username='otheruser', password='testpassword')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Test Post')
    """
    - The `test_view_with_other_user` method tests the marketplace my posts view with a different user.
    - The URL for the marketplace my posts view is obtained using the `reverse` function with the URL pattern 
    name `marketplace_my_posts` and the username as a URL parameter.
    - A different user is logged in using the `login` method of the client.
    - A GET request is made to the marketplace my posts view using the `client.get` method, with the URL.
    - The `assertEqual` method is used to check that the response status code is 200 (OK).
    - The `assertNotContains` method is used to check that the response does not contain the expected content 
    ('Test Post').
    """
