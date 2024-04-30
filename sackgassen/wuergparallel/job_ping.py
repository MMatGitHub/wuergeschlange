import time
import protokolliere
mit = None
algorithmus = None

def do():
    protokolliere.info(f"i: {__name__}: doing({mit})...")
    time.sleep(2)  # Simulating some work
    protokolliere.info(f"i: [{algorithmus(mit)}] executed.")