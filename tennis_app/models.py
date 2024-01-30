from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from PIL import Image

class Posts(models.Model):

    GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
    ]
 
    
    user_gender = models.CharField(max_length=10, choices=GENDER_CHOICES,null=True)
    birth_date = models.DateField(default=timezone.now)
   
    phone = models.CharField(max_length= 50)
    description = models.TextField(max_length=500)
    current_date = models.DateField(default=timezone.now)
    play_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='tennis_app/static/image/default.jpg', upload_to='tennis_app/static/image')
    LEVEL_CHOICES = [
        ('1', 'Novice'),
        ('2', 'Intermediate'),
        ('3', 'Advanced'),
        ('4', 'Expert'),
        ('5', 'Master'),
    ]
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES)
    LANGUAGE_CHOICES = [
        ('1', 'english'),
        ('2', 'deutsch'),
        ('3', 'spanish'),
        ('4', 'french'),
        ('5', 'persia'),
    ]
    language = models.CharField(max_length=1, choices=LANGUAGE_CHOICES)
    type = models.CharField(max_length= 100, blank=True)
    club_name = models.CharField(max_length=50, null=True, blank=True)
    author = models.ForeignKey(User,on_delete= models.CASCADE, null=True, blank=True)    

    def __str__(self):
            return f'{self.user_name} Post'

    def save(self,*args, **kwargs):
            super().save(*args, **kwargs)


            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path) 

"""
- "user_name": A character field with a maximum length of 50 characters, representing the user's name.
- "user_last": A character field with a maximum length of 100 characters, representing the user's last name.
- "user_email": An email field with a maximum length of 100 characters, representing the user's email address.
- "user_gender": A character field with a maximum length of 10 characters, representing the user's gender. It has 
predefined choices defined in the "GENDER_CHOICES" list.
- "birth_date": A DateTimeField with a default value set to the current time, representing the user's birth date.
- "phone": A character field with a maximum length of 50 characters, representing the user's phone number.
- "description": A TextField with a maximum length of 500 characters, representing a description provided by the 
user.
- "current_date": A DateField with a default value set to the current date, representing the current date.
- "play_date": A DateTimeField with a default value set to the current time, representing a play date.
- "image": An ImageField with a default image path and an upload path, representing an image associated with the 
post.
- "level": A character field with a maximum length of 1 character, representing the user's level. It has 
predefined choices defined in the "LEVEL_CHOICES" list.
- "language": A character field with a maximum length of 1 character, representing the user's preferred language. 
It has predefined choices defined in the "LANGUAGE_CHOICES" list.
- "type": A character field with a maximum length of 100 characters, representing the type of the post. It is 
optional and can be left blank.
- "club_name": A character field with a maximum length of 50 characters, representing the name of the club. It is 
optional and can be left blank.
- "author": A foreign key field referencing the "User" model, indicating the author of the post. It allows null 
values and blank values.

The "__str__" method is overridden to provide a string representation of the "Posts" object, returning the user's 
name followed by "Post".

The "save" method is overridden to perform additional actions when saving the object. It resizes the image 
associated with the post if its height or width exceeds 300 pixels.
"""


class Comments(models.Model):
    text = models.TextField(max_length=500)
    rank = RANK_CHOICES = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Good'),
        ('4', 'Very Good'),
        ('5', 'Perfect'),
    ]
    rank = models.CharField(blank= True,max_length=1, choices=RANK_CHOICES )
    author = models.ForeignKey(User, on_delete= models.CASCADE,null=True, blank=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')


class Messages(models.Model):
    sender = models.IntegerField()
    recipient = models.IntegerField()
    content = models.TextField(max_length=1000)