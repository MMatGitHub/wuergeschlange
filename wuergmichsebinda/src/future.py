import time
import concurrent.futures
import subprocess
from dataclasses import dataclass
from typing import Callable, Any, Tuple, Optional

#https://how.wtf/how-to-wait-for-all-threads-to-finish-in-python.html

def gethuebsch():
    neZeit=time.localtime(time.time())
    return str(neZeit.tm_hour)+":"+str(neZeit.tm_min)+":"+str(neZeit.tm_sec)

def nettwork(eins, zwei):
    p = subprocess.check_output("ping 8.8.8.8", shell=True)

def realwork(interval_seconds, order):
    siebenz = "C:\\Users\\itbc000133\\AppData\\Local\\LOCALHOME\\repos\\no_upstream\\c_ae\\SYS\\portable\\7-ZipPortable\\App\\7-Zip64\\7z.exe"
    p = subprocess.Popen([siebenz , 'b'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    while p.poll() is None:
      print('doing work... at '+str(gethuebsch()))
      time.sleep(1)

    output, errors = p.communicate()
    print(output)
    if (errors):
      print(errors)

def work(interval_seconds, order):
    print(f"sleeping for {interval_seconds} seconds")
    time.sleep(interval_seconds)
    print(f"slept for {interval_seconds} seconds")
    if order == 2:
      raise "TEST-Fehlerchen"
    
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
        concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
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
    Job(func=realwork, args=(1, 4)),
    Job(func=nettwork, args=(1, 4)),
    
]

results = all_settled(jobs)

for r in results:
    print(r)