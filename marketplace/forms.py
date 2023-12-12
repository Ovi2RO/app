from django import forms
from .models import MarketplaceItemPost


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
