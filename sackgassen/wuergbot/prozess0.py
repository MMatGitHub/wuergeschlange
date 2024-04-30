import multiprocessing
import time
import prozess1
import prozess2

def monitoring(p1, p2, wielange):
    try:
        while True:
            # Output the current status of prozess1
            print("Status of Prozesses:")
            print("p1 is running" if p1.is_alive() else "p1 is NOT running")
            print("p2 is running" if p2.is_alive() else "p2 is NOT running")
            print(f"sleeping {wielange} seconds...")

            time.sleep(wielange)  # Wait seconds
    except KeyboardInterrupt:
        p1.terminate()
        p2.terminate()


def verarbeite(prozessliste):
    p1=prozessliste[1].start()
    p2=prozessliste[2].start()
    monitoring(p1, p2, 30)