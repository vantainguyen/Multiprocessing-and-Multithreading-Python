# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:15:28 2021

@author: s4612643
"""
import time
from threading import Thread
import multiprocessing
from multiprocessing import Process

def do_work():
    print("Starting work")
    i = 0
    for _ in range(20000000):
        i += 1
    print("Finished work")
    
    
    
if __name__ == '__main__':
    
    for _ in range(5):
        
        p = Process(target=do_work, args=())
        p.start()