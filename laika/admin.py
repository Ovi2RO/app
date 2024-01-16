from django.contrib import admin
from .models import LaikaProfileUser, Pet, Post

admin.site.register(LaikaProfileUser)
admin.site.register(Pet)
admin.site.register(Post)

"""
- `from django.contrib import admin` imports the `admin` module from Django's `contrib` package. The 
`admin` module provides the functionality to create an administration site for managing your Django models.

- `from .models import LaikaProfileUser, Pet, Post` imports the `LaikaProfileUser`, `Pet`, and `Post` models 
from the local `models` module. This assumes that there is a `models.py` file in the same directory as this 
code and that these models are defined in that file.

- `admin.site.register(LaikaProfileUser)` registers the `LaikaProfileUser` model with the Django admin site. 
This allows you to manage instances of the `LaikaProfileUser` model through the admin interface.

- `admin.site.register(Pet)` registers the `Pet` model with the Django admin site. This allows you to manage 
instances of the `Pet` model through the admin interface.

- `admin.site.register(Post)` registers the `Post` model with the Django admin site. This allows you to manage 
instances of the `Post` model through the admin interface.

By registering your models with the admin site, you gain access to a pre-built administration interface where 
you can create, update, and delete instances of your models.
"""