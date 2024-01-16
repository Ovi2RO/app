from django import forms
from .models import Posts
from dj_proj import settings
from .models import Comments

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'user_name', 
            'user_last',
            'user_email',
            'user_gender',
            'birth_date',
            'phone',
            'description',
            'play_date',
            'image',
            'level',
            'language',
            'type',
            'club_name',
            ]
    widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'},format=settings.DATE_INPUT_FORMAT),

            'user_email': forms.EmailInput(attrs={'type': 'email', 'placeholder': 'Enter your email'}),
            'play_date': forms.DateInput(attrs={'type': 'date'},format=settings.DATE_INPUT_FORMAT),
            'image': forms.FileInput(),
        }
    
    def clean_user_email(self):
        # Validate the uniqueness of user_email
        user_email = self.cleaned_data.get('user_email')
        if Posts.objects.filter(user_email=user_email).exists():
            raise forms.ValidationError("This email is already in use. Please choose a different one.")
        return user_email


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'user_name', 
            'user_last',
            'user_gender',
            'birth_date',
            'phone',
            'description',
            'play_date',
            'image',
            'level',
            'language',
            'type',
            'club_name',
            
            ]
    widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'},format=settings.DATE_INPUT_FORMAT),
            'play_date': forms.DateInput(attrs={'type': 'date'},format=settings.DATE_INPUT_FORMAT),
            'image': forms.FileInput(),
        }
    def __init__(self, *args, **kwargs):
        super(UpdatePostForm, self).__init__(*args, **kwargs)
        # If an image is already uploaded, show its current URL
        if self.instance and self.instance.image:
            self.fields['image'].widget.attrs['current-image'] = self.instance.image.url
        else:
            self.fields['image'].widget.attrs['current-image'] = ''
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text', 'rank']


from django import forms
from .models import Posts
from dj_proj import settings
from .models import Comments

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'user_name', 
            'user_last',
            'user_email',
            'user_gender',
            'birth_date',
            'phone',
            'description',
            'play_date',
            'image',
            'level',
            'language',
            'type',
            'club_name',
            ]
    widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'},format=settings.DATE_INPUT_FORMAT),

            'user_email': forms.EmailInput(attrs={'type': 'email', 'placeholder': 'Enter your email'}),
            'play_date': forms.DateInput(attrs={'type': 'date'},format=settings.DATE_INPUT_FORMAT),
            'image': forms.FileInput(),
        }
    
    def clean_user_email(self):
        # Validate the uniqueness of user_email
        user_email = self.cleaned_data.get('user_email')
        if Posts.objects.filter(user_email=user_email).exists():
            raise forms.ValidationError("This email is already in use. Please choose a different one.")
        return user_email


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'user_name', 
            'user_last',
            'user_gender',
            'birth_date',
            'phone',
            'description',
            'play_date',
            'image',
            'level',
            'language',
            'type',
            'club_name',
            
            ]
    widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'},format=settings.DATE_INPUT_FORMAT),
            'play_date': forms.DateInput(attrs={'type': 'date'},format=settings.DATE_INPUT_FORMAT),
            'image': forms.FileInput(),
        }
    def __init__(self, *args, **kwargs):
        super(UpdatePostForm, self).__init__(*args, **kwargs)
        # If an image is already uploaded, show its current URL
        if self.instance and self.instance.image:
            self.fields['image'].widget.attrs['current-image'] = self.instance.image.url
        else:
            self.fields['image'].widget.attrs['current-image'] = ''
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text', 'rank']


class SearchForm(forms.Form):
    start_age = forms.IntegerField(required=False)
    end_age = forms.IntegerField(required=False)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    location = forms.CharField(max_length=50, required=False)
    level = forms.ChoiceField(choices=Posts.LEVEL_CHOICES, required=False)
    language = forms.ChoiceField(choices=Posts.LANGUAGE_CHOICES, required=False)
    gender = forms.ChoiceField(choices=Posts.GENDER_CHOICES, required=False)
