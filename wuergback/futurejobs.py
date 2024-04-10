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
        protokolliere.debug(f"i: Starte Jobs({i}):")
        protokolliere.debug(getattr(j, 'args'))
        i = i + 1
    protokolliere.warn("i: Beginne mit dem zippen...")
    results = warte_auf_alle_jobs(jobs)
    i=1
    for r in results:
        protokolliere.debug(f"i: Finished Job({i}):")
        i=i+1
        protokolliere.info(r)
    protokolliere.warn("i: Beende das backup...")
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

def sichere_multi():
    multi= ["C:\\Temp\\out", "C:\\Temp\\in"]
    ji = Jobitem("C:\\Temp\\pmet", "C:\\Temp\\pukcab" , "Multi_paket", multi)
    return Job(func=zipwork, args=(ji,'a','-p','-t7z','-r'))

def compose_zip_jobs():
    jobs = [
            #zipwork_test(),
            sichere_multi(),
    ]
    return zip(jobs)
