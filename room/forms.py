from django import forms
from .models import Room


class CreateRoom(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            "room_name",
            "post_author",
        ]
