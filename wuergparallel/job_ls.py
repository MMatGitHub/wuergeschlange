import os
import job
import protokolliere

def getDefinition():
    einJob=job
    einJob.mit="ls /home -R >> wuerglog.log 2>&1"
    einJob.algorithmus = lambda x: os.system(x)
    return einJob

def do():
    getDefinition().do()
    protokolliere.info(f"i: {__name__} beendet")
    return f"Ende von {__name__}"