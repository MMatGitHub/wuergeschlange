import time

mit = None
algorithmus = None

def do():
    print(f"i: {__name__}: doing({mit})...")
    time.sleep(2)  # Simulating some work
    print(f"i: [{algorithmus(mit)}] executed.")