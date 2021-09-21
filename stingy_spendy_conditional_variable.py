# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:53:04 2021

@author: s4612643
"""
import time
from threading import Thread, Condition


class StingySpendy:
    
    def __init__(self):
        
        self.money = 100 
        self.cv = Condition()
        
    def stingy(self):
        
        for i in range(500000):
            self.cv.acquire()
            self.money += 10
            self.cv.notify()
            self.cv.release()
            
        print("Stingy done")
        
    def spendy(self):
        for i in range(500000):
            self.cv.acquire()
            while self.money < 20:
                self.cv.wait()
            self.money -= 20
            if self.money < 0:
                print("Money in bank", self.money)
            self.cv.release()
            
        print("Spendy done")
        
        
ss = StingySpendy()

Thread(target=ss.stingy, args=()).start()
Thread(target=ss.spendy, args=()).start()

time.sleep(5)

print("Money in the end", ss.money)



        