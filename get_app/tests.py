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

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/parenting/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('post-list'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post-list'), follow=True)
        self.assertTemplateUsed(response, 'get_app/post_list.html')

    def test_view_returns_queryset_filtered_by_search_words(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post-list'), {'search_words': 'Test Post 1'}, follow=True)
        self.assertContains(response, 'Test Post 1')
        self.assertNotContains(response, 'Test Post 3')

    def test_view_returns_queryset_filtered_by_search_field(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post-list'), {'search_field': 'description', 'search_words': 'test post'})
        self.assertContains(response, 'Test Post 1')
        self.assertContains(response, 'Test Post 2')

    def test_view_returns_queryset_filtered_by_search_date(self):
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post-list'), {'search_date': yesterday})
        self.assertContains(response, 'Test Post 1')
        self.assertContains(response, 'Test Post 2')

    def test_view_returns_all_queryset_when_no_filters_applied(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post-list'))
        self.assertContains(response, 'Test Post 1')
        self.assertContains(response, 'Test Post 2')


class PostCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/parenting/create/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "get_app/post_create.html")

    def test_view_redirects_to_post_list_on_successful_creation(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse("post-create"), {
            "title": "Test Post",
            "description": "This is a test post"
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "get_app/post_list.html")

    def test_view_requires_authentication(self):
        response = self.client.get(reverse("post-create"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/signin_signup.html")


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

    def test_view_redirects_to_post_detail(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            reverse('post-update', kwargs={'pk': self.post.pk}),
            {'title': 'Updated Post', 'description': 'This is an updated post'}
        )
        self.assertRedirects(response, reverse('post-detail', kwargs={'pk': self.post.pk}))


class PostDeleteViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.post = Post.objects.create(title='Test Post', description='This is a test post', author=cls.user)

    def test_view_redirects_to_login_if_not_authenticated(self):
        response = self.client.get(reverse('post-delete', kwargs={'pk': self.post.pk}))
        self.assertRedirects(response, reverse('account_login') + '?next=' + reverse('post-delete', kwargs={'pk': self.post.pk}))

    def test_view_returns_403_if_not_author_or_staff(self):
        user = User.objects.create_user(username='anotheruser', password='anotherpassword')
        self.client.login(username='anotheruser', password='anotherpassword')
        response = self.client.get(reverse('post-delete', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 403)

    def test_view_deletes_post_if_author(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post-delete', kwargs={'pk': self.post.pk}))
        self.assertRedirects(response, reverse('post-list'))
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

    def test_view_deletes_post_if_staff(self):
        user = User.objects.create_user(username='staffuser', password='staffpassword', is_staff=True)
        self.client.login(username='staffuser', password='staffpassword')
        response = self.client.post(reverse('post-delete', kwargs={'pk': self.post.pk}))
        self.assertRedirects(response, reverse('post-list'))
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())


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

    def test_view_adds_comment_to_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post-detail', kwargs={'pk': self.post.pk}), {'content': 'New comment'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(self.post.comments.all()), 1)
        self.assertEqual(self.post.comments.first().content, 'New comment')

    def test_view_deletes_comment(self):
        self.client.login(username='testuser', password='testpassword')
        comment = Comment.objects.create(post=self.post, content='Test comment', author=self.user)
        response = self.client.post(reverse('post-detail', kwargs={'pk': self.post.pk}), {'delete_comment_id': comment.id})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(id=comment.id).exists())

    def test_view_deletes_reply(self):
        self.client.login(username='testuser', password='testpassword')
        comment = Comment.objects.create(post=self.post, content='Test comment', author=self.user)
        reply = Comment.objects.create(post=self.post, content='Test reply', author=self.user, parent_comment=comment)
        response = self.client.post(reverse('post-detail', kwargs={'pk': self.post.pk}), {'delete_reply_id': reply.id})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(id=reply.id).exists())









