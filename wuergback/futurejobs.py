import protokolliere
from dataclasses import dataclass
from typing import Callable, Any, Tuple
from futureworker import work_mit_fehlern, testwork, zipwork
from future import warte_auf_alle_jobs
from jobitem import Jobitem 

@dataclass
class Job:
    func: Callable[..., Any]
    args: Tuple[Any, ...] = ()
    kwargs: dict[str, Any] = None

    def execute(self):
        return self.func(*self.args, **(self.kwargs or {}))

def zip(jobs):
    i=1
    for j in jobs:
        protokolliere.debug("i: Job(" + str(i) + "):")
        protokolliere.debug(getattr(j, 'args'))
        i = i + 1
    protokolliere.warn("i: Beginne mit dem zippen...")
    results = warte_auf_alle_jobs(jobs)
    i=1
    for r in results:
        protokolliere.debug("i: Job(" + str(i) + "):")
        i=i+1
        protokolliere.info(r)
    protokolliere.warn("i: Beende das gezippe...")
    return results

def get_work_mit_fehlern_job():
    ji = Jobitem("nix", "nux", "pux")
    return Job(func=work_mit_fehlern, args=(ji,2,3,4,5))

def get_testwork_job():
    ji = Jobitem("tix", "tux", "tox")
    return Job(func=testwork, args=(ji,'b','2','3','4'))

def zipwork_test():
    ji = Jobitem("C:\\Temp\\pmet", "C:\\Temp\\pukcab", "Paket_pmet2")
    return Job(func=zipwork, args=(ji,'a','-p','-ssw','nullkommanix'))

def compose_zip_jobs():


    jobs = [
            #get_work_mit_fehlern_job(),
            #get_testwork_job(),
            zipwork_test(),
            #Job(func=testwork, item=(ji), args=(eins, zwei, drei , vier, fuenf)), 
            # Job(func=realwork, args=(arg1, arg2)),
    ]
    return zip(jobs)