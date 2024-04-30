#!/usr/bin/env python3
import multiprocessing
import time
import subprocess
import sys

def check_xdotool():
    try:
        subprocess.run(['xdotool', '--version'], check=True)
        return True
    except FileNotFoundError:
        return False

def move_mouse(stop_event):
    if check_xdotool():
        while not stop_event.is_set():
            subprocess.run(['xdotool', 'mousemove', '0', '0'])
            time.sleep(0.1)
            subprocess.run(['xdotool', 'mousemove_relative', '1', '1'])
            time.sleep(0.1)
    else:
        print("xdotool is not installed.")
        install_xdotool = input("Do you want to install xdotool? (yes/no): ")
        if install_xdotool.lower().startswith('y'):
            try:
                subprocess.run(['sudo', 'apt', 'install', 'xdotool'], check=True)
                print("xdotool has been successfully installed.")
            except subprocess.CalledProcessError:
                print("Failed to install xdotool.")
                sys.exit(1)
        else:
            print("You chose not to install xdotool. Exiting.")
            sys.exit(1)

