import json
import base64
from channels.generic.websocket import AsyncWebsocketConsumer


class ImageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Called on connection
        await self.accept()

    async def disconnect(self, close_code):
        # Called when the connection is closed
        pass

    async def receive(self, text_data):
        # Receive base64 encoded image data from WebSocket
        image_data_base64 = text_data

        # Decode base64 image data
        image_data = base64.b64decode(image_data_base64)

        # Analysis of the image could be performed here
        # For simplicity, let's assume the result is True
        result = True

        # Send result data back to Flutter client
        await self.send(text_data=json.dumps({
            'result': result
        }))
