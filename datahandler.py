#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import pickle
import time
x = 0
while x == 0:
	rw = input('1 ---------- encrypt\n2 ---------- decrypt\n: ')
	if rw == '1' or rw == '2':
		x = 1

if rw == '1':
	rw = 'encrypt'
if rw == '2':
	rw = 'decrypt'

if rw == 'decrypt':
	curr_dirr = input('1 ----------- file is in current directory\n2 ----------- file is not in current directory\n: ')
	filename = input('Filename: ')
	if curr_dirr == '1':
		_continue = False
		while _continue == False:
			try:
				data = pickle.load(open(filename, "rb"))
				print('Data decrypting...')
				_continue = True
			except FileNotFoundError:
				print('File not found, try again: ')
				_continue = False
	if curr_dirr == '2':
		path = input('Path to file: ')
		_continue = False
		while _continue == False:
			try:
				data = pickle.load(open(f'{path}/{filename}', "rb"))
				print('Data decrypting...')
				_continue = True
			except FileNotFoundError:
				print('File not found, try again: ')
				_continue = False

time.sleep(0.3)
local = data[0]
tasks = data[1]
users = data[2]

print(f'\nusers:\n            {{')
for item in users:
	print(f"    '{item}': {users[item]}")
print('}\n')

for item in users:
	user_dict = users[item]
	print(f"User: {item}")
	print('		{\n')
	for item in user_dict:
		print(f"    '{item}': {user_dict[item]}")
	print('}\n')






