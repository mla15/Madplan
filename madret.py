# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 17:07:23 2019

@author: mikkel er mit navn for helvede
"""

class MadRet:
     def __init__(self, name, price, healthy):
         self.name = name
         self.price = price
         self.healthy = healthy
     
     def displayRet(self):
         print("Name : ", self.name, "Price Weight: ", self.PriceScore(), "Health Rating: ", self.healthy, "Score: ", self.RetScore())
     
     def PriceScore(self):
         if self.price in range(40, 60):
             return 5
         if self.price in range(60, 80):
             return 4
         if self.price in range(80, 100):
             return 3
         if self.price in range(100, 120):
             return 2
         if self.price >= 120:
             return 1
         return 0
     
     def RetScore(self):
         return self.PriceScore() + self.healthy
     
class MadPlan:
    def __init__(self):
        self.retter = []
    
    def displayMadplan(self):
        for i in range(0, len(self.retter)):
            self.retter[i].displayRet()
            
    def AddRet(self, ret):
        #for i in range(0, len(self.retter)):
            #if ret.name == self.retter[i].name:
              # print("Den er helt gal mester")
               #return -1
        self.retter.append(ret)
    
    def RemoveRet(self, retname):
        for i in range(0, len(self.retter)):
            if retname == self.retter[i].name:
               del self.retter[i]
               break
                           
    def PrisTotal(self):
        SumRetPris = 0
        for i in range(0, len(self.retter)):
            SumRetPris += self.retter[i].price
        return SumRetPris
    
    def PrisAverage(self):
        return self.PrisTotal()/(len(self.retter))
    
    def HealthTotal(self):
        SumRetHealth = 0
        for i in range(0, len(self.retter)):
            SumRetHealth += self.retter[i].healthy
    
    def ExistRet(self, retname):
        for i in range(0, len(self.retter)):
            if retname == self.retter[i].name:
               return True 
        return False
    
    def HealthAverage(self):
        return self.HealthTotal()/(len(self.retter))
    
    