import pickle
import time
import sys
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')

tasks = {
	'useradd [name]': 'Adds new profile',
	'userdel [user]': 'Deletes a profile',
	'addinfo [user] [item] [info]': 'Adds info about a subject',
	'rminfo [user] [item]': "Deletes an item from a user's profile",
	'close': 'Closes current instance of DosProfiler',
	'ls [dict]': 'View all .dat data, or pass a specific table to view',
	'clear': 'Clears the terminal output',
}
local = {
	'new': False,
}
users = {
	
}

data = [local, tasks, users]
skip = False

if len(sys.argv) > 1 and sys.argv[1] == 'skip':
	skip = True
if skip == False:
	input_ = input('Are you sure you want to wipe and reset?: ')
	_input = 'yes'

if input_ == 'yes' or input_ == 'y' or skip == True:
	time.sleep(0.2)
	with open("data.dat",'wb') as x:
		pickle.dump(data, x)
		print('Deleting contents...')
time.sleep(0.4)
print('File cleaned.')