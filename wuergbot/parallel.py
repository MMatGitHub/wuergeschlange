import multiprocessing
import time
import prozess0
from prozess0 import get_prozess1_handle
from prozess0 import get_prozess2_handle

def nutzerschnittstelle(p1, p2):
    try:
        while True:
            interrupt = input("Interrupt? (yes/no): ")
            if interrupt.lower() == "yes":
                p1.terminate()
                p2.terminate()
                break

            time.sleep(60)
    except KeyboardInterrupt:
        p1.terminate()
        p2.terminate()


if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')
    prozess0_handle = multiprocessing.Process(target=prozess0)
    prozess0_handle.start()
    nutzerschnittstelle(get_prozess1_handle, get_prozess2_handle)