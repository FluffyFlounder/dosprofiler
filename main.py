#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

speed = 0 #options: 0 = OFF, 1, 2, 3 = SLOW

##################################################################

from random import randint

loadings = True
z = 1
def load_time():
	global z
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
	elif loadings == True:
		return(x/10)

if loadings == False:
	x = 0

try:
	import time
	print('Time module imported...')
except NameError:
	print("Time module not found, try 'pip3 install time'")

time.sleep(load_time())

import sys
print('SYS module imported...')

time.sleep(load_time())

try:
	import pickle
	print("Pickle module imported...")
except NameError:
	print("Pickle module not found, try 'pip3 install pickle'")

import os
print("OS module imported...")

time.sleep(load_time())
print('Initializing...')
time.sleep(load_time())
print('Importing dependencies...')

try:
	data = pickle.load(open("data.dat", "rb"))
	print('Data successfullying imported...')
except FileNotFoundError:
	print('Data.dat file not found or corrupted, please run clean.py to create new blank file...')
	sys.exit()

local = data[0]
tasks = data[1]
users = data[2]
time.sleep(load_time())
print('Data decrpyted...')

time.sleep(load_time())
print('Launched.')

print("  _____            _____            __ _ _           \n |  __ \\          |  __ \\          / _(_) |          \n | |  | | ___  ___| |__) | __ ___ | |_ _| | ___ _ __ \n | |  | |/ _ \\/ __|  ___/ '__/ _ \\|  _| | |/ _ \\ '__|\n | |__| | (_) \\__ \\ |   | | | (_) | | | | |  __/ |   \n |_____/ \\___/|___/_|   |_|  \\___/|_| |_|_|\\___|_|\n")

################################## Engine Launched ##############################

def save():
	save_data = [local, tasks, users]
	pickle.dump(save_data, open("data.dat", "wb"))

if local['new'] == True:
	print("Welcome to DosProfiler, running intial setup installation scripts...")
	local['new'] = False
	os.system('cd .. && sudo chmod +x DosProfiler/*')
	save()

close = False
while close == False:
	task = input(': ')
	task = task.split()
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




















	if tasked == False:
		print("Please enter a valid command, try 'help' for a list of commands.")