import protokolliere
import teste_my_command
import threading
import concurrent.futures
from konst import KONST
from futurejobs import compose_zip_repo_jobs
from futurejobs import compose_noup_down_ip_jobs
from futurejobs import compose_upcshare_sec_jobs
from futurejobs import compose_ulc_topsec_jobs
from folderio import test_availability
from konst import KONST
from foldermonitor import monitor_directory
from foldermonitor import BeendeMichJetzt

def selbsttest():
    protokolliere.ok ("i: Starting App...")
    protokolliere.fehler ("i: DAS will ich sehen: Starting App test error...")
    protokolliere.ausnahme ("i: DAS will ich auch sehen: Starting App test exception...")
    protokolliere.warn ("i: DAS will ich doch sehen: Starting App... test warning")
    protokolliere.info ("i: DAS brauch ich nicht sehen: Starting App... info")
    protokolliere.debug ("i: DAS will ich NICHT sehen: Starting App... debug")
    protokolliere.info ("i: Lower than info werden nach logdetails.log ausgegeben")

def konststest():
    protokolliere.debug ("APP_NAME: "+KONST.APP_NAME)
    protokolliere.debug ("LOCALHOME: "+KONST.LOCALHOME)
    protokolliere.debug ("U_home: "+KONST.U_home)
    protokolliere.debug ("H_home: "+KONST.H_home)

def availabilitytest():
    try:
        test_availability(KONST.NON_EXISTING_PATH)
    except:
        protokolliere.debug (f"i: AVAILABILITY CHECK: [OK]")    
    test_availability(KONST.LOCALHOME)
    test_availability(KONST.H_home)
    test_availability(KONST.U_home)
  

def testefunctions():
    protokolliere.debug (teste_my_command.teste_hallo_welt())
    protokolliere.debug (teste_my_command.test_ping_inet())
    protokolliere.debug (teste_my_command.test_dir_temp())

def los():
    protokolliere.info (KONST.GREETING)
    protokolliere.info ("i: Starte full BACKUP")
    #compose_zip_repo_jobs()
    #compose_noup_down_ip_jobs()
    #compose_upcshare_sec_jobs()
    #monitor_thread_local = threading.Thread(target=monitor_directory, args=(KONST.LOCALHOME,))
    #monitor_thread_archiv = threading.Thread(target=monitor_directory, args=(KONST.BACKUP_TARGET,))
    #monitor_thread_local.start()
    #monitor_thread_archiv.start()

    #with concurrent.futures.ThreadPoolExecutor() as executor:
    #    monitore = executor.submit(monitor_directory, KONST.LOCALHOME)

    compose_ulc_topsec_jobs()
   
   # BeendeMichJetzt()
    #future.result() # This will wait for the thread to finish
    #monitor_thread_local.join()
    #monitor_thread_archiv.join()
    
if __name__ == '__main__':
    selbsttest()
    # testefunctions()
    availabilitytest()
    los()
else:
    print ("i: Nichts wurde ausserhalb von __main__ gestartet!")