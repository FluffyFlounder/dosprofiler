#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

#import parser
from configparser import ConfigParser
config = ConfigParser()
#set config file
config.read('config.ini')
#set variables from config file
speed = config.get('SETTINGS', 'speed')
key = config.get('SETTINGS', 'key')

#setup random timer to make loadings look cool
from random import randint
loadings = True
z = 1
def load_time():
	global z
	global loadings
	if speed == 0:
		loadings = False
	if speed == 1:
		z = 2
	elif speed == 2:
		z = 5
	elif speed == 3:
		z = 8
	x = randint(1, z)
	if loadings == False:
		return(0)
	if loadings == True:
		return(x/10)

#import libraries
import time
print('Time module imported...')
time.sleep(load_time())

import sys
print('SYS module imported...')
time.sleep(load_time())

import pickle
print("Pickle module imported...")
time.sleep(load_time())

import os
print("OS module imported...")
time.sleep(load_time())

#load data from data.dat
try:
	data = pickle.load(open("data.dat", "rb"))
	print('Data successfullying imported...')
	time.sleep(load_time())
except FileNotFoundError:
	print("Data.dat file not found or corrupted, please run 'python3 clean.py' to create new file.")
	sys.exit()
local = data[0]
tasks = data[1]
users = data[2]

time.sleep(load_time())
print('Launched.')
print("  _____            _____            __ _ _           \n |  __ \\          |  __ \\          / _(_) |          \n | |  | | ___  ___| |__) | __ ___ | |_ _| | ___ _ __ \n | |  | |/ _ \\/ __|  ___/ '__/ _ \\|  _| | |/ _ \\ '__|\n | |__| | (_) \\__ \\ |   | | | (_) | | | | |  __/ |   \n |_____/ \\___/|___/_|   |_|  \\___/|_| |_|_|\\___|_|\n")

#create save function to save the current local, tasks, users variables into data.dat
def save():
	save_data = [local, tasks, users]
	pickle.dump(save_data, open("data.dat", "wb"))


if local['new'] == True:
	print("Please run setup.py script...")
	sys.exit('Closed with error; setup.py not run.')
	

close = False
while close == False:
	task = input(': ').split()
	tasked = False

	if task[0] == 'help':
		print('')
		for item in tasks:
			print(f"{item} -- {tasks[item]}")
		print('')
		tasked = True

	if task[0] == 'close':
		save()
		sys.exit('Closed with task-exit.')


	if task[0] == 'ls' and len(task) == 1:
		print('\nLOCAL:\n            {')
		for item in local:
			print(f"    '{item}': {local[item]}")
		print('}')
		print('\nTASKS:\n            {')
		for item in tasks:
			print(f"    '{item}': '{tasks[item]}'")
		print('}')
		print('\nUSERS:\n            {')
		for item in users:
			print(f"    '{item}': {users[item]}")
		print('}')
		print('\n')
		tasked = True

	elif task[0] == 'ls' and len(task) > 1:
		continue_ = True
		try:
			temp_dict = eval(task[1])
		except NameError:
			print('\nNameError, please enter a valid dictionary;')
			continue_ = False
		while tasked == False and continue_ == True:
			print(f'\n{task[1].lower()}:\n            {{')
			for item in temp_dict:
				print(f"    '{item}': {temp_dict[item]}")
			print('}\n')
			tasked = True

	if task[0] == 'clear':
		os.system('clear')
		tasked = True

	if task[0] == 'useradd':
		__continue__ = True
		_user = task[1]
		if __continue__ == True:
			if len(task) > 1:
				new_username = task[1]
				users[new_username] = {}
				tasked = True
			elif len(task) < 2: 
				print("'useradd' requires 1 argument, 0 given")
				tasked = True


	if task[0] == 'userdel':
		__continue__ = True
		_user = task[1]
		if _user not in users:
			print('Please enter a valid user or create a new profile.')
			__continue__ = False
			tasked = True
		if __continue__ == True:
			if len(task) > 1:
				user = task[1]
				del users[user]
				tasked = True
			elif len(task) < 2:
				print("'userdel' requires 1 argument, 0 given")
				tasked = True

	if task[0] == 'addinfo' and len(task) == 4:
		__continue__ = True
		_user = task[1]
		_item = task[2]
		_info = task[3]
		if _user not in users:
			print('Please enter a valid user or create a new profile.')
			__continue__ = False
		if __continue__ == True:
			user_dict = users[_user]
			user_dict[_item] = _info
			save()
			tasked = True

	if task[0] == 'rminfo' and len(task) == 3:
		__continue__ = True
		_user = task[1]
		_item = task[2]
		if _user not in users:
			print('Please enter a valid user or create a new profile.')
			__continue__ = False
			tasked = True
		if __continue__ == True:
			print('Deleting...')
			user_dict = users[_user]
			user_dict.pop(_item, None)
			print('Done.')
			tasked = True



















	#if a valid command wasn't ran, tasked will stay == False, causing this to run:
	if tasked == False:
		print("Please enter a valid command, try 'help' for a list of commands.")