import multiprocessing
import time
import prozess0
import prozess1
import prozess2

def nutzerschnittstelle(process_list):
    try:
        while True:
            interrupt = input("Interrupt? (yes/no): ")
            if interrupt.lower() == "yes":
                # Send termination signal to processes
                for process in process_list:
                    process.terminate()
                break
    except KeyboardInterrupt:
        for process in process_list:
            process.terminate()

if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')
    
    # Create a multiprocessing Manager to manage the list
    manager = multiprocessing.Manager()
    process_list = manager.list()
    
    # Start process 0
    p0_handle = multiprocessing.Process(target=prozess0.verarbeite)
    p1_handle = multiprocessing.Process(target=prozess1.verarbeite)
    p2_handle = multiprocessing.Process(target=prozess2.verarbeite)
    process_list.append(p1_handle)
    process_list.append(p2_handle)

    p0_handle.start(p0_handle)

    process_list.append(p0_handle)  # Store process handle in the list
    
    nutzerschnittstelle(process_list, p1_handle, p2_handle)