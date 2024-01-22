from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from datetime import date
from .models import Post
from .models import LaikaProfileUser, Pet
from .custom_form import ProfileForm, PetForm


class PostListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.post1 = Post.objects.create(title='Test Post 1', description='This is test post 1', author=cls.user)
        cls.post2 = Post.objects.create(title='Test Post 2', description='This is test post 2', author=cls.user)
        cls.post3 = Post.objects.create(title='Another Post', description='This is another post', author=cls.user)
    """
    The `setUpTestData` method is a class method that sets up the test data for the test case. In this case, it 
    creates a user and some posts using the `User.objects.create_user` and `Post.objects.create` methods.
    """

    def test_view_url_exists(self):
        response = self.client.get(reverse('laika-post-list'), follow=True)
        self.assertEqual(response.status_code, 200)
    """
    - The `test_view_url_exists` method tests that the view URL exists and returns a 200 status code.
    - The `client.get` method is used to make a GET request to the URL `reverse('laika-post-list')`, which is the 
    URL pattern name for the post list view.
    - The response object is then checked to ensure that the status code is 200 using the `assertEqual` method.
    """

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-list'))
        self.assertTemplateUsed(response, 'laika/post_list.html')
    """
    - The `test_view_uses_correct_template` method tests that the view uses the correct template.
    - The `login` method of the `client` is used to log in as the user.
    - A GET request is made to the post list URL using the `client.get` method, with the URL pattern name 
    `reverse('laika-post-list')`.
    - The response object is then checked to ensure that the template used is `'laika/post_list.html'` using the 
    `assertTemplateUsed` method.
    """

    def test_view_returns_queryset(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-list'))
        posts = response.context['posts']
        expected_posts = [self.post1, self.post2, self.post3]
        self.assertQuerysetEqual(posts, expected_posts)
    """
    - The `test_view_returns_queryset` method tests that the view returns the expected queryset.
    - The `login` method of the `client` is used to log in as the user.
    - A GET request is made to the post list URL using the `client.get` method, with the URL pattern name 
    `reverse('laika-post-list')`.
    - The `posts` queryset is retrieved from the response context using the `response.context` attribute.
    - The `expected_posts` list is defined with the expected posts.
    - The `assertQuerysetEqual` method is used to check that the `posts` queryset matches the `expected_posts` list.
    """

    def test_view_filters_by_title(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-list'), {'search_words': 'Test', 'search_field': 'title'})
        posts = response.context['posts']
        self.assertQuerysetEqual(posts, [self.post1, self.post2])
    """
    - The `test_view_filters_by_title` method tests that the view filters the posts by title correctly.
    - The `login` method of the `client` is used to log in as the user.
    - A GET request is made to the post list URL using the `client.get` method, with the URL pattern name 
    `reverse('laika-post-list')` and search parameters `{'search_words': 'Test', 'search_field': 'title'}`.
    - The `posts` queryset is retrieved from the response context using the `response.context` attribute.
    - The `expected_posts` list is defined with the expected posts that match the title filter.
    - The `assertQuerysetEqual` method is used to check that the `posts` queryset matches the `expected_posts` list.
    """

    def test_view_filters_by_description(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-list'), {'search_words': 'test', 'search_field': 'description'})
        posts = response.context['posts']
        self.assertQuerysetEqual(posts, [self.post1, self.post2])
    """
    - The `test_view_filters_by_description` method tests that the view filters the posts by description correctly.
    - The `login` method of the `client` is used to log in as the user.
    - A GET request is made to the post list URL using the `client.get` method, with the URL pattern name 
    `reverse('laika-post-list')` and search parameters `{'search_words': 'test', 'search_field': 'description'}`.
    - The `posts` queryset is retrieved from the response context using the `response.context` attribute.
    - The `expected_posts` list is defined with the expected posts that match the description filter.
    - The `assertQuerysetEqual` method is used to check that the `posts` queryset matches the `expected_posts` list.
    """

    def test_view_filters_by_date(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-list'), {'search_date': date.today()})
        posts = response.context['posts']
        self.assertQuerysetEqual(posts, [self.post1, self.post2, self.post3])
    """
    - The `test_view_filters_by_date` method tests that the view filters the posts by date correctly.
    - The `login` method of the `client` is used to log in as the user.
    - A GET request is made to the post list URL using the `client.get` method, with the URL pattern name 
    `reverse('laika-post-list')` and search parameter `{'search_date': date.today()}`.
    - The `posts` queryset is retrieved from the response context using the `response.context` attribute.
    - The `expected_posts` list is defined with the expected posts that match the date filter.
    - The `assertQuerysetEqual` method is used to check that the `posts` queryset matches the `expected_posts` list.
    """

    def test_view_no_filters_return_all_posts(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-list'))
        posts = response.context['posts']
        self.assertQuerysetEqual(posts, [self.post1, self.post2, self.post3])
    """
    - The `test_view_no_filters_return_all_posts` method tests that the view returns all posts when no filters are 
    applied.
    - The `login` method of the `client` is used to log in as the user.
    - A GET request is made to the post list URL using the `client.get` method, with the URL pattern name 
    `reverse('laika-post-list')` and without any search parameters.
    - The `posts` queryset is retrieved from the response context using the `response.context` attribute.
    - The `expected_posts` list is defined with all the posts available.
    - The `assertQuerysetEqual` method is used to check that the `posts` queryset matches the `expected_posts` list.
    """


class PostCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
          
    def test_view_renders_template(self):
        self.client.login(username='testuser', password='testpassword', follow=True)
        response = self.client.get(reverse('laika-post-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laika/post_create.html')
    """
    - The `test_view_renders_template` method tests that the view renders the correct template.
    - The `login` method of the `client` is used to log in as the user.
    - A GET request is made to the post create URL using the `client.get` method, with the URL pattern name 
    `reverse('laika-post-create')`.
    - The response status code is checked using the `assertEqual` method to ensure it is 200 (OK).
    - The `assertTemplateUsed` method is used to check that the correct template, `'laika/post_create.html'`, is 
    used to render the response.
    """

    def test_form_valid(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('laika-post-create'), data={
            'title': 'Test Post',
            'description': 'This is a test post.',
            'image': '', 
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('laika-post-list'))
        
        post = Post.objects.get(title='Test Post')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.description, 'This is a test post.')
    """
    - The `test_form_valid` method tests that the form is valid and a new post is created with the correct data.
    - The `login` method of the `client` is used to log in as the user.
    - A POST request is made to the post create URL using the `client.post` method, with the URL pattern name 
    `reverse('laika-post-create')` and form data containing a title, description, and image.
    - The response status code is checked using the `assertEqual` method to ensure it is 302 (redirect).
    - The `assertRedirects` method is used to check that the response redirects to the post list URL, 
    `reverse('laika-post-list')`.
    - The newly created post is retrieved from the database using the `Post.objects.get` method and stored in 
    the `post` variable.
    - The `author` attribute of the post is checked to ensure it is the logged-in user.
    - The `description` attribute of the post is checked to ensure it matches the form data.
    """
        
    def test_view_requires_authentication(self):
        response = self.client.get(reverse("laika-post-create"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/signin_signup.html")
    """
    - The `test_view_requires_authentication` method tests that the view requires authentication and redirects to 
    the sign-in/sign-up page.
    - A GET request is made to the post create URL using the `client.get` method, with the URL pattern name 
    `reverse("laika-post-create")`.
    - The response status code is checked using the `assertEqual` method to ensure it is 200 (OK).
    - The `assertTemplateUsed` method is used to check that the correct template, `'account/signin_signup.html'`, 
    is used to render the response.
    """


class PostDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', description='This is a test post.', author=self.user)
        
    def test_view_renders_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laika/post_detail.html')
    """
    - The `test_view_renders_template` method tests that the post detail view renders the correct template.
    - The user is logged in using the `login` method of the client.
    - A GET request is made to the post detail URL using the `client.get` method, with the URL pattern name 
    `reverse('laika-post-detail')` and the post's primary key as the argument.
    - The response status code is checked using the `assertEqual` method to ensure it is 200 (OK).
    - The `assertTemplateUsed` method is used to check that the correct template, `'laika/post_detail.html'`, 
    is used to render the response.
    """
        
    def test_view_displays_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'], self.post)
    """
    - The `test_view_displays_post` method tests that the post detail view displays the correct post.
    - The user is logged in using the `login` method of the client.
    - A GET request is made to the post detail URL using the `client.get` method, with the URL pattern name 
    `reverse('laika-post-detail')` and the post's primary key as the argument.
    - The response status code is checked using the `assertEqual` method to ensure it is 200 (OK).
    - The `post` object in the response context is accessed using `response.context['post']`.
    - The `post` object in the response context is compared to the created post using the `assertEqual` method.
    """
        
    def test_view_displays_404_for_invalid_post_id(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-detail', args=[999]))
        self.assertEqual(response.status_code, 404)
    """
    - The `test_view_displays_404_for_invalid_post_id` method tests that the post detail view returns a 404 
    status code for an invalid post ID.
    - The user is logged in using the `login` method of the client.
    - A GET request is made to the post detail URL using the `client.get` method, with the URL pattern name 
    `reverse('laika-post-detail')` and an invalid post ID (999 in this case) as the argument.
    - The response status code is checked using the `assertEqual` method to ensure it is 404 (Not Found).
    """


class PostUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', description='This is a test post.', author=self.user)
        
    def test_view_renders_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laika/post_update.html')
    """
    - The `test_view_renders_template` method tests that the post update view renders the correct template.
    - The user is logged in using the `login` method of the client.
    - A GET request is made to the post update URL using the `client.get` method, with the URL pattern name 
    `reverse('laika-post-update')` and the post's primary key as the argument.
    - The response status code is checked using the `assertEqual` method to ensure it is 200 (OK).
    - The `assertTemplateUsed` method is used to check that the correct template, `'laika/post_update.html'`, is 
    used to render the response.
    """
        
    def test_view_displays_post_form(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertIsNotNone(form)
        self.assertEqual(form.initial['title'], 'Test Post')
        self.assertEqual(form.initial['description'], 'This is a test post.')
    """
    - The `test_view_displays_post_form` method tests that the post update view displays the post form with the 
    correct initial data.
    - The user is logged in using the `login` method of the client.
    - A GET request is made to the post update URL using the `client.get` method, with the URL pattern name 
    `reverse('laika-post-update')` and the post's primary key as the argument.
    - The response status code is checked using the `assertEqual` method to ensure it is 200 (OK).
    - The `form` object is obtained from the response context using `response.context['form']`.
    - The `assertIsNotNone` method is used to check that the `form` object is not None.
    - The initial data of the form is checked using the `assertEqual` method to ensure it matches the expected 
    values.
    """
        
    def test_view_updates_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('laika-post-update', args=[self.post.pk]), data={
            'title': 'Updated Test Post',
            'description': 'This is an updated test post.',
            'image': '',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('laika-post-detail', args=[self.post.pk]))
        
        post = Post.objects.get(pk=self.post.pk)
        self.assertEqual(post.title, 'Updated Test Post')
        self.assertEqual(post.description, 'This is an updated test post.')
    """
    - The `test_view_updates_post` method tests that the post update view updates the post correctly.
    - The user is logged in using the `login` method of the client.
    - A POST request is made to the post update URL using the `client.post` method, with the URL pattern name 
    `reverse('laika-post-update')` and the post's primary key as the argument. The updated data is provided in 
    the `data` parameter.
    - The response status code is checked using the `assertEqual` method to ensure it is 302 (Redirect).
    - The `assertRedirects` method is used to check that the response redirects to the post detail URL for the 
    updated post.
    - The updated post is obtained from the database using `Post.objects.get(pk=self.post.pk)`.
    - The `assertEqual` method is used to check that the post title and description have been updated correctly.
    """
        
    def test_view_updates_post_image(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('laika-post-update', args=[self.post.pk]), data={
            'title': 'Updated Test Post',
            'description': 'This is an updated test post.',
            'replace_image': '', 
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('laika-post-detail', args=[self.post.pk]))

        post = Post.objects.get(pk=self.post.pk)
        self.assertIsNotNone(post.image)
    """
    - The `test_view_updates_post_image` method tests that the post update view updates the post image correctly.
    - The user is logged in using the `login` method of the client.
    - A POST request is made to the post update URL using the `client.post` method, with the URL pattern name 
    `reverse('laika-post-update')` and the post's primary key as the argument. The updated data is provided in 
    the `data` parameter, with the `replace_image` field set to an empty string to indicate that the image should 
    not be replaced.
    - The response status code is checked using the `assertEqual` method to ensure it is 302 (Redirect).
    - The `assertRedirects` method is used to check that the response redirects to the post detail URL for the 
    updated post.
    - The updated post is obtained from the database using `Post.objects.get(pk=self.post.pk)`.
    - The `assertIsNotNone` method is used to check that the post image is not None.
    """
        

class PostDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', description='This is a test post.', author=self.user)
        
    def test_view_renders_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laika/post_delete.html')
    """
    - The `test_view_renders_template` method tests that the post delete view renders the correct template.
    - The user is logged in using the `login` method of the client.
    - A GET request is made to the post delete URL using the `client.get` method, with the URL pattern name 
    `reverse('laika-post-delete')` and the post's primary key as the argument.
    - The response status code is checked using the `assertEqual` method to ensure it is 200 (OK).
    - The `assertTemplateUsed` method is used to check that the response uses the 'laika/post_delete.html' template.
    """
        
    def test_view_deletes_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('laika-post-delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('laika-post-list'))
        
        post_exists = Post.objects.filter(pk=self.post.pk).exists()
        self.assertFalse(post_exists)
    """
    - The `test_view_deletes_post` method tests that the post delete view deletes the post correctly.
    - The user is logged in using the `login` method of the client.
    - A POST request is made to the post delete URL using the `client.post` method, with the URL pattern name 
    `reverse('laika-post-delete')` and the post's primary key as the argument.
    - The response status code is checked using the `assertEqual` method to ensure it is 302 (Redirect).
    - The `assertRedirects` method is used to check that the response redirects to the post list URL.
    - The `filter` method is used to check if the post still exists in the database. The `exists` method is 
    called on the filtered queryset to determine if any posts match the given primary key.
    - The `assertFalse` method is used to check that the post no longer exists in the database.
    """


class LaikaProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
    def test_view_renders_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laika/profile.html')
    """
    - The `test_view_renders_template` method tests that the Laika profile view renders the correct template.
    - The user is logged in using the `login` method of the client.
    - A GET request is made to the Laika profile URL using the `client.get` method, with the URL pattern name 
    `reverse('laika-profile')`.
    - The response status code is checked using the `assertEqual` method to ensure it is 200 (OK).
    - The `assertTemplateUsed` method is used to check that the response uses the 'laika/profile.html' template.
    """
        
    def test_view_renders_forms_with_existing_data(self):
        profile = LaikaProfileUser.objects.create(laika_user=self.user)
        pet = Pet.objects.create(owner=self.user)
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-profile'))
        self.assertEqual(response.status_code, 200)
        
        profile_form = response.context['profile_form']
        pet_form = response.context['pet_form']
        
        self.assertIsInstance(profile_form, ProfileForm)
        self.assertIsInstance(pet_form, PetForm)
        self.assertEqual(profile_form.instance, profile)
        self.assertEqual(pet_form.instance, pet)
    """
    - The `test_view_renders_forms_with_existing_data` method tests that the Laika profile view renders the forms 
    with existing data.
    - A `LaikaProfileUser` object and a `Pet` object are created for the user using the `create` method of the 
    respective models.
    - The user is logged in using the `login` method of the client.
    - A GET request is made to the Laika profile URL using the `client.get` method, with the URL pattern name 
    `reverse('laika-profile')`.
    - The response status code is checked using the `assertEqual` method to ensure it is 200 (OK).
    - The profile form and pet form are retrieved from the response context using their respective keys.
    - The `isinstance` method is used to check that the profile form is an instance of `ProfileForm` and the pet 
    form is an instance of `PetForm`.
    - The `instance` attribute of the profile form is checked to ensure it is equal to the created profile object.
    - The `instance` attribute of the pet form is checked to ensure it is equal to the created pet object.
    """
        
    def test_view_renders_empty_forms(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-profile'))
        self.assertEqual(response.status_code, 200)
        
        profile_form = response.context['profile_form']
        pet_form = response.context['pet_form']
        
        self.assertIsInstance(profile_form, ProfileForm)
        self.assertIsInstance(pet_form, PetForm)
        self.assertIsNone(profile_form.instance.pk)
        self.assertIsNone(pet_form.instance.pk)
    """
    - The `test_view_renders_empty_forms` method tests that the Laika profile view renders empty forms.
    - The user is logged in using the `login` method of the client.
    - A GET request is made to the Laika profile URL using the `client.get` method, with the URL pattern name 
    `reverse('laika-profile')`.
    - The response status code is checked using the `assertEqual` method to ensure it is 200 (OK).
    - The profile form and pet form are retrieved from the response context using their respective keys.
    - The `isinstance` method is used to check that the profile form is an instance of `ProfileForm` and the pet 
    form is an instance of `PetForm`.
    - The `pk` attribute of the profile form's instance is checked to ensure it is `None`.
    - The `pk` attribute of the pet form's instance is checked to ensure it is `None`.
    """
            
    def test_view_renders_form_errors_on_invalid_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('laika-profile'), {
            'pet_form-name': '',
        })
        self.assertEqual(response.status_code, 200)
        pet_form = response.context['pet_form']
        self.assertIsInstance(pet_form, PetForm)
        self.assertTrue(pet_form.errors)
    """
    - The `test_view_renders_form_errors_on_invalid_post` method tests that the Laika profile view renders form 
    errors on an invalid POST request.
    - The user is logged in using the `login` method of the client.
    - A POST request is made to the Laika profile URL using the `client.post` method, with the URL pattern name 
    `reverse('laika-profile')`.
    - The POST data includes an empty value for the `name` field of the `pet_form`.
    - The response status code is checked using the `assertEqual` method to ensure it is 200 (OK).
    - The pet form is retrieved from the response context using its key.
    - The `isinstance` method is used to check that the pet form is an instance of `PetForm`.
    - The `errors` attribute of the pet form is checked using the `assertTrue` method to ensure it is not empty.
    """





