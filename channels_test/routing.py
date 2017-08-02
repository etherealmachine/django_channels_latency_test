from channels.routing import route, route_class
from channels_test.consumers import EventConsumer

channel_routing = [
	route_class(EventConsumer, path=r'^/ws/$')
]