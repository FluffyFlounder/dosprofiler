import os
import time
print("Welcome to DosProfiler, running intial setup installation scripts...")
os.system('cd .. && chmod +x dosprofiler-main/*')
os.system('cd .. && chmod +x dosprofiler*')
print('Folder granted executable access.')
time.sleep(0.3)
os.system('python3 clean.py skip')
print('Running clean.py, generating new .dat file...')
time.sleep(0.3)
print('Installing requirements.txt...')
os.system('pip3 install -r requirements.txt')
time.sleep(0.3)
print('Done.')