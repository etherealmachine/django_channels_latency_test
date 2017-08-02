from channels.generic.websockets import WebsocketConsumer
import json
import time


class EventConsumer(WebsocketConsumer):

	strict_ordering = False

	def connect(self, message, **kwargs):
		self.message.reply_channel.send({'accept': True})

	def raw_receive(self, message, **kwargs):
		content = json.loads(message['text'])
		content['recv_time'] = time.time()
		self.message.reply_channel.send({
			'text': json.dumps(content)
		})
