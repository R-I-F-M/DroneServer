from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DroneConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        print(text_data)
        # text_data_json = json.loads(text_data)
        # message = text_data_json.get('message')

        if text_data == 'ConnectDrone':
            # Respond with success message
            await self.send(text_data=json.dumps({
                'status': 'success',
                'message': 'Drone connected successfully'
            }))