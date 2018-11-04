#!/usr/bin/env python
import os
import subprocess 
from queue import Queue
from threading import Thread
import time
import logging
import sys

class runner:

    def __init__(self, num_workers = 10,):
        self.num_workers = num_workers

    def __do_work(*args):
        cmd = args[1]
        logging.warn("starting work on {}".format(str(cmd)))
        subprocess.call(cmd)


    def __worker(self,q):
        
        while True:
            item = q.get()
            self.__do_work(item)
            q.task_done()

    def run(self,*tasks):
        q = Queue()

        for i in range(self.num_workers):
            t = Thread(target=self.__worker,args=(q,))
            t.daemon = True
            t.start()
        
        for task in tasks[0]:
            q.put(task)

        q.join()

if __name__ == "__main__" :
    runner = runner()
    runner.run(sys.argv[1:len(sys.argv)],)