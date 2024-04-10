import time
import subprocess
import protokolliere
import shutil
import shlex
# https://how.wtf/how-to-wait-for-all-threads-to-finish-in-python.html

def zipwork(jobitem, *arguementis):
    try:
        for arg in arguementis:
            protokolliere.debug(f"i: zipping with arguments: [{arg}]")
        zipparam=arguementis[0]
        passparam=arguementis[1]
        passparam= passparam + jobitem.geheim
        zippintparams=arguementis[2]
        multiquelle=jobitem.multiquellfolder
        multiquellenstring = " ".join(jobitem.multiquellfolder)
        multiquellenstring=jobitem.multiquellfolder
       # multiquelle = " ".join(shlex.quote(item)
        temp =""
        for item in jobitem.multiquellfolder:
             temp = temp + " " + item
        multiquellenstring= temp

        eintraege = [eintrag.strip() for eintrag in jobitem.multiquellfolder]
        multiquellenstring= " ".join(eintraege)
        dasKommando=f"{jobitem.prg} {zipparam} {jobitem.getZielpaket()} {passparam} {zippintparams} {jobitem.quelle} {multiquellenstring}"
        protokolliere.warn(f"i: zip KOMMANDO:{dasKommando}")
        kommandos = [jobitem.prg, zipparam, jobitem.getZielpaket(), passparam, zippintparams, jobitem.quelle] +  jobitem.multiquellfolder
        protokolliere.warn(f"i: zip KOMMANDOS:{kommandos}")
        p = subprocess.Popen(kommandos, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="cp437")
        #p = subprocess.Popen([jobitem.prg, zipparam, jobitem.getZielpaket(), passparam, zippintparams, jobitem.quelle, multiquellenstring], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="cp437")
        # tut: p = subprocess.Popen([jobitem.prg, zipparam, jobitem.getZielpaket(), passparam, zippintparams, jobitem.quelle, multiquelle[0], multiquelle[1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        while p.poll() is None:
            protokolliere.debug("i: bearbeite {jobitem.paketname}... at "+time.strftime("%Y.%m.%d_%H-%M-%S", time.localtime()))
            time.sleep(2)
        
        output, errors = p.communicate()
        protokolliere.debug(output)
        if (errors):
            protokolliere.debug(errors)
        # hochladen
        protokolliere.warn("i: Beende das gezippe. lade ins Archiv hoch...")
        von=jobitem.getZielpaket()
        nach=jobitem.getArchivpaket()
        protokolliere.warn(f"i: py sh util copy KOMMANDO: {von} --> {nach}")
        shutil.copy(f"{von}", f"{nach}")    
    except:
        raise NameError("e: Unbekannter Fehler aufgetreten!")

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
