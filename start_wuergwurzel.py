import os
import sys
path = os.getcwd()
print('i: Loading '+ str(__file__))
print("i: PYTHONPATH: " + str(sys.path))
print("i: Current Dir: " + str(path))

scriptdir=os.path.dirname(os.path.abspath(__file__))
print("Scriptdir: "+str(scriptdir))

print("i: Appending PYTHONPATH: I " + str(sys.path))
sys.path.append(".\\wuergwurzel\\src")
print("i: Adapted PYTHONPATH: II " + str(sys.path))

import wuergwurzel.src.main as starte

def los():
    starte.main()
los()
