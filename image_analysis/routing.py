from django.urls import re_path
from .consumers.imageConsumer import ImageConsumer


websocket_urlpatterns = [
    re_path(r'ws/analysis-image/',  ImageConsumer.as_asgi()),
]
