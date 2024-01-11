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


