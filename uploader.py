#!/usr/bin/env python
import os,sys
import subprocess 
from queue import Queue
from threading import Thread
import time
import logging

def do_work(src,dest):
    logging.warn("starting to upload {}...".format(dest))
    subprocess.call(["aws","s3","cp",src,dest])

def worker(q,i):
    while True:
        item = q.get()
        do_work(item,"s3://mscv/sample3/{}-{}.csv".format(i,time.time()))
        q.task_done()

q = Queue()
num_worker_threads = 10

for i in range(num_worker_threads):
     t = Thread(target=worker,args=(q,i))
     t.daemon = True
     t.start()

for item in range(100):
    q.put("{}".format(sys.argv[1]))

q.join()