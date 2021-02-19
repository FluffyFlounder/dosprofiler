# Requirements

Python3 or greater, built using python 3.8.5
THIS PROGRAM IS DESIGNED FOR MAC ONLY, WINDOWS NOT EXCEPETED TO RUN

#  Setup.py Installation Instructions

Run setup.py for an automatic installation of all dependencies and packages:
    
    python3 setup.py
 
If an error occurs, try a manual installation.

# Manual Installation

If the above script didn't work, trying a manual installation maybe work.

First double check you are running python3:

    python3 --version

CD into the dosprofiler-main folder:

    cd /path/to/folder/dosprofiler-main

Next, install the extra packages in requirements.txt:

    pip3 install configparser
    
Run clean.py to generate a new data file:

    python3 clean.py
    
Give the folder executable privileges:

    cd .. && sudo chmod +x dosprofiler-main/* && cd dosprofiler-main
    
# Commands

Run 'help' inside while the program is running to see a list of commands.
