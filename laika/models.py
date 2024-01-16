from django.db import models
from django.contrib.auth.models import User


class LaikaProfileUser(models.Model):
    
    laika_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="lpu")
    image = models.ImageField(upload_to='laika_img/', default='laika_img/laika_logo_400.png', null=True, blank=True)

"""
- `class LaikaProfileUser(models.Model):` defines a `LaikaProfileUser` class that inherits from `models.Model`. 
This class represents a model for a Laika profile user.

- `laika_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="lpu")` creates a one-to-one 
relationship field named `laika_user` that links the `LaikaProfileUser` model with the built-in `User` model. 
This field defines a foreign key relationship where each `LaikaProfileUser` instance is associated with one 
`User` instance. The `on_delete` parameter specifies the behavior when the referenced `User` instance is deleted 
(it will delete the associated `LaikaProfileUser` instance as well). The `related_name` parameter specifies the 
reverse relation name from the `User` model back to the `LaikaProfileUser` model.

- `image = models.ImageField(upload_to='laika_img/', default='laika_img/laika_logo_400.png', null=True, 
blank=True)` creates an `image` field of type `ImageField`. This field allows users to upload an image file for 
their Laika profile. The `upload_to` parameter specifies the directory where the uploaded images will be stored. 
The `default` parameter specifies the default image to use if no image is uploaded. The `null=True` parameter 
allows the field to be nullable in the database. The `blank=True` parameter allows the field to be left blank in 
forms.

By defining this model, you can create instances of `LaikaProfileUser` that are associated with specific `User` 
instances and store additional information such as profile images.
"""


class Pet(models.Model):
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=20, default = "None")
    species = models.CharField(max_length=20, default = "None")
    species_type = models.CharField(max_length=20, null=True, blank=True, default = "None")
    description = models.TextField(null=True, blank=True, default = "None")
    
    def __str__(self):
        return f"{self.species}: {self.pet_name}"

"""
- `class Pet(models.Model):` defines a `Pet` class that inherits from `models.Model`. This class represents a 
model for a pet.

- `owner = models.ForeignKey(User, on_delete=models.CASCADE)` creates a foreign key field named `owner` that 
links the `Pet` model with the built-in `User` model. This field defines a many-to-one relationship where each 
`Pet` instance is associated with one `User` instance. The `on_delete` parameter specifies the behavior when the 
referenced `User` instance is deleted (it will delete the associated `Pet` instance as well).

- `pet_name = models.CharField(max_length=20, default = "None")` creates a character field named `pet_name` that 
can store up to 20 characters. The `default` parameter specifies the default value to use if no value is provided.

- `species = models.CharField(max_length=20, default = "None")` creates a character field named `species` that 
can store up to 20 characters. The `default` parameter specifies the default value to use if no value is provided.

- `species_type = models.CharField(max_length=20, null=True, blank=True, default = "None")` creates a character 
field named `species_type` that can store up to 20 characters. The `null=True` parameter allows the field to be 
nullable in the database. The `blank=True` parameter allows the field to be left blank in forms. The `default` 
parameter specifies the default value to use if no value is provided.

- `description = models.TextField(null=True, blank=True, default = "None")` creates a text field named 
`description` that can store a large amount of text. The `null=True` parameter allows the field to be nullable in 
the database. The `blank=True` parameter allows the field to be left blank in forms. The `default` parameter 
specifies the default value to use if no value is provided.

- `def __str__(self):` defines a `__str__` method for the `Pet` class. This method returns a string representation 
of the `Pet` instance, which is used for display purposes. It returns a string that combines the `species` and 
`pet_name` attributes.
"""


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
    
"""
- `class Post(models.Model):` defines a `Post` class that inherits from `models.Model`. This class represents a 
model for a post.

- `author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="laika_author")` creates a foreign 
key field named `author` that links the `Post` model with the built-in `User` model. This field defines a 
many-to-one relationship where each `Post` instance is associated with one `User` instance. The `on_delete` 
parameter specifies the behavior when the referenced `User` instance is deleted (in this case, it will delete 
the associated `Post` instance as well). The `related_name` parameter specifies the reverse relation name from 
the `User` model back to the `Post` model.

- `image = models.ImageField(upload_to='laika_img/', default='laika_img/laika_logo_400.png', null=True, 
blank=True)` creates an `image` field of type `ImageField`. This field allows users to upload an image file for 
their post. The `upload_to` parameter specifies the directory where the uploaded images will be stored. The 
`default` parameter specifies the default image to use if no image is uploaded. The `null=True` parameter allows 
the field to be nullable in the database. The `blank=True` parameter allows the field to be left blank in forms.

- `title = models.CharField(max_length=100)` creates a character field named `title` that can store up to 100 
characters.

- `description = models.TextField()` creates a text field named `description` that can store a large amount of 
text.

- `created_at = models.DateField(auto_now_add=True)` creates a date field named `created_at` that automatically 
sets the current date when a new `Post` instance is created.

- `updated_at = models.DateField(auto_now=True)` creates a date field named `updated_at` that automatically 
updates to the current date whenever a `Post` instance is saved.

- `class Meta:` defines the inner class `Meta` that provides metadata for the `Post` model.

- `ordering = ['-updated_at']` specifies the default ordering of `Post` instances based on the `updated_at` 
field in descending order.

- `def __str__(self):` defines a `__str__` method for the `Post` class. This method returns a string 
representation of the `Post` instance, which is used for display purposes. It returns a string that combines the 
`title` and `author` attributes.

By defining this model, you can create instances of `Post` that are associated with specific `User` instances 
and store information about the posts, such as their titles, descriptions, images, and creation/update timestamps.
"""