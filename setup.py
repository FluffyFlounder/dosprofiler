import os

print("Welcome to DosProfiler, running intial setup installation scripts...")
os.system('cd .. && sudo chmod +x DosProfiler/*')
os.system('cd .. && sudo chmod +x DosProfiler-main/*')
os.system('python3 clean.py skip')
print('Reading to launch...')