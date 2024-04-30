#!/usr/bin/env python3
import time
import protokolliere
import datetime
import concurrent.futures

def do(wielange):

    protokolliere.info(f"__name__ gestartet...")
    end_time = time.time() + wielange
    
    start_time = datetime.datetime.now() # Record the current time as the starting point
    wieoft = 3

    while not concurrent.futures.Future.cancelled():       
        protokolliere.info(f"__name__ is moving...")
        time.sleep(1)
        wieoft = wieoft -1
        if wieoft<1:
            break
    dauer = datetime.datetime.now() - start_time 
    
    #raise RuntimeError(f"i: Robby arbeitete {dauer.total_seconds()} Sek.Robby sollte {wielange} sec arbeiten.")
    
    return f"i: Robby arbeitete {dauer.total_seconds()} Sek.Robby sollte {wielange} sec arbeiten."
