from django import forms
from .models import Pet, LaikaProfileUser


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = LaikaProfileUser
        fields = ['image']
        

class PetForm(forms.ModelForm):
    
    class Meta:
        model = Pet
        fields = ['pet_name', 'species', 'species_type', 'description'] 

"""
- `from django import forms` imports the `forms` module from Django. The `forms` module provides a set of 
form-related classes and functions for handling form rendering, validation, and processing.

- `from .models import Pet, LaikaProfileUser` imports the `Pet` and `LaikaProfileUser` models from the local 
`models` module. This assumes that there is a `models.py` file in the same directory as this code and that 
these models are defined in that file.

- `class ProfileForm(forms.ModelForm):` defines a `ProfileForm` class that inherits from `forms.ModelForm`. 
This class is used to create a form for the `LaikaProfileUser` model.

- `class Meta:` defines the nested `Meta` class within the `ProfileForm` class. The `Meta` class provides 
metadata for the form, including the model to use (`model = LaikaProfileUser`) and the fields to include in 
the form (`fields = ['image']`).

- `class PetForm(forms.ModelForm):` defines a `PetForm` class that also inherits from `forms.ModelForm`. 
This class is used to create a form for the `Pet` model.

- `class Meta:` defines the nested `Meta` class within the `PetForm` class. The `Meta` class provides metadata 
for the form, including the model to use (`model = Pet`) and the fields to include in the form (`fields = 
['pet_name', 'species', 'species_type', 'description']`).

By creating these form classes, you can easily generate HTML forms based on your models. These forms can be 
used for data validation, rendering, and processing.
"""
