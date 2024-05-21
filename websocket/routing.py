from django.urls import path
from .consumer import MessageConsumer
url=[
    path("<str:roomid>/",MessageConsumer.as_asgi(),name="asgi_chat")
]