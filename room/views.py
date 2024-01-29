from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room, Message

# Create your views here.


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, "room/rooms.html", {"rooms": rooms})


@login_required
def room(request, pk):
    room = Room.objects.get(pk=pk)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, "room/room.html", {"room": room, "messages": messages})



