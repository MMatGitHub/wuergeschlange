import multiprocessing
import time
import datetime
import protokolliere
import hasso
import robby
import ui

def a(event, queue):
    try:
        what="a"
        dies="Dummy-Task"
        seit = lambda t: (datetime.datetime.now() - t).total_seconds()
        gestartet = datetime.datetime.now()
        protokolliere.info(f"{dies} {what} gestartet.")
        for i in range(1, 99):
            event.wait(1.0)
            if event.is_set():
                protokolliere.logfile(f"{dies} {what} Abbruch-Event received.")
                break
            protokolliere.logfile(f"{dies} {what} continues to run... {i}. time")
        protokolliere.logfile(f"{dies} {what} completed without erros.")
    except Exception as e:
        queue.put(f"Fehler: {e}") 
    finally:
        protokolliere.info(f"{dies} {what} beendet...")
        queue.put(f"{dies} {what} beendet. Dauer: {seit(gestartet)} sec")
        event.set()


def b(event, queue):
    try:
        what="b"
        dies="Dummy-Task"
        seit = lambda t: (datetime.datetime.now() - t).total_seconds()
        gestartet = datetime.datetime.now()
        protokolliere.info(f"{dies} {what} gestartet...")
        for i in range(1, 88):
            event.wait(1.0)
            if event.is_set():
                protokolliere.logfile(f"{dies} {what} Abbruch-Event received.")
                break
            protokolliere.logfile(f"{dies} {what} continues to run... {i}. time")
        dauer = (datetime.datetime.now() - gestartet)
        protokolliere.logfile(f"{dies} {what} completed without erros.")
    except Exception as e:
        queue.put(f"Fehler: {e}") 
    finally:
        protokolliere.info(f"{dies} {what} beendet...")
        queue.put(f"{dies} {what} beendet. Dauer: {seit(gestartet)} sec")
        event.set()
    
def c(event, queue):
    try:
        dies="Dummy-Task"
        what="c"
        seit = lambda t: (datetime.datetime.now() - t).total_seconds()
        gestartet = datetime.datetime.now()
        protokolliere.info(f"{dies} {what} gestartet...")
        for i in range(1, 77):
            event.wait(1.0)
            if event.is_set():
                protokolliere.logfile(f"{dies} {what} Abbruch-Event received.")
                break
            protokolliere.logfile(f"{dies} {what} continues to run... {i}. time")
        protokolliere.logfile(f"{dies} {what} completed without erros.")
    except Exception as e:
        queue.put(f"Fehler: {e}") 
    finally:
        protokolliere.info(f"{dies} {what} beendet...")
        queue.put(f"{dies} {what} beendet. Dauer: {seit(gestartet)} sec")
        event.set()


def los(yes_any):    
    a_aus = multiprocessing.Event()
    b_aus = multiprocessing.Event()
    c_aus = multiprocessing.Event()
    robby_aus = multiprocessing.Event()
    process_aus = [a_aus, b_aus,c_aus, robby_aus]
    hasso_aus = multiprocessing.Event()
    ui_aus = multiprocessing.Event()
    result_queue = multiprocessing.Queue()

    process_a = multiprocessing.Process(target=a, args=(a_aus, result_queue))
    process_b = multiprocessing.Process(target=b, args=(b_aus, result_queue))
    process_c = multiprocessing.Process(target=c, args=(c_aus, result_queue))
    process_robby = multiprocessing.Process(target=robby.do, args=(robby_aus, result_queue))
    process_hasso = multiprocessing.Process(target=hasso.do, args=(hasso_aus, result_queue))
    process_ui = multiprocessing.Process(target=ui.do, args=(ui_aus, result_queue))
    processes = [process_a, process_b, process_c, process_robby]
    # Starten
    process_hasso.start()
    for process in processes:
        process.start()

    # Start UI process later...
    ui_gestartet= False

    # Überwachen
    while True:
        if not ui_gestartet:
            ui.do(ui_aus, result_queue)
            ui_gestartet=True
        if yes_any:
            any_process_completed = any(flag.is_set() for flag in process_aus)
            if any_process_completed:
                hasso_aus.set()
            if hasso_aus.is_set():
                break
            if ui_aus.is_set():
                break
        else:
            all_processes_completed = all(flag.is_set() for flag in process_aus)
            if all_processes_completed:
                break
            if hasso_aus.is_set():
                break
            if ui_aus.is_set():
                break
    # Beenden
    for flag in process_aus:
        flag.set()
    hasso_aus.set()  
    ui_aus.set()    
    protokolliere.logfile(f"Shutting down...")
    time.sleep(1)

    if process_hasso.is_alive():
            process_hasso.terminate()
            protokolliere.logfile(f"Process Hasso terminated.")
    if process_ui.is_alive():
            process_ui.terminate()
            protokolliere.logfile(f"Process UI terminated.")
    for process in processes:
        if process.is_alive():
            process.terminate()
            protokolliere.logfile(f"Process {process.name} terminated.")
    
    # Collect results
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    protokolliere.logfile("Ergebnisse:")
    for result in results:
        protokolliere.logfile(result)
    
    protokolliere.logfile(f"Los() beendet.")

def los_any():
    protokolliere.logfile(f"Warte auf den ersten beendeten Prozess...")
    los(True)

def los_all():
    protokolliere.logfile(f"Warte bis alle Prozesse  beendet sind...")
    los(False)

if __name__ == '__main__':
    #los_any()
    los_all()
