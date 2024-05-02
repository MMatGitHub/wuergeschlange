import time
import os
import protokolliere
import datetime
import typcheck
import threading

def do(event, queue):
    try:
        what="Hasso"
        gestartet = datetime.datetime.now()
        seit = lambda t: (datetime.datetime.now() - t).total_seconds()
        jetzt  = lambda : (time.strftime("%H:%M:%S", time.localtime()))
        protokolliere.info(f"Task {what} gestartet...")
        wielange=5.0
        timer_thread = threading.Thread(target=timer_task, args=(event, wielange,))
        timer_thread.start()
        protokolliere.info(f"Task {what} passt auf für {wielange} sec ...")


        i=0
        while True:
            i=i+1
            event.wait(1.0)
            if event.is_set():
                protokolliere.info(f"Task {what} Abbruch-Event received")
                break
            #time.sleep(1)
            protokolliere_logfilesize("./roboter.log")
            protokolliere.info(f"Passe weiter {i} auf {jetzt()}...")
        protokolliere.info(f"Task {what} completed without erros.")
    except Exception as e:
        queue.put(f"Fehler: {e}") 
    finally:
        protokolliere.info(f"Feierabend! Wachte {seit(gestartet)} Sek. Gehe wieder in meine Hütte. Bis zum nächsten Mal. :-)")
        queue.put(f"Task {what} beendet. Dauer: {seit(gestartet)} sec")
        event.set()



def timer_task(event, duration):
    time.sleep(duration)
    event.set()
    protokolliere.info(f"WUFF: Abbruch - Alarm - Alles wird abgebrochen: Das sollte nur max. {duration} sec. dauern!")



def get_human_readable_size(size_bytes):
    if size_bytes == 0:
        return "0B"

    # Define the units and their corresponding suffixes
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    
    # Determine the appropriate unit for the size
    unit_index = 0
    while size_bytes >= 1024 and unit_index < len(units) - 1:
        size_bytes /= 1024
        unit_index += 1
    
    # Format the size with the appropriate unit
    return "{:.2f} {}".format(size_bytes, units[unit_index])

def protokolliere_logfilesize(logfilename):
    file_path = typcheck.verified_filepath(logfilename)
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        protokolliere.info(f"Dateigroesse: {get_human_readable_size(file_size)} ({file_size} bytes)")
    else:
        protokolliere.info("i: File does not exist.")

if __name__ == "__main__":
    protokolliere_logfilesize("./roboter.log")