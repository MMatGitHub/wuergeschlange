import concurrent.futures
import jobs

def wait_for_all_jobs_to_have_been_finished(aufgabenliste, when_all_or_first):
    print(f"i: Waiting for jobs...until :[{when_all_or_first}]")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(aufgabe.do) for aufgabe in aufgabenliste]
        
        concurrent.futures.wait(futures, return_when=when_all_or_first)

