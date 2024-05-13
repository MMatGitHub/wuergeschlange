#!/usr/bin/env python3
import time
import subprocess
import sys
import protokolliere

def check_xdotool():
    try:
        subprocess.run(['xdotool', '--version'], check=True)
        return True
    except FileNotFoundError:
        protokolliere.kritisch("xdotool scheint nicht installiert zu sein.")
        return False

def move_mouse():
    verzoegerung=1
    if check_xdotool():
        protokolliere.info("Schubse -1,-1")
        subprocess.run(['xdotool', 'mousemove', '-1', '-1'])
        time.sleep(verzoegerung)
        protokolliere.info("Scubse 1,1")
        subprocess.run(['xdotool', 'mousemove_relative', '1', '1'])
        time.sleep(verzoegerung)
    else:
        protokolliere.kritisch("xdotool scheint nicht installiert zu sein.")
        #sys.exit(1)

