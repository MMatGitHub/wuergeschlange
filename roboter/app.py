import concurrent.futures
import time
import robby
import hasso
import protokolliere

def los():
    liste = [hasso.do, robby.do]
    with concurrent.futures.ProcessPoolExecutor() as executor:

        zukuenftige = []
        zukuenftige.append(executor.submit(hasso.do, 10))
        zukuenftige.append(executor.submit(robby.do, 2))
        #zukuenftige = [executor.submit(zukuenftig) for zukuenftig in liste]
        time.sleep(1)
        protokolliere.info(f"Number of running processes: {len(executor._processes)}") 
        concurrent.futures.wait(zukuenftige, return_when=concurrent.futures.FIRST_COMPLETED)
        
        executor.shutdown(wait=False, cancel_futures=True)
        protokolliere.info(f"SHUTDOWN: !!!")
        i=0
        results =[]
        for z in zukuenftige:
            if z.done():
                if i==0:
                    protokolliere.info('i: Beendet! Hasso hat aufgepasst. Wuff!')
            else:
                if i==0:
                    protokolliere.info('i: Hasso: "Wuff" - war was? Ich geh wieder schlafen.')
            z.cancel()
            protokolliere.info(f"i: future {i} wird abgebrochen...")
            i=i+1
            results.append(z.result())

    return results







#with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
   #'' future1 = executor.submit(robby.do(5))
   #'' future2 = executor.submit(hasso.do())
    
    
    # Wait for a few seconds to let the scripts start running
 #   time.sleep(1)

  #  print("Number of running processes:", len(executor._processes)) 
  
if __name__ == "__main__":
    resultat=los()
    #protokolliere.info(f"ERGEBNISSE: {los()}")