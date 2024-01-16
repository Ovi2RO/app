from random import choices
from django import forms
from .models import MarketplaceItemPost
import datetime


class CreateMarketplacePostForm(forms.ModelForm):
    class Meta:
        model = MarketplaceItemPost
        fields = [
            "title",
            "description",
            "price",
            "location",
            "category",
            "image",
        ]

"""
`CreateMarketplacePostForm` that is used to create new instances of the `MarketplaceItemPost` model.

`class CreateMarketplacePostForm(forms.ModelForm)`: This line defines a new form class called 
`CreateMarketplacePostForm` that inherits from `forms.ModelForm`. By using `forms.ModelForm`, the form is 
automatically created based on the fields and model specified in the `Meta` class.

`class Meta:`: This nested class within the `CreateMarketplacePostForm` class is used to provide metadata for 
the form.

`model = MarketplaceItemPost`: This line specifies the model that the form is associated with, which is 
`MarketplaceItemPost`. The form will be used to create new instances of this model.

`fields = [...]`: This line specifies the fields that should be included in the form. The form includes the 
fields "title", "description", "price", "location", "category", and "image" from the `MarketplaceItemPost` model.

By using this form, you can easily create a form in your Django views or templates that allows users to input 
data for creating new `MarketplaceItemPost` objects.
"""


class SearchForm(forms.Form):
    # aux
    category_choices = [
        ("", ""),
        ("technology", "Technology"),
        ("services", "Services"),
        ("vehicles", "Vehicles"),
        ("fashion_beauty", "Fashion & Beauty"),
        ("furniture", "Furniture"),
        ("animals", "Animals"),
        ("property_for_rent", "Property for rent"),
        ("books", "Books"),
    ]

    title = forms.CharField(label="Search", max_length=255, required=False)
    user = forms.CharField(label="User", max_length=255, required=False)
    category = forms.ChoiceField(choices=category_choices, required=False)
    min_price = forms.DecimalField(label="Minimum price", required=False)
    max_price = forms.DecimalField(label="Maximum price", required=False)
    location = forms.CharField(label="Item location", max_length=255, required=False)
    init_post_date = forms.DateField(
        label="Inital date to search from",
        required=False,
        widget=forms.SelectDateWidget(
            years=range(2000, datetime.datetime.now().year + 1)
        ),
    )
    final_post_date = forms.DateField(
        label="Final date to search up to",
        required=False,
        widget=forms.SelectDateWidget(
            years=range(2000, datetime.datetime.now().year + 1)
        ),
    )

"""
`class SearchForm(forms.Form)`: This line defines a new form class called `SearchForm` that inherits from 
`forms.Form`. This means that the form is a regular Django form and not associated with a specific model.

`category_choices = [...]`: This line defines a list of choices for the `category` field. Each choice is a tuple 
containing a value and a label. The empty string "" is included as a choice to represent the option for no 
specific category.

`title = forms.CharField(...)`: This line defines a `CharField` named `title` in the form. It represents the 
search input for the item title. It has a label "Search" and a maximum length of 255 characters. It is not 
required, as indicated by `required=False`.

`user = forms.CharField(...)`: This line defines a `CharField` named `user` in the form. It represents the search 
input for the user. It has a label "User" and a maximum length of 255 characters. It is not required.

`category = forms.ChoiceField(...)`: This line defines a `ChoiceField` named `category` in the form. It represents 
the search input for the category. It uses the `category_choices` defined earlier as the choices. It is not 
required.

`min_price = forms.DecimalField(...)`: This line defines a `DecimalField` named `min_price` in the form. It 
represents the minimum price for the search. It has a label "Minimum price" and is not required.

`max_price = forms.DecimalField(...)`: This line defines a `DecimalField` named `max_price` in the form. It 
represents the maximum price for the search. It has a label "Maximum price" and is not required.

`location = forms.CharField(...)`: This line defines a `CharField` named `location` in the form. It represents 
the search input for the item location. It has a label "Item location" and a maximum length of 255 characters. 
It is not required.

`init_post_date = forms.DateField(...)`: This line defines a `DateField` named `init_post_date` in the form. It 
represents the initial date to search from. It has a label "Initial date to search from" and is not required. It 
uses a `SelectDateWidget` to provide a widget for selecting the date.

`final_post_date = forms.DateField(...)`: This line defines a `DateField` named `final_post_date` in the form. It 
represents the final date to search up to. It has a label "Final date to search up to" and is not required. It 
uses a `SelectDateWidget` to provide a widget for selecting the date.

By using this form, you can create a search form in your Django views or templates that allows users to specify 
search criteria for filtering `MarketplaceItemPost` objects.
"""