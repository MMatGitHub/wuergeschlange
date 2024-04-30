import time
import os

def verarbeite():
    while True:
        os.system("ls / >> wuerglog.log 2>&1")

if __name__ == "__main__":
    verarbeite()
