from threading import *
from concurrent.futures import ThreadPoolExecutor

sem = Semaphore(4)

def name(name):
    sem.acquire()
    sem.acquire()
    print(f"Hello: Thread name {name}")
    sem.release()

with ThreadPoolExecutor(max_workers=10) as exe:
    exe.submit(name,("t1"))
    exe.submit(name,("t2"))
    exe.submit(name,("t3"))
    exe.submit(name,("t4"))
    exe.submit(name,("t5"))
    exe.submit(name,("t6"))
    exe.submit(name,("t7"))
    exe.submit(name,("t8"))



    