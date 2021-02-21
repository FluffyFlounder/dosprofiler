import pickle
import time
import sys
import codec

tasks = {
	codec.encode('useradd [name]'): codec.encode('Adds new profile'),
	codec.encode('userdel [user]'): codec.encode('Deletes a profile'),
	codec.encode('addinfo [user] [item] [info]'): codec.encode('Adds info about a subject'),
	codec.encode('rminfo [user] [item]'): codec.encode("Deletes an item from a user's profile"),
	codec.encode('close'): codec.encode('Closes current instance of DosProfiler'),
	codec.encode('ls [dict]'): codec.encode('View all .dat data, or pass a specific table to view'),
	codec.encode('clear'): codec.encode('Clears the terminal output'),
	codec.encode('save'): codec.encode('Saves .dat file'),
}
local = {
	
}
users = {
	
}

data = [local, tasks, users]
skip = False
sub_run = False
input_ = ''

if not sub_run == True:
	if len(sys.argv) > 1 and sys.argv[1] == 'skip':
		skip = True
		input_ = 'yes'
	if skip == False:
		input_ = input('Are you sure you want to wipe and reset?: ')

if input_ == 'yes' or input_ == 'y' or sub_run == True:
	time.sleep(0.2)
	with open("data.dat",'wb') as x:
		pickle.dump(data, x)
		print('Deleting contents...')
time.sleep(0.4)
print('File cleaned.')