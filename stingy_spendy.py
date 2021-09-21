# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:53:04 2021

@author: s4612643
"""
import time
from threading import Thread, Lock 


class StingySpendy:
    
    def __init__(self):
        
        self.money = 100 
        self.mutex = Lock()
        
    def stingy(self):
        
        for i in range(1000000):
            self.mutex.acquire()
            self.money += 10
            self.mutex.release()
            
        print("Stingy done")
        
    def spendy(self):
        for i in range(1000000):
            self.mutex.acquire()
            self.money -= 10
            self.mutex.release()
            
        print("Spendy done")
        
        
ss = StingySpendy()

Thread(target=ss.stingy, args=()).start()
Thread(target=ss.spendy, args=()).start()

time.sleep(5)

print("Money in the end", ss.money)



        