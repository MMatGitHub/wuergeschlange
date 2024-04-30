import time
import subprocess
import protokolliere
import shutil
import shlex
# https://how.wtf/how-to-wait-for-all-threads-to-finish-in-python.html

def zipwork(jobitem, *arguementis):
    try:
        if None==jobitem: protokolliere.fehler("e: Objekt wurde nicht erzeugt") 
        custom_attributes = [attr for attr in dir(jobitem) if not attr.startswith("__")]
       # print(custom_attributes)       
        for attr in custom_attributes:
            protokolliere.debug(f"{attr, getattr(jobitem, attr)}")
    except:
        raise NameError("e: Fehler jobitem-Objekt in zipwork")   
    try:
        protokolliere.debug(f"i: zipping with arguments: " + ", ".join(arguementis))
        zipparam=arguementis[0]
        passparam=arguementis[1]
        passparam= passparam + jobitem.geheim
        zippintparams=arguementis[2]
        kommandos = [jobitem.prg, zipparam, jobitem.getZielpaket(), passparam, zippintparams, jobitem.quelle]
        if not None == jobitem.multiquellfolder:
            kommandos = kommandos +  jobitem.multiquellfolder
        protokolliere.debug(f"i: zip KOMMANDOS:{kommandos}")
    except:
        raise NameError("e: Fehler beim zip-init aufgetreten!")      
    try:
        p = subprocess.Popen(kommandos, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="cp437")
        while p.poll() is None:
            protokolliere.debug(f"i: PROGRESS... {jobitem.paketname}... at "+time.strftime("%Y.%m.%d_%H-%M-%S", time.localtime()))
            time.sleep(2)
        
        output, errors = p.communicate()
        protokolliere.debug(output)
        if (errors):
            protokolliere.debug(errors)
    except:
        raise NameError("e: Fehler beim zippen aufgetreten!")
    try:
        # hochladen
        protokolliere.warn("i: Beende das gezippe. lade ins Archiv hoch...")
        von=jobitem.getZielpaket()
        nach=jobitem.getArchivpaket()
        protokolliere.warn(f"i: py sh util copy KOMMANDO: {von} --> {nach}")
        shutil.copy(f"{von}", f"{nach}")    
    except:
        raise NameError("e: Fehler beim ins Archiv laden!")

def zip_test_work(jobitem, *arguementis):
    for arg in arguementis:
        protokolliere.warn(f"i: argument: {arg}")
    p = subprocess.Popen([jobitem.prg , arguementis[0]], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)   
    while p.poll() is None:
        neZeit=time.localtime(time.time())
        get_timestamp = str(neZeit.tm_hour)+":"+str(neZeit.tm_min)+":"+str(neZeit.tm_sec)
        protokolliere.debug(f"i: bearbeite {jobitem.paketname}... at {get_timestamp}")
        time.sleep(2)
    
    output, errors = p.communicate()
    protokolliere.debug(output)
    if (errors):
      protokolliere.debug(errors)

def testwork(jobitem, *arguementis):
    for arg in arguementis:
        protokolliere.warn(f"i: argument: {arg}")
    p = subprocess.Popen([jobitem.prg , 'b'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)   
    while p.poll() is None:
        neZeit=time.localtime(time.time())
        get_timestamp = str(neZeit.tm_hour)+":"+str(neZeit.tm_min)+":"+str(neZeit.tm_sec)
        protokolliere.debug(f"i: bearbeite {jobitem.paketname}... at {get_timestamp}")
        time.sleep(2)
    
    output, errors = p.communicate()
    protokolliere.debug(output)
    if (errors):
      protokolliere.debug(errors)

def work_mit_fehlern(jobitem, *arguementis):
    for arg in arguementis:
        protokolliere.warn(f"i: argument: {arg}")
    interval_seconds= arguementis[2]  
    protokolliere.debug(f"sleeping for {interval_seconds} seconds")
    time.sleep(interval_seconds)
    protokolliere.debug(f"slept for {interval_seconds} seconds")
    if arguementis[3] == 3:
      raise  NameError("OK: TEST-Fehlerchen: OK")
    return f"task {arguementis[3]}"
