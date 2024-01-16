from django.contrib import admin
from .models import MarketplaceItemPost


admin.site.register(MarketplaceItemPost)

"""
`from django.contrib import admin`: This line imports the `admin` module from the `django.contrib` package. 
The `admin` module provides the functionality for creating an administration site for managing Django models.

`from .models import MarketplaceItemPost`: This line imports the `MarketplaceItemPost` model from the current 
directory's `models.py` file. The `MarketplaceItemPost` model is a Django model that represents a marketplace 
item post.

`admin.site.register(MarketplaceItemPost)`: This line registers the `MarketplaceItemPost` model with the Django 
admin site. By registering a model, you enable the admin interface to manage instances of that model. Once 
registered, you can perform CRUD (Create, Read, Update, Delete) operations on `MarketplaceItemPost` objects 
through the admin site.

"""