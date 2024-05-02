import multiprocessing
import the_parallel_starter as starter
import protokolliere
import time
import datetime

def selbsttest():
    protokolliere.ok ("i: Starting App...")
    protokolliere.fehler ("i: DAS will ich sehen: Starting App test error...")
    protokolliere.ausnahme ("i: DAS will ich auch sehen: Starting App test exception...")
    protokolliere.warn ("i: DAS will ich doch sehen: Starting App... test warning")
    protokolliere.info ("i: DAS brauch ich nicht sehen: Starting App... info")
    protokolliere.debug ("i: DAS will ich NICHT sehen: Starting App... debug")
    protokolliere.info ("i: Lower than info werden nach logdetails.log ausgegeben")

def display_time_and_greeting():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(f"It is exactly {current_time} now. I am alive {__file__}")

def what_do_you_want(event, queue, question_text):
    try:
        what="menu"
        gestartet = datetime.datetime.now()
        protokolliere.info(f"Task {what} gestartet...")
        while True:
            protokolliere.info(question_text)
            choice = input("> ")      
            event.wait(1.0)
            if event.is_set():
                protokolliere.info(f"Task {what} Abbruch-Event received.")
                break
            protokolliere.info(f"Ihre Eingabe: {choice}")
            return choice.lower()
        protokolliere.info(f"Task {what} completed without erros.")
    except Exception as e:
        queue.put(f"Fehler: {e}") 
    finally:
        queue.put(f"Task {what} beendet. Dauer: {(datetime.datetime.now() - gestartet).total_seconds()} sec")
        event.set()
    
    
def ui_loop():
    c_aus = multiprocessing.Event()
    result_queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=what_do_you_want, args=(c_aus, result_queue, "Was willste?"))
    # Starten
    process.start()
    
    while True:
        if c_aus.is_set:
            break
    
    # Beenden
    c_aus.set()
    protokolliere.info(f"Shutting down...")
    time.sleep(1)

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

def los():
    selbsttest()
    display_time_and_greeting()
    ui_loop()
    #starter.los_any()
    starter.los_all()

if __name__ == '__main__':
    los()