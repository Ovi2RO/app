from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from .models import Post

class PostListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', description='This is a test post', created_at=datetime.now())


    def test_post_list_view_with_search_words(self):
        search_words = 'test'
        search_field = 'title'

        response = self.client.get(reverse('post-list'), {'search_words': search_words, 'search_field': search_field})

        self.assertContains(response, self.post.title)





