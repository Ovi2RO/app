from django.contrib import admin
from tennis_app import models

# Register your models here.

admin.site.register(models.Posts)
admin.site.register(models.Comments)
admin.site.register(models.Messages)


