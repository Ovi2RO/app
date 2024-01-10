from django.contrib import admin
from .models import Post, Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)

'''
Django Admin Registration Documentation

from django.contrib import admin
This line imports the admin module from the django.contrib package, which provides the Django administration functionality.

from .models import Post, Comment
This line imports the Post and Comment models from the same Django app. 
These models are assumed to be defined in the models.py file of the app.

admin.site.register(Post)
This line registers the Post model with the Django admin site. Once registered, you can manage Post objects through the Django admin interface.
This includes viewing, adding, editing, and deleting Post instances.

admin.site.register(Comment)
This line registers the Comment model with the Django admin site. 
Similarly, it allows you to manage Comment objects through the Django admin interface.

'''