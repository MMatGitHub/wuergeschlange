import multiprocessing
import time
import prozess0

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
    prozess0_handle = multiprocessing.Process(target=prozess0.starte)
    prozess0_handle.start()
    
    # Get process handles
    p1_handle = prozess0.get_prozess1_handle()
    p2_handle = prozess0.get_prozess2_handle()
    
    # Start user interface
    nutzerschnittstelle(p1_handle, p2_handle)


#def nutzerschnittstelle(p1, p2):
#    try:
#        while True:
#            interrupt = input("Interrupt? (yes/no): ")
#            if interrupt.lower() == "yes":
#                p1.terminate()
#                p2.terminate()
#                break
#
#            time.sleep(60)
#    except KeyboardInterrupt:
#        p1.terminate()
#        p2.terminate()


#if __name__ == "__main__":
#    multiprocessing.set_start_method('spawn')
#    prozess0_handle = multiprocessing.Process(target=prozess0)
#    prozess0_handle.start()
#    nutzerschnittstelle(get_prozess1_handle(), get_prozess2_handle())