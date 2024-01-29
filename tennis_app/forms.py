from django import forms
from .models import Posts
from dj_proj import settings
from .models import Comments

"""
1. `from django import forms`:
   - This line imports the `forms` module from `django`.
   - The `forms` module provides classes for creating and working with forms in Django.

2. `from .models import Posts`:
   - This line imports the `Posts` model from the current module's (`.`) `models` module.
   - The `Posts` model likely contains the definition of the Django model that the form is based on.

3. `from dj_proj import settings`:
   - This line imports the `settings` module from the `dj_proj` package.
   - The `settings` module likely contains the configuration settings for the Django project.

4. `from .models import Comments`:
   - This line imports the `Comments` model from the current module's (`.`) `models` module.
"""


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
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
            #'user_gender': forms.Select(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')]),
        }

"""
1. `class CreatePostForm(forms.ModelForm):`:
   - This line defines a form class named `CreatePostForm` that inherits from `forms.ModelForm`.
   - The `ModelForm` class is a subclass of `Form` that is specifically designed to work with Django models.

2. `class Meta:`:
   - This line defines a nested `Meta` class within the `CreatePostForm` class.
   - The `Meta` class provides metadata about the form, such as the model it is based on and the fields to include.

3. `model = Posts`:
   - This line sets the `model` attribute of the `Meta` class to the `Posts` model.
   - This specifies that the form is based on the `Posts` model.

4. `fields = [...]`:
   - This line sets the `fields` attribute of the `Meta` class to a list of field names.
   - These field names specify which fields from the `Posts` model should be included in the form.

5. `widgets = {...}`:
   - This line sets the `widgets` attribute of the `CreatePostForm` class to a dictionary of field names and 
   widget instances.
   - The `widgets` dictionary specifies the HTML widget to use for each form field.

6. `def clean_user_email(self):`:
    - This line defines a method named `clean_user_email` within the `CreatePostForm` class.
    - This method is used for custom validation of the `user_email` field.

7. `user_email = self.cleaned_data.get('user_email')`:
    - This line retrieves the value of the `user_email` field from the cleaned form data.
    - The `cleaned_data` attribute contains the validated form data.

8. `if Posts.objects.filter(user_email=user_email).exists():`:
    - This line checks if a `Posts` object with the given `user_email` already exists in the database.
    - The `Posts.objects.filter()` method is used to query the database for matching objects.

9. `raise forms.ValidationError("This email is already in use. Please choose a different one.")`:
    - This line raises a `ValidationError` if the `user_email` is already in use.
    - The `ValidationError` is a built-in Django exception that is used to handle form validation errors.

10. `return user_email`:
    - This line returns the `user_email` value if it passes the custom validation.
"""


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
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

"""
This form class is a model form for the `Posts` model. It specifies the model to be used (`Posts`) and the fields 
to include in the form (`user_name`, `user_last`, `user_gender`, `birth_date`, `phone`, `description`, 
`play_date`, `image`, `level`, `language`, `type`, `club_name`).

The `widgets` attribute is a dictionary that defines the widgets to be used for certain form fields. The 
`birth_date` and `play_date` fields are rendered as `DateInput` widgets with the `type` attribute set to 
`'date'` and the `format` attribute set to `settings.DATE_INPUT_FORMAT`. The `image` field is rendered as a 
`FileInput` widget.

The `__init__` method is a constructor that is called when an instance of the form is created. It calls the 
parent class constructor and then checks if the form instance has an `image` attribute. If it does, it sets the 
`current-image` attribute of the `image` field widget to the URL of the instance's image. Otherwise, it sets it 
to an empty string.

"""


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text', 'rank']

"""
The `CommentForm` class is a model form for the `Comments` model. It specifies the model to be used (`Comments`) 
and the fields to include in the form (`text` and `rank`).

This form class provides a convenient way to create a form that is based on the `Comments` model. By specifying 
the model and fields, Django will automatically generate the necessary form fields and validation based on the 
model's fields and attributes.

To use this form, you can create an instance of it and pass it to your view or template. 
"""


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
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
    

