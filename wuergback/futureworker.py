import time
import subprocess
import protokolliere
import shutil
import os
# https://how.wtf/how-to-wait-for-all-threads-to-finish-in-python.html

def zipwork(jobitem, *arguementis):
#try:
    for arg in arguementis:
        protokolliere.debug(f"i: zipping with arguments: [{arg}]")

    zipparam=arguementis[0]
    passparam=arguementis[1]
    passparam= passparam + jobitem.geheim
    zippintparams=arguementis[2]

    protokolliere.warn(f"i: zip KOMMANDO: {jobitem.prg} {zipparam} {jobitem.getZielpaket()} {passparam} {zippintparams} {jobitem.quelle}]")
    p = subprocess.Popen([jobitem.prg , zipparam, jobitem.getZielpaket(), passparam, zippintparams, jobitem.quelle], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)   
    while p.poll() is None:
        neZeit=time.localtime(time.time())
        get_timestamp = str(neZeit.tm_hour)+":"+str(neZeit.tm_min)+":"+str(neZeit.tm_sec)
        protokolliere.debug(f"i: bearbeite {jobitem.paketname}... at {get_timestamp}")
        time.sleep(2)
    
    output, errors = p.communicate()
    protokolliere.debug(output)
    if (errors):
        protokolliere.debug(errors)
    # hochladen
    #time.sleep(2)


    von=jobitem.getZielpaket()
    nach=jobitem.getArchivpaket()
    # kopiere ohne ETA (von, nach)
    protokolliere.warn(f"i: robocopy KOMMANDO: {von} --> {nach}")
    shutil.copy(f"{von}", f"{nach}")    
    #von=jobitem.getZielpaketfilename()
    #nach=jobitem.getArchivpaketfilename()
    #robo = subprocess.Popen([jobitem.prg_copy, f"{von}", f"{nach}", '/r:4', '/w:1' ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)   
    # do_robocopy(jobitem.ziel, jobitem.archiv, f"{von}", f"{nach}", 'logrobocopy.log')
    #while robo.poll() is None:
    #    neZeit=time.localtime(time.time())
    #    get_timestamp = str(neZeit.tm_hour)+":"+str(neZeit.tm_min)+":"+str(neZeit.tm_sec)
    #    protokolliere.debug(f"i: bearbeite {jobitem.paketname}... at {get_timestamp}")
    #    time.sleep(1)
    
    #output, errors = robo.communicate()
    #if (errors):
    #    protokolliere.debug(errors)
#except Exception as e:
#    protokolliere.fehler(str(e))

#def log_progress(copied: int, total: int):
#    percentage = (copied / total) * 100 if total > 0 else 0
#    protokolliere.debug (f"Kopiert: {percentage}")
 
#def kopiere_mit_ETA(von, nach):
#    with open(von, 'rb') as src:
#        total_size: int = src.seek(0, 2)
#        src.seek(0)
#    
#    with open(nach, 'wb') as dst:
#        copied = 0

#    while True:
#        chunk = src.read(8192)
#        if not chunk:
#            break
#        dst.write(chunk)
#        copied += len(chunk)
#        
#        # Log the progress every second
#        if time.time() % 1 < 0.5:
#            log_progress(copied, total_size)

def do_robocopy(source, destination, sourcefilename, destfilename, logfile):
    # Create the log file if it doesn't exist
    with open(logfile, 'a'):
        pass

    robocopy_command = [
        "robocopy", source, destination, sourcefilename, destfilename,
        "/COPY:DAT",
        "/R:4", "/W:2",
        "/TEE",
        "/LOG:" + f"{logfile}",
    ]
    protokolliere.warn(" ".join(robocopy_command))
    #os.system(" ".join(robocopy_command))
    result = subprocess.run(robocopy_command)
    if result.returncode == 0:
        print("Copy completed successfully.")
    else:
        print("Error occurred during copying.")

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
