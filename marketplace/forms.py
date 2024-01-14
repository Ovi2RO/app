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
