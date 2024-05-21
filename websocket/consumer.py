from channels.generic.websocket import AsyncJsonWebsocketConsumer

class MessageConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        room_id=self.scope["url_route"]["kwargs"]["roomid"]
        await self.channel_layer.group_add(room_id,self.channel_name)

    async def receive_json(self, content, **kwargs):
        room_id=self.scope["url_route"]["kwargs"]["roomid"]
        await self.channel_layer.group_send(room_id,{'type':"send.message",'msg':content})
    
    async def send_message(self,event):
        await self.send_json(content=event['msg'])
    
    async def disconnect(self, code):
        room_id=self.scope["url_route"]["kwargs"]["roomid"]
        await self.channel_layer.group_send(room_id,{'type':"send.message",'msg':{'username':'server','message':"left the chat"}})
        await self.close()