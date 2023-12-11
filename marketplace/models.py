from email.mime import image
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class MarketplaceItemPost(models.Model):
    # these should be automatic
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # aux
    category_choices = [
        ("technology", "Technology"),
        ("services", "Services"),
        ("vehicles", "Vehicles"),
        ("fashion_beauty", "Fashion & Beauty"),
        ("furniture", "Furniture"),
        ("animals", "Animals"),
        ("property_for_rent", "Property for rent"),
        ("books", "Books"),
    ]

    # these can be created and updated
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        choices=category_choices,
    )
    image = models.ImageField(
        upload_to="images/",
        null=True,
        blank=True,
    )  # gotta finish this one later

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("marketplace_detail", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("marketplace_delete", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("marketplace_update", kwargs={"pk": self.pk})
