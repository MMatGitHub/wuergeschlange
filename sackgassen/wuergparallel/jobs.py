import job_ls
#import job_ping
import job_pong
import watchdog

def get_jobs():
    job_names = []
    #job_names.append(konstruktor(job_ls, "/home",lambda x: f"ls {x}"))
    #job_names.append(konstruktor(job_ls, "ls /home >> wuerglog.log 2>&1",lambda x: os.system(x)))
    #job_names.append(konstruktor(job_ping, "www.google.de",lambda x: f"ping {x}"))
    job_names.append(job_ls)
    job_names.append(job_pong)
    job_names.append(watchdog)
    return job_names

#def konstruktor(dings, wert, algo):
#    dings.mit=wert
#    dings.algorithmus=algo
#    return dings