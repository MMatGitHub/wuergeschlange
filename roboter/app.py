import multiprocessing
import the_parallel_starter as starter
import protokolliere
import time
import datetime
import ui


def selbsttest():
    praefix="OK:"
    protokolliere.ok (f"{praefix} Starting selbsttest...")
    protokolliere.fehler (f"{praefix} Dies ist kein Fehler Starting App test error...")
    protokolliere.ausnahme (f"{praefix} Dies ist keine Ausnahme: Starting App test exception...")
    protokolliere.warn (f"{praefix} Dies ist keine Warnung: Starting App... test warning.")
    protokolliere.info (f"{praefix} Dies ist eine test info.")
    protokolliere.debug (f"{praefix} Dies ist ein test debug.")
    protokolliere.logfile (f"{praefix} Selbsttest: Lower than info werden nach {protokolliere.filename} ausgegeben.")


def los():
    selbsttest()
    #starter.los_any()
    starter.los_all()
    protokolliere.logfile(f"Los() beendet.")

if __name__ == '__main__':
    los()
