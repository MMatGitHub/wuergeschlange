#!/usr/bin/env python3
import time
import protokolliere
import datetime
import mousemover_xdo
import os_weiche
#import sys

def do(event, queue):
    try:
        isWin=(os_weiche.get_os()==os_weiche.is_win_nt)
        what="Task: robby-spielt-mit-der-Maus"
        gestartet = datetime.datetime.now()
        seit = lambda t: (datetime.datetime.now() - t).total_seconds()
        jetzt  = lambda : (time.strftime("%H:%M:%S", time.localtime()))
        protokolliere.logfile(f"{what} gestartet...")
        i=0
        while True:
            i=i+1
            event.wait(1.0)
            if event.is_set():
                protokolliere.logfile(f"{what} Abbruch-Event received")
                break
            if (isWin):
                protokolliere.logfile(f"Win is to be implemented!")
            else:    
                mousemover_xdo.move_mouse()
            time.sleep(1)
            protokolliere.logfile(f"Schubse weiter {i} auf {jetzt()}...")
        protokolliere.logfile(f"{what} completed without erros.")
    except Exception as e:
        queue.put(f"Fehler: {e}") 
    finally:
        protokolliere.logfile(f"Feierabend! Wachte {seit(gestartet)} Sek. Gehe wieder in meine Hütte. Bis zum nächsten Mal. :-)")
        queue.put(f"Task {what} beendet. Dauer: {seit(gestartet)} sec")
        event.set()