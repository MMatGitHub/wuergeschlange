import concurrent.futures
import jobs
import watchdog
import protokolliere

def wait_for_all_jobs_to_have_been_finished(aufgabenliste, when_all_or_first):
    print(f"i: Waiting for jobs...until :[{when_all_or_first}]")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        watchdog_future = executor.submit(watchdog.do) 
        futures = [executor.submit(aufgabe.do) for aufgabe in aufgabenliste]
        #concurrent.futures.wait(futures, return_when=when_all_or_first)
    result = combine_with_watchdog(futures, watchdog_future)
    protokolliere.info(f"Combined result: {result}")


def combine_with_watchdog(job_futures, hasso):
    # Wait for either any job to complete or the watchdog to trigger
    done, _ = concurrent.futures.wait(job_futures + [hasso], return_when=concurrent.futures.FIRST_COMPLETED)

    results = []

    if not hasso.done():
        hasso.cancel()
        results.append(hasso.result())
        protokolliere.info('i: Hasso: "Wuff" - war was? Ich geh wieder schlafen.')
    else:
        protokolliere.info('i: Beendet! Hasso hat aufgepasst!')
    
    i=0
    for future in job_futures:
        if not future.done():
            protokolliere.info(f"i: future {i} wird abgebrochen...")
            future.cancel()
            protokolliere.info("future lief noch:", future._callable_name)
            protokolliere.info(f"i: future {i} wurde beendet.")
        else:
            protokolliere.info(f"future war {i} bereits beendet:")
        i=i+1
        results.append(future.result())
    return results

    # If the watchdog triggered, cancel all remaining job futures
#    if hasso in done:
#        for future in job_futures:
#            future.cancel()
#        return hasso.result()

    # Get the result of the first completed future
#    first_completed_future = done.pop()

    # Return the result of the first completed future
#    return first_completed_future.result()

