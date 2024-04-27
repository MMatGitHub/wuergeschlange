import time
import os

def do():
    while True:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(f"alive and kiccking {current_time}")
        time.sleep(3)
        printlogfilesize()

def get_human_readable_size(size_bytes):
    """
    Convert size in bytes to human-readable format
    """
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

def printlogfilesize():
    file_path = "./wuerglog.log" 
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        print(f"Dateigroesse: {get_human_readable_size(file_size)} ({file_size} bytes)")
    else:
        print("i: File does not exist.")



if __name__ == "__main__":
    printlogfilesize()