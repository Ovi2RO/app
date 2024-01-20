from django.views.generic import (
    ListView,
)
from django.shortcuts import render, redirect

# Create your views here.


class MessageAppInboxView(ListView):
    pass


def MessageAppChatView(request, *args, **kwargs):
    context = {}
    return render(request, "message_app/message_page.html", context)
