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

def sichere_multi_test():
    multi= ["C:\\Temp\\out", "C:\\Temp\\in"]
    ji = Jobitem("C:\\Temp\\pmet", "C:\\Temp\\pukcab" , "Multi_paket", multi)
    return Job(func=zipwork, args=(ji,'a','-p','-t7z','-r'))

def sichere_ui_projekte():
    ji = Jobitem(None, None, 'ui_projekte', None)
    return Job(func=zipwork, args=(ji,'a','-p','-t7z','-r'))

def compose_zip_repo_jobs():
    # Einfachster Fall paketname ist das zu sichernde Verzeichnis. Multi ist None
    jobs = [
            Job(func=zipwork, args=(Jobitem(None, None, 'ui_projekte', None),'a','-p','-t7z','-r')),
            Job(func=zipwork, args=(Jobitem(None, None, 'upcgit', None),'a','-p','-t7z','-r')),
            Job(func=zipwork, args=(Jobitem(None, None, 'upcintern', None),'a','-p','-t7z','-r')),
            Job(func=zipwork, args=(Jobitem(None, None, 'upsecret', None),'a','-p','-t7z','-r')),
            Job(func=zipwork, args=(Jobitem(None, None, 'uptopsecret', None),'a','-p','-t7z','-r')),
    ]
    return zip(jobs)

LOCALHOME="C:\\Users\\itbc000133\\AppData\\Local\\LOCALHOME\\repos"

def compose_noup_down_ip_jobs():
    # Einfacher Fall paketname ist kein Verzeichnis. Multi überschreibt
    jobs = [
            Job(func=zipwork, args=(Jobitem(None, None, 'down_ip', None),'a','-p','-t7z','-r')),
            Job(func=zipwork, args=(Jobitem(None, None, 'no_up_desktop', [f"{LOCALHOME}\\no_upstream\\desktop"]),'a','-p','-t7z','-r')),
            Job(func=zipwork, args=(Jobitem(None, None, 'no_up_cae_SYS', [f"{LOCALHOME}\\no_upstream\\c_ae\\SYS"]),'a','-p','-t7z','-r')),
    ]
    return zip(jobs)

def compose_upcshare_sec_jobs():
    # Einfacher Fall paketname ist kein Verzeichnis. Multi überschreibt
    UPSEC=f"{LOCALHOME}\\upcshare_sec"

    jobs = [
            Job(func=zipwork, args=(Jobitem(None, None, 'alle_k1-BU-center', [f"{UPSEC}\\alle_k1", f"{UPSEC}\\BU",f"{UPSEC}\\andere_non_K1",f"{UPSEC}\\center"]),'a','-p','-t7z','-r')),
            Job(func=zipwork, args=(Jobitem(None, None, 'FK', [f"{UPSEC}\\FK"]),'a','-p','-t7z','-r')),
            Job(func=zipwork, args=(Jobitem(None, None, 'mamue_mima', [f"{UPSEC}\\mamue_bereich", f"{UPSEC}\\miMA"]),'a','-p','-t7z','-r')),
            Job(func=zipwork, args=(Jobitem(None, None, 'upshare_sec_projekte', [f"{UPSEC}\\projekte"]),'a','-p','-t7z','-r')),
            Job(func=zipwork, args=(Jobitem(None, None, 'team_HR', [f"{UPSEC}\\team_HR"]),'a','-p','-t7z','-r')),
            Job(func=zipwork, args=(Jobitem(None, None, 'RE', [f"{UPSEC}\\RE"]),'a','-p','-t7z','-r')),
    ]
    return zip(jobs)

def compose_ulc_topsec_jobs():
    TOPSEC=f"{LOCALHOME}\\ulc_topsecret"

    jobs = [
            #Job(func=zipwork, args=(Jobitem(None, None, 'container_mount', [f"{TOPSEC}\\container_mount"]),'a','-p','-t7z','-r')),
            #Job(func=zipwork, args=(Jobitem(None, None, 'OneNote', [f"{TOPSEC}\\One"]),'a','-p','-t7z','-r')),
            #Job(func=zipwork, args=(Jobitem(None, None, 'outlook_dateien', [f"{TOPSEC}\\Outlook-Dateien"]),'a','-p','-t7z','-r')),
            Job(func=zipwork, args=(Jobitem(None, None, 'projekte_zeugs', [f"{TOPSEC}\\_backup", f"{TOPSEC}\\_workspaces",f"{TOPSEC}\projekte",f"{TOPSEC}\\_powershell",f"{TOPSEC}\\_todo",f"{TOPSEC}\\Zettelkasten"]),'a','-p','-t7z','-r')),
   ]
    return zip(jobs)
