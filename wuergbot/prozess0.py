import multiprocessing
import time
import prozess1
import prozess2

def monitoring(p1, p2):
    try:
        while True:
            # Output the current status of prozess1
            print("Status of prozess1:")
            print("Status of prozess1 is Running" if p1.is_alive() else "p1 is NOT running")

            # Output the current status of prozess2
            print("Status of prozess2:")
            print("Running" if p2.is_alive() else "p2 is NOT running")

            time.sleep(30)  # Wait for 30 seconds before checking again
    except KeyboardInterrupt:
        p1.terminate()
        p2.terminate()

def get_prozess1_handle():
    return intern_eorhenGeinfkLjf   

def get_prozess2_handle():
    return intern_ipenOoeonPPioiw   

def starte():
    prozess1_handle = get_prozess1_handle()
    prozess2_handle = get_prozess2_handle()
    prozess1_handle.start()
    prozess2_handle.start()
    monitoring(prozess1_handle, prozess2_handle)

intern_eorhenGeinfkLjf=multiprocessing.Process(target=prozess1.verarbeite)
intern_ipenOoeonPPioiw=multiprocessing.Process(target=prozess2.verarbeite)
if __name__ == "__main__":
    starte()
