from multiprocessing import Pool
import os
import time

def hello_world(name):
    print("warte...")
    time.sleep(1)
    print('aufgewacht')
    return "Hello: {name}"

list_of_movie_names = ["1fjf", "2jhgg", "3lkjgkjhg"]

#https://tomarv2.medium.com/python-multiprocessing-with-example-a1db1e825d1c
def demo_multi_processing():
    tic = time.time()
    pool = Pool(processes=os.cpu_count())
    res = list(pool.apply_async(hello_world, args=(film,)) for film in list_of_movie_names)

    pool.close()
    pool.join()

    results = [r.get() for r in res]
    print(results)
    toc = time.time()
    print(f'Completed in {toc - tic} seconds')

#init-init-init
siebenz = "C:\\Users\\itbc000133\\AppData\\Local\\LOCALHOME\\repos\\no_upstream\\c_ae\\SYS\\portable\\7-ZipPortable\\App\\7-Zip64\\7z.exe"