from urllib import response
from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from django.template import Context, Template
from marketplace.views import (
    MarketplaceListView,
    MarketplaceDetailView,
    MarketplaceCreateView,
    MarketplaceUpdateView,
    MarketplaceDeleteView,
)
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

    def test_view_url_exists(self):
        response = self.client.get(reverse('marketplace_list'), follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('marketplace_list'))
        self.assertTemplateUsed(response, 'marketplace/marketplace_list.html')

    def test_marketplace_list_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('marketplace_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marketplace/marketplace_list.html')
        self.assertContains(response, 'Test Post 1')
        self.assertContains(response, 'Test Post 2')
    
    def test_marketplace_list_view_unauthenticated(self):
        response = self.client.get(reverse('marketplace_list'))
        self.assertEqual(response.status_code, 302)


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

    def test_marketplace_detail_view_unauthenticated(self):
        response = self.client.get(reverse('marketplace_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 302)


class MarketplaceCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_marketplace_create_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('marketplace_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marketplace/marketplace_create.html')
        self.assertIsInstance(response.context['form'], CreateMarketplacePostForm)

    def test_marketplace_create_view_unauthenticated(self):
        response = self.client.get(reverse('marketplace_create'))
        self.assertEqual(response.status_code, 302)

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

    def test_marketplace_update_view_authenticated_non_author(self):
        self.client.login(username='anotheruser', password='anotherpassword')
        response = self.client.get(reverse('marketplace_update', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 302)

    def test_marketplace_update_view_unauthenticated(self):
        response = self.client.get(reverse('marketplace_update', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 302)

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


class MarketplaceDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = MarketplaceItemPost.objects.create(title='Test Post', description='Test description', price=10.0, location='Test Location', category='test_category', author=self.user)

    def test_marketplace_delete_view_post_authenticated_author(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('marketplace_delete', kwargs={'pk': self.post.pk}))
        self.assertRedirects(response, reverse('marketplace_list'))
        self.assertFalse(MarketplaceItemPost.objects.filter(pk=self.post.pk).exists())

    def test_marketplace_delete_view_post_unauthenticated(self):
        response = self.client.post(reverse('marketplace_delete', kwargs={'pk': self.post.pk}))
        self.assertTrue(MarketplaceItemPost.objects.filter(pk=self.post.pk).exists())


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

    def test_view_with_invalid_search_form(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('marketplace_search')
        response = self.client.get(url, {'title': '', 'category': 'Test Category'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_view_requires_login(self):
        url = reverse('marketplace_search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


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

    def test_view_with_other_user(self):
        url = reverse('marketplace_my_posts', kwargs={'username': 'testuser'})
        self.client.login(username='otheruser', password='testpassword')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Test Post')