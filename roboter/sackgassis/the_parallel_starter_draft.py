import multiprocessing
import time
import datetime
import protokolliere
def a(event, queue):
    try:
        what="a"
        gestartet = datetime.datetime.now()
        protokolliere.info(f"Task {what} gestartet...")
        for i in range(1, 7):
            event.wait(1.0)
            if event.is_set():
                protokolliere.info(f"Task {what} Abbruch-Event received.")
                break
            protokolliere.info(f"Task {what} continues to run... {i}. time")
        dauer = (datetime.datetime.now() - gestartet)
        event.set()
        protokolliere.info(f"Task {what}completed without erros.")
    except Exception as e:
        queue.put(f"Fehler: {e}") 
    finally:
        queue.put(f"Task {what} beendet. Dauer: {dauer.total_seconds()} sec")


def b(event, queue):
    try:
        what="b"
        gestartet = datetime.datetime.now()
        protokolliere.info(f"Task {what} gestartet...")
        for i in range(1, 5):
            event.wait(1.0)
            if event.is_set():
                protokolliere.info(f"Task {what} Abbruch-Event received.")
                break
            protokolliere.info(f"Task {what} continues to run... {i}. time")
        dauer = (datetime.datetime.now() - gestartet)
        event.set()
        protokolliere.info(f"Task {what}completed without erros.")
    except Exception as e:
        queue.put(f"Fehler: {e}") 
    finally:
        queue.put(f"Task {what} beendet. Dauer: {dauer.total_seconds()} sec")


#def b(event, queue):
#    print("Task B running...")
#    event.wait(5.0)
#    print("Task B completed.")
#    event.set()
#    queue.put("bbbb")

def c(event, queue):
    try:
        what="c"
        gestartet = datetime.datetime.now()
        protokolliere.info(f"Task {what} gestartet...")
        for i in range(1, 22):
            event.wait(1.0)
            if event.is_set():
                protokolliere.info(f"Task {what} Abbruch-Event received.")
                break
            protokolliere.info(f"Task {what} continues to run... {i}. time")
        dauer = (datetime.datetime.now() - gestartet)
        event.set()
        protokolliere.info(f"Task {what}completed without erros.")
    except Exception as e:
        queue.put(f"Fehler: {e}") 
    finally:
        queue.put(f"Task {what} beendet. Dauer: {dauer.total_seconds()} sec")

#def c(event, queue):
#    print("Task C running...")
#    while not event.is_set():
#        if event.wait(1.0):
#            break
#    print("Task C completed.")
#    queue.put("cccc")

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
            protokolliere.info(f"Process {process.name} terminated.")
    
    # Collect results
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    # Print collected results
    print("Results:")
    for result in results:
        print(result)
    
    protokolliere.info(f"Los() beendet.")

if __name__ == '__main__':
    los()
