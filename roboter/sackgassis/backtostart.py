import multiprocessing
import time

def a(event, queue):
    print("Task A running...")
    event.wait(40.0)
    print("Task A completed.")
    queue.put("aaaa")

def b(event, queue):
    print("Task B running...")
    event.wait(2.0)
    print("Task B completed.")
    event.set()
    queue.put("bbbb")

def c(event, queue):
    print("Task C running...")
    while not event.is_set():
        if event.wait(1.0):
            break
    print("Task C completed.")
    queue.put("cccc")

def los():
    process_completed = multiprocessing.Event()
    result_queue = multiprocessing.Queue()

    process_a = multiprocessing.Process(target=a, args=(process_completed, result_queue))
    process_b = multiprocessing.Process(target=b, args=(process_completed, result_queue))
    process_c = multiprocessing.Process(target=c, args=(process_completed, result_queue))

    processes = [process_a, process_b, process_c]

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    # Terminate other processes
    for process in processes:
        if process.is_alive():
            process.terminate()
            print(f"Process {process.name} terminated.")
    
    # Collect results
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    # Print collected results
    print("Results:")
    for result in results:
        print(result)
    
    print(f"Los() beendet.")

if __name__ == '__main__':
    los()
