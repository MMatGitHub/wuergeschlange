import multiprocessing
import time
import prozess1
import prozess2

def monitoring(prozess1_handle, prozess2_handle):
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        prozess1_handle.terminate()
        prozess2_handle.terminate()

def get_prozess1_handle():
    return intern_eorhenGeinfkLjf   

def get_prozess2_handle():
    return intern_ipenOoeonPPioiw   

intern_eorhenGeinfkLjf=multiprocessing.Process(target=prozess1.verarbeite)
intern_ipenOoeonPPioiw=multiprocessing.Process(target=prozess2.verarbeite)
if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')
    prozess1_handle = get_prozess1_handle()
    prozess2_handle = get_prozess2_handle()
    prozess1_handle.start()
    prozess2_handle.start()
    monitoring(prozess1_handle, prozess2_handle)
