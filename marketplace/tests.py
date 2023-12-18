from urllib import response
from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from django.template import Context, Template
from marketplace.views import (
    MarketplaceItemPostListView,
    MarketplaceItemPostDetailView,
    MarketplaceItemPostCreateView,
    MarketplaceItemPostUpdateView,
    MarketplaceItemPostDeleteView,
)
from marketplace.models import MarketplaceItemPost

# Create your tests here.
"""
In a Django application, you typically want to test the following:

1 Models: Test the methods and properties of your models. This includes any custom save methods, any custom querysets, and any other logic that's part of your models.

2 Views: Test that your views return the correct HTTP status codes and render the correct templates. For class-based views, you might also want to test any custom methods or overridden methods.

3 Forms: Test that your forms validate correctly. This includes testing any custom validation rules, and testing that the form saves correctly.

4 Templates: Test that your templates render correctly. This includes testing any custom template tags or filters, and testing that the templates display the correct data.

5 URLs: Test that your URL configurations route to the correct views.
"""


class MarketplaceItemPostListViewTest(TestCase):
    def test_no_posts(self):
        response = self.client.get(reverse("marketplace_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts found.")
        self.assertQuerysetEqual(response.context["marketposts"], [])

    def test_post_w_image(self):
        with open("./media/images/megaphone.jpg", "rb") as file:
            pass

        post = MarketplaceItemPost.objects.create(
            title="Test post",
            description="Test post description",
            price=100.00,
            location="Test location",
            category="technology",
        )
