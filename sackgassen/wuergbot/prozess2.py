import time
import os

def verarbeite():
    while True:
        os.system("ping google -c 6000  >> wuerglog.log 2>&1")

if __name__ == "__main__":
    verarbeite()
