import os
import job
def getDefinition():
    einJob=job
    einJob.mit="ping google -c 6000  >> wuerglog.log 2>&1"
    einJob.algorithmus = lambda x: os.system(x)
    return einJob

def do():
    getDefinition().do()