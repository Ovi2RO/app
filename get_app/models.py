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

# Create your models here.
class Post(models.Model):
    """
    A Django model representing a blog post.

    Attributes:
        author (ForeignKey): The author of the post, linked to the User model.
        title (CharField): The title of the post, limited to 100 characters.
        description (TextField): The content or description of the post.
        created_at (DateTimeField): The date and time when the post was created, set automatically on creation.
        updated_at (DateTimeField): The date and time when the post was last updated, updated automatically.
        image (ImageField): An optional image associated with the post, uploaded to the 'images/' directory.
    
    Methods:
        __str__: Returns the string representation of the post, which is the title.
        imageURL: Property method that returns the URL of the post's image or an empty string if no image exists.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    
    def __str__(self) -> str:
        """
        Returns the string representation of the post, which is the title.

        Returns:
            str: The title of the post.
        """
        return self.title
    
    @property
    def imageURL(self):
        """
        Property method that returns the URL of the post's image or an empty string if no image exists.

        Returns:
            str: The URL of the post's image or an empty string.
        """
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
'''
Django Model Documentation
class Post(models.Model)
This line defines a Django model named Post that inherits from the models.Model class.

author = models.ForeignKey(User, on_delete=models.CASCADE)
This field represents a foreign key relationship to the User model, indicating the author of the post. 
The on_delete=models.CASCADE argument specifies that if the referenced user is deleted, all associated posts should be deleted as well.

title = models.CharField(max_length=100)
This field represents the title of the post and is limited to a maximum of 100 characters.

description = models.TextField()
This field represents the content or description of the post and is a text field allowing for longer content.

created_at = models.DateTimeField(auto_now_add=True)
This field represents the date and time when the post was created.
The auto_now_add=True argument ensures that it is automatically set to the current date and time when the post is created.

updated_at = models.DateTimeField(auto_now=True)
This field represents the date and time when the post was last updated. 
The auto_now=True argument ensures that it is automatically updated to the current date and time whenever the post is modified.

image = models.ImageField(upload_to='images/', null=True, blank=True)
This field represents an optional image associated with the post. 
Images are uploaded to the 'images/' directory. The null=True and blank=True arguments allow for the image to be optional.

def __str__(self) -> str:
This method returns the string representation of the post, which is the title.
It is used for display purposes, such as in the Django admin interface.

@property def imageURL(self):
This property method returns the URL of the post's image or an empty string if no image exists.
It is used to conveniently access the image URL in templates or other parts of the application.

'''    
    

# f"{self.author} {self.title}"
# self.author + " " + self.title

class Comment(models.Model):
    """
    A Django model representing comments on blog posts.

    Attributes:
        post (ForeignKey): The post to which the comment is attached, linked to the Post model.
        content (TextField): The content or text of the comment.
        author (ForeignKey): The author of the comment, linked to the User model.
        created_at (DateTimeField): The date and time when the comment was created, set automatically on creation.
        updated_at (DateTimeField): The date and time when the comment was last updated, updated automatically.
        parent_comment (ForeignKey, optional): The parent comment to which this comment is a reply, linked to the Comment model.
    
    Methods:
        __str__: Returns the string representation of the comment, which is the content.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey("self", on_delete=models.CASCADE, related_name="reply", null=True, blank=True)
    
    def __str__(self) -> str:
        """
        Returns the string representation of the comment, which is the content.

        Returns:
            str: The content of the comment.
        """
        return self.content
    
'''
Django Model Documentation
class Comment(models.Model)
This line defines a Django model named Comment that inherits from the models.Model class.

post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
This field represents a foreign key relationship to the Post model, indicating the post to which the comment belongs. 
The on_delete=models.CASCADE argument specifies that if the referenced post is deleted, the comment should be deleted as well. The related_name="comments" allows accessing comments associated with a post using the comments attribute on a Post instance.

content = models.TextField()
This field represents the content or text of the comment and is a text field allowing for longer content.

author = models.ForeignKey(User, on_delete=models.CASCADE)
This field represents the author of the comment and is linked to the User model.

created_at = models.DateTimeField(auto_now_add=True)
This field represents the date and time when the comment was created.
The auto_now_add=True argument ensures that it is automatically set to the current date and time when the comment is created.

updated_at = models.DateTimeField(auto_now=True)
This field represents the date and time when the comment was last updated.
The auto_now=True argument ensures that it is automatically updated to the current date and time whenever the comment is modified.

parent_comment = models.ForeignKey("self", on_delete=models.CASCADE, related_name="reply", null=True, blank=True)
This field represents a reference to the parent.
'''
    
    
    
    
    
    