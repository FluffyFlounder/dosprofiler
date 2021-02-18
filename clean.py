#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import pickle
import time
import sys

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
	'new': True,
}

users = {
	
}


input_ = input('Are you sure you want to wipe and reset?: ')

data = [local, tasks, users]

if input_ == 'yes' or input_ == 'y':
	time.sleep(0.3)
	with open("data.dat",'wb') as x:
		pickle.dump(data, x)
		print('Deleting contents...')
time.sleep(0.4)
print('New file created.')