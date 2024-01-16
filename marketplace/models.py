from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


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
        upload_to="market_img/",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("marketplace_detail", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("marketplace_delete", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("marketplace_update", kwargs={"pk": self.pk})

"""
`class MarketplaceItemPost(models.Model)`: This line defines a new model class called `MarketplaceItemPost` that 
inherits from `models.Model`. This means that the `MarketplaceItemPost` class is a Django model.

`author = models.ForeignKey(User, on_delete=models.CASCADE)`: This line defines a foreign key relationship to 
the `User` model. Each `MarketplaceItemPost` object is associated with a specific user who authored it. The 
`on_delete=models.CASCADE` parameter specifies that if the associated user is deleted, the `MarketplaceItemPost` 
object should also be deleted.

`created_on = models.DateTimeField(auto_now_add=True)`: This line defines a `DateTimeField` named `created_on` 
that represents the date and time when the `MarketplaceItemPost` object was created. The `auto_now_add=True` 
parameter specifies that the field should be automatically set to the current date and time when the object is 
created.

`updated_on = models.DateTimeField(auto_now=True)`: This line defines a `DateTimeField` named `updated_on` that 
represents the date and time when the `MarketplaceItemPost` object was last updated. The `auto_now=True` parameter 
specifies that the field should be automatically updated to the current date and time whenever the object is saved.

`category_choices = [...]`: This line defines a list of choices for the `category` field. Each choice is a tuple 
containing a value and a label. These choices represent different categories that an item post can belong to.

`title = models.CharField(max_length=100)`: This line defines a `CharField` named `title` that represents the 
title of the marketplace item post. It has a maximum length of 100 characters.

`description = models.TextField()`: This line defines a `TextField` named `description` that represents the 
description of the marketplace item post. It can store a large amount of text.

`price = models.DecimalField(max_digits=10, decimal_places=2)`: This line defines a `DecimalField` named `price` 
that represents the price of the marketplace item post. It can store a decimal number with a maximum of 10 digits 
and 2 decimal places.

`location = models.CharField(max_length=200, blank=True, null=True)`: This line defines a `CharField` named 
`location` that represents the location of the marketplace item. It has a maximum length of 200 characters. It is 
optional, as indicated by `blank=True` and `null=True`.

`category = models.CharField(...)`: This line defines a `CharField` named `category` that represents the category 
of the marketplace item post. It has a maximum length of 100 characters. It is optional, as indicated by 
`blank=True` and `null=True`. It uses the `category_choices` defined earlier as the choices for the field.

`image = models.ImageField(...)`: This line defines an `ImageField` named `image` that represents the image 
associated with the marketplace item post. It allows users to upload an image file. The images will be stored in 
the "market_img/" directory. It is optional, as indicated by `null=True` and `blank=True`.

`def __str__(self) -> str:`: This method defines how the `MarketplaceItemPost` object should be represented as a 
string. In this case, it returns the `title` of the object.

`def get_absolute_url(self):`: This method defines the absolute URL for the `MarketplaceItemPost` object. It 
returns the URL pattern named "marketplace_detail" with the `pk` parameter set to the primary key of the object. 
This is typically used for redirecting to the detail view of the object after creation.

`def get_delete_url(self):`: This method defines the URL for deleting the `MarketplaceItemPost` object. It returns 
the URL pattern named "marketplace_delete" with the `pk` parameter set to the primary key of the object.

`def get_update_url(self):`: This method defines the URL for updating the `MarketplaceItemPost` object. It returns 
the URL pattern named "marketplace_update" with the `pk` parameter set to the primary key of the object.

By using this model, you can create, update, and delete `MarketplaceItemPost` objects in your Django application. 
You can also access the author, creation date, and update date of each object. The model provides methods for 
getting the absolute URL, delete URL, and update URL of each object.
"""