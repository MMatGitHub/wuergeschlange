import multiprocessing
import the_parallel_starter as starter
import protokolliere
import time
import datetime
import app    

appname ="robby"

#def display_time_and_greeting():
#    current_time = time.strftime("%H:%M:%S", time.localtime())
#    print(f"It is exactly {current_time} now. I am alive {__file__}")

#def what_do_you_want(question_text):
#    try:
#        what="menu"
#        gestartet = datetime.datetime.now()
#        protokolliere.info(f"Task {what} gestartet...")
#        while True:
#            protokolliere.info(question_text)
#            choice = input("Ihre Eingabe: > ")      
#            protokolliere.info(f"Ihre Eingabe: {choice}")
#            return choice.lower()
#        protokolliere.info(f"Task {what} completed without erros.")
#    except Exception as e:
#        protokolliere.fehler(f"Fehler: {e}") 
#    finally:
#        protokolliere.info(f"Task {what} beendet...")
#        protokolliere.logfile(f"Task {what} beendet. Dauer: {(datetime.datetime.now() - gestartet).total_seconds()} sec")

def eval_user_input(event, eingabe):
    if eingabe is None or eingabe.strip() == "":
        protokolliere.warn("OK: Ungültige Eingabe - Kein Abbruch!")
        return
    protokolliere.info(f"Ihre Eingabe war: [{eingabe}]")
    if eingabe.lower().startswith('y'):
        event.set()
    elif eingabe.lower().startswith('j'):
        event.set()
    else:
        protokolliere.warn("OK: Kein Abbruch!")

def do(event, queue):
    protokolliere.info(f"Willkommen beim {appname}-Menu")
    what="ui"
    gestartet = datetime.datetime.now()
    seit = lambda t: (datetime.datetime.now() - t).total_seconds()
    protokolliere.logfile(f"Task {what} gestartet...")
    try:
        protokolliere.info(f"Task {what} gestartet...")
        while True:
            event.wait(1.0)
            if event.is_set():
                protokolliere.logfile(f"Task {what} Abbruch-Event received.")
                break
            protokolliere.info(f"Abbruch aller Tasks mit 'ja' [j*] oder 'yes' [y*]")
            eingabe = input("Ihre Eingabe: ")
            eval_user_input(event, eingabe)
        protokolliere.logfile(f"Task {what} completed without erros.")
    except Exception as e:
        queue.put(f"Fehler: {e}") 
    finally:
        protokolliere.logfile(f"Feierabend for {what} {seit(gestartet)} Sek. ")
        queue.put(f"Task {what} beendet. Dauer: {seit(gestartet)} sec")
        event.set()


def los():
    do()
    protokolliere.logfile(f"Los() beendet.")

if __name__ == '__main__':
    los()