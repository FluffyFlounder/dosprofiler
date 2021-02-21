import base64
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
dev_options = config.get('SETTINGS', 'dev_options')

def encode(msg):
	x = base64.b64encode(msg.encode("utf-8"))
	x = x.decode('utf-8')
	if dev_options == True:
		print(f'{msg} --> {x}')
	return x

def decode(msg):
	x = base64.b64decode(msg).decode("utf-8")
	if dev_options == True:
		print(f'{msg} --> {x}')
	return x
