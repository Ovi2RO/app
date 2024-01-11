from django.db import models
from django.contrib.auth.models import User


class LaikaProfileUser(models.Model):
    
    laika_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="lpu")
    image = models.ImageField(upload_to='laika_img/', default='laika_img/laika_logo_400.png', null=True, blank=True)
    
    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ""
    #     return url
    

class Pet(models.Model):
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=20, default = "None")
    species = models.CharField(max_length=20, default = "None")
    species_type = models.CharField(max_length=20, null=True, blank=True, default = "None")
    description = models.TextField(null=True, blank=True, default = "None")
    
    def __str__(self):
        return f"{self.species}: {self.pet_name}"

class Post(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="laika_author")
    image = models.ImageField(upload_to='laika_img/', default='laika_img/laika_logo_400.png', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.title}: {self.author}'
    
    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ""
    #     return url