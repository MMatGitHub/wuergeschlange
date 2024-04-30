import os
import time
from konst import KONST
import protokolliere

JA_BEENDEMICH=False

def format_filesize(size_in_bytes):
    units = ['B', 'kB', 'MB', 'GB', 'TB']
    
    size = float(size_in_bytes)
    i = 0
    
    while size >= 1024 and i < len(units) - 1:
        size /= 1024
        i += 1
        
    return f"{size:.2f} {units[i]}"

def monitor_directory(path):    
    prev_sizes = {}
    slidingwindow=30    
    while True:
        # Get a list of files in the directory
        protokolliere.debug (f"i: Nach {slidingwindow}s dir [{path}]")
        files = os.listdir(path)
        
        # Calculate size differences for each file
        size_diff=0
        curr_size=0

        for file in files:
            file_path = os.path.join(path, file)
            
            if os.path.isfile(file_path):
                curr_size = os.path.getsize(file_path)
                
                # Check if the file was seen before
                if file in prev_sizes:
                    size_diff = curr_size - prev_sizes[file]
                    
                    # Print the size difference if it's not zero
                    if size_diff != 0:
                        protokolliere.info(f"CHG: {file}: {format_filesize(size_diff)}")
                        rate = (size_diff/slidingwindow)*(60/slidingwindow)
                        protokolliere.info(f"SPEED: {format_filesize(rate)} per Minute")
                        
                else:
                    # First time seeing this file, store its size
                    prev_sizes[file] = curr_size
                    protokolliere.info(f"NEW: {file}: {format_filesize(curr_size)}")
       
             # Update the current size in the dictionary regardless of change
                prev_sizes[file] = curr_size

        if JA_BEENDEMICH: # Check the stop flag each iteration
            protokolliere.info(f"JA BEENDE MICH:{JA_BEENDEMICH}, wird beendet!")
            break
        protokolliere.debug (f"i: Sleeping...for {slidingwindow} sec")
        time.sleep(slidingwindow)

def BeendeMichJetzt():
    JA_BEENDEMICH=True

#user_input = input("Do you want to continue? (y/n): ")
#        if user_input.lower() != 'y':
 #           break

# monitor_directory(KONST.BACKUP_TARGET)