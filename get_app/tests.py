from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

class PostListViewTest(TestCase):
    def setUp(self):
        self.post1 = Post.objects.create(author=self.user, title='Test Post 1', description='Description 1')
        self.post2 = Post.objects.create(author=self.user, title='Test Post 2', description='Description 2')
        self.user = User.objects.create_user(username='testuser', password='user')
        
    def test_post_creation(self):
        post1 = Post.objects.get(id=1)
        post2 = Post.objects.get(id=2)

        self.assertEqual(post1.title, 'Test Post 1')
        self.assertEqual(post1.description, 'Description 1')

        self.assertEqual(post2.title, 'Test Post 2')
        self.assertEqual(post2.description, 'Description 2')








