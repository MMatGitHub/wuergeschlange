import concurrent.futures
import time
import protokolliere
import datetime
def a():
    try:
        what="a"
        gestartet = datetime.datetime.now()
        print(f"Task {what} gestartet...")
        for i in range(1, 7):
            time.sleep(1)  
            protokolliere.info(f"Task {what} continues to run... {i}. time")
        dauer = (datetime.datetime.now() - gestartet)
        return(f"Task {what} beendet. Dauer: {dauer.total_seconds()} sec")
    except NameError:
        print("Variable x is not defined")
    except:
        print("Something else went wrong") 
    finally:
        return(f"Task {what} beendet mit Fehlern")
def b():
    try:
        what="b"
        gestartet = datetime.datetime.now()
        print(f"Task {what} gestartet...")
        for i in range(1, 7):
            time.sleep(1)  
            protokolliere.info(f"Task {what} continues to run... {i}. time")
        dauer = (datetime.datetime.now() - gestartet)
        return(f"Task {what} beendet. Dauer: {dauer.total_seconds()} sec")
    except NameError:
        print("Variable x is not defined")
    except:
        print("Something else went wrong") 
    finally:
        return(f"Task {what} beendet mit Fehlern")
def c():
    try:
        what="c"
        gestartet = datetime.datetime.now()
        print(f"Task {what} gestartet...")
        for i in range(1, 7):
            time.sleep(1)
            if concurrent.futures.current_thread().is_alive():  # Check if the current thread is still alive
                 print("Task C is still running...")
            else:
                print("Task C interrupted.")
                break

            protokolliere.info(f"Task {what} continues to run... {i}. time")
        dauer = (datetime.datetime.now() - gestartet)
        return(f"Task {what} beendet. Dauer: {dauer.total_seconds()} sec")
    except NameError:
        print("Variable x is not defined")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Something else went wrong") 
    finally:
        return(f"Task {what} beendet mit Fehlern")


def los():
    exe = concurrent.futures.ProcessPoolExecutor()
    future_a = exe.submit(a)
    future_b = exe.submit(b)
    future_c = exe.submit(c)

    # Wait for either task 'a', 'b', or 'c' to complete
    completed_futures = concurrent.futures.wait([future_a, future_b, future_c], return_when=concurrent.futures.FIRST_COMPLETED)

    # Cancel the tasks that haven't completed
    for future in completed_futures:
        print(f"Task {future} completed, stopping other tasks...")
        break
        #for remaining_future in [future_a, future_b, future_c]:
           # if remaining_future != future:
             #   remaining_future.cancel()


#    liste = [a, b, c]
#    zukuenftige = []
#    for l in liste:
#        zukuenftige.append(exe.submit(l))
#    protokolliere.info(f"Laufende Prozesse: {len(exe._processes)}")
#    completed_futures, _ = concurrent.futures.wait(zukuenftige, return_when=concurrent.futures.FIRST_COMPLETED)
#    results = []
#    for future in completed_futures:
#        protokolliere.info(f"First task completed, stopping other tasks...")
#        results.append(future.result(timeout=0))
#        for remaining_future in zukuenftige:
#            if remaining_future != future:
#                protokolliere.info(f"Stopping next task...")
#                remaining_future.cancel()
#                results.append(remaining_future.result(timeout=0))
    exe.shutdown(wait=False, cancel_futures=True)

    protokolliere.info("i: Shutting down...")
    protokolliere.info(f"HIER DIE ERGEBNISSLISTE:")
    #for r in results:
        #protokolliere.info(f"{r}")
if __name__ == '__main__':
    los()