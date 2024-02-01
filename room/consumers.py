import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Message, Room
from django.contrib.auth.models import User


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = text_data_json["user"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {"type": "chat.message", "message": message, "user": user},
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        user = event["user"]

        # Send message to WebSocket
        self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "user": user,
                }
            )
        )


# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         print("connect")
#         self.accept()

#     def disconnect(self, close_code):
#         pass

#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#         user = text_data_json["user"]

#         print("message", message)
#         self.send(
#             text_data=json.dumps(
#                 {
#                     "message": message,
#                     "user": user,
#                 }
#             )
#         )
