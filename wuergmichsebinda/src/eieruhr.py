# SuperFastPython.com
import time
from time import sleep
from threading import current_thread, Thread

def gethuebsch(neZeit):
    return str(neZeit.tm_hour)+":"+str(neZeit.tm_min)+":"+str(neZeit.tm_sec)
def eieruhr(arg1, startzeit, arg3):
    thread = current_thread()
    print(f'Daemon thread: {thread.daemon}')
    #print(f'Argumente thread: arg1: {arg1} - arg2: {arg2} - arg3: {arg3}')
    print(f'Stelle Eieruhr: {arg1} um  {gethuebsch(startzeit)} {arg3}')
    print(f'Schlafe: 1')
    sleep(1)
    jetzt=time.localtime(time.time())
    print(f'Aufgewacht: {gethuebsch(jetzt)}')

def bedrohungen():
    my_list = range(1, 10)
    threads = []

    for x in my_list:
        now = time.localtime(time.time())
        threads.append(Thread(target=eieruhr, daemon=True, args=(str(x),now,"")))
    for thread in threads:
        thread.start()
    sleep(22)
    print('Main bedrohungen exiting...')

bedrohungen()
print('Main thread exiting...')