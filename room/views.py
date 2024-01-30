from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import Room, Message
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


# @login_required
# def rooms(request):
#     rooms = Room.objects.all()

#     return render(request, "room/rooms.html", {"rooms": rooms})


@method_decorator(login_required, name="dispatch")
class RoomList(ListView):
    model = Room
    template_name = "room/rooms.html"
    context_object_name = "rooms"

    def get_queryset(self):
        current_user = self.request.user
        queryset = Room.objects.filter(
            Q(chat_initiator=current_user) | Q(post_author=current_user)
        )
        return queryset

    # this list only shows the chats the user has access to


@login_required
def room(request, pk):
    # room = Room.objects.get(pk=pk)
    room = get_object_or_404(Room, pk=pk)

    if request.user == room.chat_initiator or request.user == room.post_author:
        messages = Message.objects.filter(room=room)[0:25]
        return render(request, "room/room.html", {"room": room, "messages": messages})

    else:
        raise PermissionDenied("You're not allowed to view this room")
