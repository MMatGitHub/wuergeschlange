import multiprocessing
import time
import datetime
import protokolliere
import hasso
def a(event, queue):
    try:
        what="a"
        gestartet = datetime.datetime.now()
        protokolliere.info(f"Task {what} gestartet...")
        for i in range(1, 2):
            event.wait(1.0)
            if event.is_set():
                protokolliere.info(f"Task {what} Abbruch-Event received.")
                break
            protokolliere.info(f"Task {what} continues to run... {i}. time")
        dauer = (datetime.datetime.now() - gestartet)
        protokolliere.info(f"Task {what} completed without erros.")
    except Exception as e:
        queue.put(f"Fehler: {e}") 
    finally:
        queue.put(f"Task {what} beendet. Dauer: {dauer.total_seconds()} sec")
        event.set()


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
        protokolliere.info(f"Task {what} completed without erros.")
    except Exception as e:
        queue.put(f"Fehler: {e}") 
    finally:
        queue.put(f"Task {what} beendet. Dauer: {dauer.total_seconds()} sec")
        event.set()

def c(event, queue):
    try:
        what="c"
        gestartet = datetime.datetime.now()
        protokolliere.info(f"Task {what} gestartet...")
        for i in range(1, 12):
            event.wait(1.0)
            if event.is_set():
                protokolliere.info(f"Task {what} Abbruch-Event received.")
                break
            protokolliere.info(f"Task {what} continues to run... {i}. time")
        dauer = (datetime.datetime.now() - gestartet)
        protokolliere.info(f"Task {what} completed without erros.")
    except Exception as e:
        queue.put(f"Fehler: {e}") 
    finally:
        queue.put(f"Task {what} beendet. Dauer: {dauer.total_seconds()} sec")
        event.set()

def los(yes_any):    
    a_aus = multiprocessing.Event()
    b_aus = multiprocessing.Event()
    c_aus = multiprocessing.Event()
    process_aus = [a_aus, b_aus,c_aus]
    hasso_aus = multiprocessing.Event()
    result_queue = multiprocessing.Queue()

    process_a = multiprocessing.Process(target=a, args=(a_aus, result_queue))
    process_b = multiprocessing.Process(target=b, args=(b_aus, result_queue))
    process_c = multiprocessing.Process(target=c, args=(c_aus, result_queue))
    process_hasso = multiprocessing.Process(target=hasso.do, args=(hasso_aus, result_queue))
    processes = [process_a, process_b, process_c]
    # Starten
    process_hasso.start()
    for process in processes:
        process.start()
    
    # Überwachen
    if yes_any:
        while True:
            any_process_completed = any(flag.is_set() for flag in process_aus)
            if any_process_completed:
                hasso_aus.set()
            if hasso_aus.is_set():
                break
    else:
        while True:
            all_processes_completed = all(flag.is_set() for flag in process_aus)
            if all_processes_completed:
                break
            if hasso_aus.is_set():
                break

    # Beenden
    for flag in process_aus:
        flag.set()
    hasso_aus.set()    
    protokolliere.info(f"Shutting down...")
    time.sleep(1)

    if process_hasso.is_alive():
            process_hasso.terminate()
            protokolliere.info(f"Process Hasso terminated.")

    for process in processes:
        if process.is_alive():
            process.terminate()
            protokolliere.info(f"Process {process.name} terminated.")
    
    # Collect results
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    protokolliere.info("Ergebnisse:")
    for result in results:
        protokolliere.info(result)
    
    protokolliere.info(f"Los() beendet.")

def los_any():
    protokolliere.info(f"Warte auf den ersten beendeten Prozess...")
    los(True)

def los_all():
    protokolliere.info(f"Warte bis alle Prozesse  beendet sind...")
    los(False)

if __name__ == '__main__':
    #los_any()
    los_all()
