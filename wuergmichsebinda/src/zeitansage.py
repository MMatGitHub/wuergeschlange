import time 
import threading
# SuperFastPython.com
from threading import Timer
from time import sleep
# target task function
def task(message):
    # report the custom message
    print(message)

def eieruhr():
    timer = Timer(3, task, args=('Hello world',))
    timer.start()
    print('Waiting for the timer...')
    sleep(12)   
def print_message():
    print("This message will be printed every 3 seconds.")

def zeitsteuerung():
    print("Running zeitsteuerung")
    for i in range(1,11):
        print("Stelle Eieruhr"+str(i))
        eieruhr
 
if __name__ == '__main__':
    print("Running as main script")
    zeitsteuerung()
else:
    print("Importing as a module")