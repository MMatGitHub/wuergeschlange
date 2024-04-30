import os
import job
import protokolliere

def getDefinition():
    einJob=job
    einJob.mit="dir C:\\Users\\itbc000133\\AppData\\Local\\LOCALHOME\\repos\\down_ip -R >> wuerglog.log 2>&1"
    einJob.algorithmus = lambda x: os.system(x)
    return einJob

def do():
    getDefinition().do()
    protokolliere.info(f"i: {__name__} beendet")
    return f"Ende von {__name__}"