import protokolliere
import teste_my_command
from futurejobs import compose_zip_jobs as compose_futurejobs
def selbsttest():
    protokolliere.ok ("i: Starting App...")
    protokolliere.fehler ("i: DAS will ich sehen: Starting App test error...")
    protokolliere.ausnahme ("i: DAS will ich auch sehen: Starting App test exception...")
    protokolliere.warn ("i: DAS will ich doch sehen: Starting App... test warning")
    protokolliere.info ("i: DAS brauch ich nicht sehen: Starting App... info")
    protokolliere.debug ("i: DAS will ich NICHT sehen: Starting App... debug")
    protokolliere.info ("i: Lower than info werden nach logdetails.log ausgegeben")

def testefunctions():
    protokolliere.debug (teste_my_command.teste_hallo_welt())
    protokolliere.debug (teste_my_command.test_ping_inet())
    protokolliere.debug (teste_my_command.test_dir_temp())

def los():
   compose_futurejobs()

if __name__ == '__main__':
    # selbsttest()
    # testefunctions()
    los()
else:
    print ("i: Nichts wurde ausserhalb von __main__ gestartet!")