"""
The `CreatePostForm` class is a model form for the `Posts` model. It specifies the model to be used (`Posts`) and 
the fields to include in the form (`user_name`, `user_last`, `user_email`, `user_gender`, `birth_date`, `phone`, 
`description`, `play_date`, `image`, `level`, `language`, `type`, `club_name`).

The `widgets` attribute is a dictionary that defines the widgets to be used for certain form fields. In this case, 
the `birth_date` and `play_date` fields are rendered as `DateInput` widgets with the `type` attribute set to 
`'date'` and the `format` attribute set to `settings.DATE_INPUT_FORMAT`. The `user_email` field is rendered as an 
`EmailInput` widget with the `type` attribute set to `'email'` and a placeholder text of `'Enter your email'`. 
The `image` field is rendered as a `FileInput` widget.

The `clean_user_email` method is a custom validation method specific to the `user_email` field. It checks if the 
provided `user_email` already exists in the `Posts` model and raises a `ValidationError` if it does. This ensures 
that each user's email is unique.

`request.POST` is used to bind the form to the submitted data. If the request does not contain any data, `None` 
is passed as the initial data. You can then use this form instance in your view or template to display the form 
and handle form submission.
"""


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
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

"""
The `UpdatePostForm` class is a model form for the `Posts` model. It specifies the model to be used (`Posts`) and 
the fields to include in the form (`user_name`, `user_last`, `user_gender`, `birth_date`, `phone`, `description`, 
`play_date`, `image`, `level`, `language`, `type`, `club_name`).

The `widgets` attribute is a dictionary that defines the widgets to be used for certain form fields. In this case, 
the `birth_date` and `play_date` fields are rendered as `DateInput` widgets with the `type` attribute set to 
`'date'` and the `format` attribute set to `settings.DATE_INPUT_FORMAT`. The `image` field is rendered as a 
`FileInput` widget.

The `__init__` method is a constructor method that is called when an instance of the form is created. It overrides 
the default behavior of the parent class constructor to add custom functionality. In this case, it checks if an 
image is already uploaded for the instance being updated (`self.instance`), and if so, it sets the `current-image` 
attribute of the `image` field widget to the URL of the uploaded image. If no image is uploaded, it sets the 
`current-image` attribute to an empty string.

`request.POST` is used to bind the form to the submitted data, and `post` is the instance of the `Posts` model 
that you want to update. You can then use this form instance in your view or template to display the form with 
the pre-filled data and handle form submission.
"""


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text', 'rank']

"""
The `CommentForm` class is a model form for the `Comments` model. It specifies the model to be used (`Comments`) 
and the fields to include in the form (`text` and `rank`).

`request.POST` is used to bind the form to the submitted data. You can then use this form instance in your view or 
template to display the form and handle form submission.
"""


class SearchForm(forms.Form):
    start_age = forms.IntegerField(required=False)
    end_age = forms.IntegerField(required=False)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    location = forms.CharField(max_length=50, required=False)
    level = forms.ChoiceField(choices=Posts.LEVEL_CHOICES, required=False)
    language = forms.ChoiceField(choices=Posts.LANGUAGE_CHOICES, required=False)
    gender = forms.ChoiceField(choices=Posts.GENDER_CHOICES, required=False)

"""
 `start_age` and `end_age` are integer fields that represent the minimum and maximum age values for searching 
 posts. They are not required fields (`required=False`).
- `start_date` and `end_date` are date fields that represent the start and end dates for searching posts. They are 
rendered as date input widgets (`widget=forms.DateInput(attrs={'type': 'date'})`) and are not required 
(`required=False`).
- `location` is a character field that represents the location for searching posts. It has a maximum length of 50 
characters and is not required (`required=False`).
- `level`, `language`, and `gender` are choice fields that represent the level, language, and gender criteria for 
searching posts. They are rendered as select input widgets. The choices for these fields are specified using the 
`choices` parameter, which is set to the corresponding choices defined in the `Posts` model. These fields are not 
required (`required=False`).

 `request.GET` is used to bind the form to the query parameters in the URL. You can then use this form instance in 
 your view or template to display the form and handle the search criteria.
"""
