from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from tennis_app.models import Posts
from django.contrib.messages import get_messages
from .forms import CreatePostForm
from .views import PostCreateView


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

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('tennis-post-list'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('tennis-post-list'))
        self.assertTemplateUsed(response, 'tennis/post_search.html')

    def test_view_lists_empty(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('tennis-post-list'), follow=True)
        self.assertNotContains(response, self.post.user_name)
        self.assertNotContains(response, self.post.user_last)

    def test_view_requires_login(self):
        response = self.client.get(reverse('tennis-post-list'))
        self.assertEqual(response.status_code, 302)


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

    def test_view_displays_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('tennis-post-detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'], self.post)

    def test_view_displays_404_for_invalid_post_id(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('tennis-post-detail', args=[999]))
        self.assertEqual(response.status_code, 404)


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

    def test_view_displays_post_form(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('tennis-post-update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertIsNotNone(form)
        self.assertEqual(form.initial['description'], 'Lorem ipsum dolor sit amet')


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

    def test_view_deletes_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('tennis-post-delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tennis-post-list'))
        
        post_exists = Posts.objects.filter(pk=self.post.pk).exists()
        self.assertFalse(post_exists)


