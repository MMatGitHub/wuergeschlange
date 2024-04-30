import time
import os
import protokolliere
import datetime
import typcheck
import concurrent.futures
def do(wieoft):
    i=0
    start_time = datetime.datetime.now() # Record the current time as the starting point
    while not concurrent.futures.Future.cancelled():
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        protokolliere.info(f"alive and kicking {current_time}")
        time.sleep(1)
        i=i+1
        printlogfilesize("./roboter.log")
        if (i>wieoft):
            dauer = datetime.datetime.now() - start_time # Calculate the time difference
            #raise RuntimeError(f"i: Abbruch durch Hasso! Wachte {dauer.total_seconds()} Sek. Jetzt ist gut. :-)")
            return(f"i: Abbruch durch Hasso! Wachte {dauer.total_seconds()} Sek. Jetzt ist gut. :-)")

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

def printlogfilesize(logfilename):
    file_path = typcheck.verified_filepath(logfilename)
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        protokolliere.info(f"Dateigroesse: {get_human_readable_size(file_size)} ({file_size} bytes)")
    else:
        protokolliere.info("i: File does not exist.")

if __name__ == "__main__":
    printlogfilesize("./roboter.log")