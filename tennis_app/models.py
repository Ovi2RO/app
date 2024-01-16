from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from PIL import Image

class Posts(models.Model):
    user_name = models.CharField(max_length=50)
    user_last = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    GENDER_CHOICES = [
    ('A','Any'),
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
    ]
 
    
    user_gender = models.CharField(max_length=10, choices=GENDER_CHOICES,null=True)
    birth_date = models.DateTimeField(default=timezone.now)
   
    # @property
    # def age(self):
    #      from datetime import date
    #      today = date.today()
    #      age = today.year-self.birth_date
    #      return age
     
    #age = property(age)

   
    phone = models.CharField(max_length= 50)
    description = models.TextField(max_length=500)
    current_date = models.DateField(default=timezone.now)
    play_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='tennis_app/static/image/default.jpg', upload_to='tennis_app/static/image')
    LEVEL_CHOICES = [
        ('A','Any'),
        ('1', 'Novice'),
        ('2', 'Intermediate'),
        ('3', 'Advanced'),
        ('4', 'Expert'),
        ('5', 'Master'),
    ]
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES)
    LANGUAGE_CHOICES = [
        ('A','Any'),
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