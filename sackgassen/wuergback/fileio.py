import os
import json
import protokolliere

def slurp_verbose(file_path):
    gelesen = do_slurp(file_path)
    protokolliere.debug(f"Gelesen [{file_path}]: Inhalt: {gelesen}")

def slurp(file_path):
    gelesen = do_slurp(file_path)
    if gelesen: 
        return gelesen
    else: 
        raise NameError ("Fehler beim Lesen einer Datei")
def do_slurp(file_path):
    try:
        contents = "e: File not found"
        #with contextmanager => autoclosing
        with open(file_path, 'r') as file: #r stands for read
            contents = file.read()
    except FileNotFoundError:
        protokolliere.warn(f"File not found:[{file_path}]")
    else:
        protokolliere.debug(f"File gelesen:[{file_path}]")
    return contents

def slurp_json(file_path):
    try:
        contents = "e: File not found"
        with open(file_path, 'r') as file:
            contents = json.load(file)
    except FileNotFoundError:
        protokolliere.warn(f"File not found:[{file_path}]")
    else:
        protokolliere.debug(f"Gelesen [{file_path}]: Inhalt: {contents}")
    return contents