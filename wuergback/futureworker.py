import time
import subprocess
import protokolliere
# https://how.wtf/how-to-wait-for-all-threads-to-finish-in-python.html

def zipwork(jobitem, *arguementis):
    # a %archiv% -p%zip_pw%,user. -ssw %quellordner%
#    return Job(func=zipwork, args=(ji,'a','-p','-ssw','nullkommanix'))

    for arg in arguementis:
        protokolliere.debug(f"i: zipping with arguments: [{arg}]")

    zipparam=arguementis[0]
    passparam=arguementis[1]
    passparam= passparam + jobitem.geheim
    zippintparams=arguementis[2]

    protokolliere.warn(f"i: zip KOMMANDO: {jobitem.prg} {zipparam} {jobitem.getZielpaket()} {passparam} {zippintparams} {jobitem.quelle}]")
    p = subprocess.Popen([jobitem.prg , zipparam, jobitem.paketname, passparam, zippintparams, jobitem.quelle], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)   
    while p.poll() is None:
        neZeit=time.localtime(time.time())
        get_timestamp = str(neZeit.tm_hour)+":"+str(neZeit.tm_min)+":"+str(neZeit.tm_sec)
        protokolliere.debug(f"i: bearbeite {jobitem.paketname}... at {get_timestamp}")
        time.sleep(2)
    
    output, errors = p.communicate()
    protokolliere.debug(output)
    if (errors):
      protokolliere.debug(errors)
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
