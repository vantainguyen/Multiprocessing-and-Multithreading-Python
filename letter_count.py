# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:25:25 2021

@author: s4612643
"""
import json
import urllib.request
import time
from threading import Thread, Lock

finished_count = 0

def count_letters(url, frequency):
    response = urllib.request.urlopen(url)
    txt = str(response.read())
    
    for l in txt:
        letter = l.lower()
        
        if letter in frequency:
            frequency[letter] += 1
            
    global finished_count
    
    finished_count += 1
            
def main():
    frequency = {}
    
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    
    start = time.time()
    
    for i in range(1000, 1020):
        Thread(target=count_letters, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)).start()
        
    while finished_count < 20:
        time.sleep(.5)
        
    end = time.time()
    print(json.dumps(frequency, indent=4))
    print("Done, time taken", end - start)
    
    
main()