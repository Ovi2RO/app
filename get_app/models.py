from django.db import models
from django.contrib.auth.models import User

'''
from django.db import models
This line imports the models module from Django, which provides the base classes for defining database models. 
In Django, models are used to define the structure and behavior of database tables.

from django.contrib.auth.models import User
This line imports the User model from the django.contrib.auth.models module. 
The User model is a built-in model provided by Django for handling user authentication and authorization. It includes fields such as username, password, email, and others, which are commonly used for user authentication in web applications.

'''

class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
"""
 - `Post` is a Django model that inherits from `models.Model`.

- `author` is a foreign key field that relates to the `User` model, using 
`models.ForeignKey(User, on_delete=models.CASCADE)`. It represents the author of the post.

- `title` is a character field with a maximum length of 100 characters, defined using 
`models.CharField(max_length=100)`. It represents the title of the post.

- `description` is a text field, defined using `models.TextField()`. It represents the 
description of the post.

- `created_at` is a date and time field that automatically stores the creation timestamp of the 
post, defined using `models.DateTimeField(auto_now_add=True)`.

- `updated_at` is a date and time field that automatically stores the last update timestamp of 
the post, defined using `models.DateTimeField(auto_now=True)`.

- `image` is an image field that allows uploading an image file, defined using 
`models.ImageField(upload_to='images/', null=True, blank=True)`. It specifies that the uploaded 
images will be stored in the 'images/' directory.

- `__str__` is a method that returns a string representation of the post. In this case, it returns 
the title of the post.

- `imageURL` is a property method that returns the URL of the post's image. It handles exceptions 
and returns an empty string if the image URL is not available.
 """


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey("self", on_delete=models.CASCADE, related_name="reply", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.content

"""
- `Comment` is a Django model that inherits from `models.Model`.

- `post` is a foreign key field that relates to the `Post` model, using 
`models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)`. 
It represents the post to which the comment belongs. The `related_name` attribute specifies the name 
to use for the reverse relation from the `Post` model to the `Comment` model.

- `content` is a text field, defined using `models.TextField()`. It represents the content of the comment.

- `author` is a foreign key field that relates to the `User` model, using 
`models.ForeignKey(User, on_delete=models.CASCADE)`. It represents the author of the comment.

- `created_at` is a date and time field that automatically stores the creation timestamp of the 
comment, defined using `models.DateTimeField(auto_now_add=True)`.

- `updated_at` is a date and time field that automatically stores the last update timestamp of the 
comment, defined using `models.DateTimeField(auto_now=True)`.

- `parent_comment` is a foreign key field that relates to the `Comment` model itself, using 
`models.ForeignKey("self", on_delete=models.CASCADE, related_name="reply", null=True, blank=True)`. 
It represents the parent comment to which the comment is a reply. The `related_name` attribute specifies 
the name to use for the reverse relation from the `Comment` model to the reply comments.
"""
    
    
    
    
    