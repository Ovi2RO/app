from django.contrib import admin
from .models import LaikaProfileUser, Pet, Post

admin.site.register(LaikaProfileUser)
admin.site.register(Pet)
admin.site.register(Post)