import time
import concurrent.futures
from dataclasses import dataclass
from typing import Callable, Any, Tuple, Optional

#https://how.wtf/how-to-wait-for-all-threads-to-finish-in-python.html

def work(interval_seconds, order):
    print(f"sleeping for {interval_seconds} seconds")
    time.sleep(interval_seconds)
    print(f"slept for {interval_seconds} seconds")
    if order == 2:
      raise "lakjsf"
    
    return f"task {order}"

@dataclass
class JobResult:
    status: str
    value: Optional[Any] = None
    reason: Optional[Exception] = None

@dataclass
class Job:
    func: Callable[..., Any]
    args: Tuple[Any, ...] = ()
    kwargs: dict[str, Any] = None

    def execute(self):
        return self.func(*self.args, **(self.kwargs or {}))



def all(jobs):

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(job.execute) for job in jobs]
        return [f.result() for f in futures]

def all_settled(jobs):

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(job.execute) for job in jobs]
        concurrent.futures.wait(futures)
        results = []
        for future in futures:
            if future.exception():
                results.append(JobResult(status="rejected", reason=future.exception()))
            else:
                results.append(JobResult(status="fulfilled", value=future.result()))
        return results

jobs = [

    Job(func=work, args=(1, 1)),
    Job(func=work, args=(2, 2)),
    Job(func=work, args=(1, 3)),
]

results = all_settled(jobs)

for r in results:
    print(r)