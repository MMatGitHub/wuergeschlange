import os
import job
def getLambda():
    einJob=job
    einJob.mit="ping google -c 6000  >> wuerglog.log 2>&1"
    einJob.algorithmus = lambda x: os.system(x)
    return einJob

def do():
    getLambda().do()