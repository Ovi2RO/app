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

    def test_view_url_exists(self):
        response = self.client.get(reverse('laika-post-list'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-list'))
        self.assertTemplateUsed(response, 'laika/post_list.html')

    def test_view_returns_queryset(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-list'))
        posts = response.context['posts']
        expected_posts = [self.post1, self.post2, self.post3]
        self.assertQuerysetEqual(posts, expected_posts)

    def test_view_filters_by_title(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-list'), {'search_words': 'Test', 'search_field': 'title'})
        posts = response.context['posts']
        self.assertQuerysetEqual(posts, [self.post1, self.post2])

    def test_view_filters_by_description(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-list'), {'search_words': 'test', 'search_field': 'description'})
        posts = response.context['posts']
        self.assertQuerysetEqual(posts, [self.post1, self.post2])

    def test_view_filters_by_date(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-list'), {'search_date': date.today()})
        posts = response.context['posts']
        self.assertQuerysetEqual(posts, [self.post1, self.post2, self.post3])

    def test_view_no_filters_return_all_posts(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-list'))
        posts = response.context['posts']
        self.assertQuerysetEqual(posts, [self.post1, self.post2, self.post3])


class PostCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
          
    def test_view_renders_template(self):
        self.client.login(username='testuser', password='testpassword', follow=True)
        response = self.client.get(reverse('laika-post-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laika/post_create.html')

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
        
    def test_view_requires_authentication(self):
        response = self.client.get(reverse("laika-post-create"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/signin_signup.html")


class PostDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', description='This is a test post.', author=self.user)
        
    def test_view_renders_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laika/post_detail.html')
        
    def test_view_displays_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'], self.post)
        
    def test_view_displays_404_for_invalid_post_id(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-detail', args=[999]))
        self.assertEqual(response.status_code, 404)


class PostUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', description='This is a test post.', author=self.user)
        
    def test_view_renders_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laika/post_update.html')
        
    def test_view_displays_post_form(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertIsNotNone(form)
        self.assertEqual(form.initial['title'], 'Test Post')
        self.assertEqual(form.initial['description'], 'This is a test post.')
        
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
        

class PostDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', description='This is a test post.', author=self.user)
        
    def test_view_renders_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-post-delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laika/post_delete.html')
        
    def test_view_deletes_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('laika-post-delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('laika-post-list'))
        
        post_exists = Post.objects.filter(pk=self.post.pk).exists()
        self.assertFalse(post_exists)


class LaikaProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
    def test_view_renders_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('laika-profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laika/profile.html')
        
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
            
    def test_view_renders_form_errors_on_invalid_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('laika-profile'), {
            'pet_form-name': '',
        })
        self.assertEqual(response.status_code, 200)
        pet_form = response.context['pet_form']
        self.assertIsInstance(pet_form, PetForm)
        self.assertTrue(pet_form.errors)






