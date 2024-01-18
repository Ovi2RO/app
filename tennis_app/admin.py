from django.contrib import admin
from tennis_app import models

# Register your models here.

admin.site.register(models.Posts)
admin.site.register(models.Comments)
admin.site.register(models.Messages)

"""
1. `from django.contrib import admin`:
   - This line imports the `admin` module from `django.contrib`.
   - The `admin` module provides the Django admin interface.

2. `from tennis_app import models`:
   - This line imports the `models` module from the `tennis_app` package.
   - The `models` module likely contains the definition of the Django models that you want to register with the 
   admin interface.

3. `admin.site.register(models.Posts)`:
   - This line registers the `Posts` model from the `models` module with the admin interface.
   - By registering a model with the admin interface, you can manage and interact with instances of that model 
   through the Django admin.

4. `admin.site.register(models.Comments)`:
   - This line registers the `Comments` model from the `models` module with the admin interface.

5. `admin.site.register(models.Messages)`:
   - This line registers the `Messages` model from the `models` module with the admin interface.
"""
