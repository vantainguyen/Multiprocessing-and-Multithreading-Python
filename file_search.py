# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:41:23 2021

@author: s4612643
"""
import os
from os.path import isdir, join
from threading import Lock, Thread
matches = []

mutex = Lock()


def file_search(root, filename):
    print("Searching in:", root)
    child_threads = []
    for file in os.listdir(root):
        full_path = join(root, file) #cat.png c:\mypictures...
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
            
        if isdir(full_path):
            t = Thread(target=file_search, args=(full_path, filename))
            t.start()
            child_threads.append(t)
    for t in child_threads:
        t.join()
            
def main():
    t = Thread(target=file_search, args=("c:/Users", "README.md"))
    t.start()
    t.join()
    
    for m in matches:
        print("Matches:", m)
        
        
        
main()