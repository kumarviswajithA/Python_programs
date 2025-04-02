# Multi-Threading :  It just like multiprocessing , multithreading is a way of acheving multitasking.

import threading
import time

def cubes(n):
    print("cubes : ")
    for i in n:
        time.sleep(1)
        print("cubes : ",i*i*i)
def squares(n):
    print("squares : ")
    for i in n:
        time.sleep(1)
        print("squares : ",i*i)
n = [1,2,3,4,5]
t1 = threading.Thread(target=cubes,args=(n,))
t2 = threading.Thread(target=squares,args=(n,))
t1.start()
t2.start()