from django.urls import path
from . import views

urlpatterns = [
    path("", views.RoomList.as_view(), name="rooms"),
    path("<int:pk>/", views.room, name="room"),
    path("create_room/", views.RoomCreateView.as_view(), name="room_create"),
]
