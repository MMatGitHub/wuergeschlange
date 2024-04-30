import concurrent.futures
from dataclasses import dataclass
from typing import Any, Optional

#https://how.wtf/how-to-wait-for-all-threads-to-finish-in-python.html

@dataclass
class JobResult:
    status: str
    value: Optional[Any] = None
    reason: Optional[Exception] = None

def warte_auf_alle_jobs(jobs):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(job.execute) for job in jobs]
        concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
        results = []
        for future in futures:
            if future.exception():
                fex="e: {}: {}".format(future, future.exception())
               # protokolliere.fehler(fex)
                results.append(JobResult(status="e: Exception during job", reason=fex))
            else:
                results.append(JobResult(status="i: Job erfolgreich beendet", value=future.result()))
        return results
