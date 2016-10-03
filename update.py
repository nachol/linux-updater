#!/usr/bin/env python
import os
import subprocess
import os.path
import sys


def banner():
    print """
=========================================================== 
___  ___      _         _   _           _       _            
|  \/  |     (_)       | | | |         | |     | |           
| .  . | __ _ _ _ __   | | | |_ __   __| | __ _| |_ ___ _ __ 
| |\/| |/ _` | | '_ \  | | | | '_ \ / _` |/ _` | __/ _ \ '__|
| |  | | (_| | | | | | | |_| | |_) | (_| | (_| | ||  __/ |   
\_|  |_/\__,_|_|_| |_|  \___/| .__/ \__,_|\__,_|\__\___|_|   
                             | |                             
                             |_|                              
Main Updater
Written by Ignacio Lizaso
===========================================================

    """
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def updateRepos():
	clear()
	print('Updating Distribution...')
	os.system('apt update')
	os.system('apt dist-upgrade -y')

def updateOPT():
	clear()
	print('Updating Apps...')
	dirs = [d for d in os.listdir('/opt/') if os.path.isdir(os.path.join('/opt/', d))]
	for folders in dirs:
		print('/opt/'+folders)
		p = subprocess.Popen(['git','pull'], cwd='/opt/'+folders)
		p.wait()

def noValidOption():
	clear()
	print('Thats not a valid option.')

ans = True
while ans:
    clear()
    banner()
    print """
==Main Updater==
-----------------------------------------------------
[1] Update Repos - Distribution
[2] Update OPT
[3] Update All
[99] Exit/Quit
-----------------------------------------------------
    """
    ans = int(raw_input("Select An Option: "))
    if ans == 1:
        updateRepos()
    elif ans == 2:
        updateOPT()
    elif ans == 3:
        updateRepos()
        updateOPT()
    elif ans == 99:
	sys.exit(0)
    else:
	noValidOption()

