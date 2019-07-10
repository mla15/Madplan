# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 17:14:18 2019

@author: mikke
"""
import math

from madret import MadRet
from madret import MadPlan

#definér de forskellige retter
#a*x+b*y <= 6
def MadPlanGenerator(Alle_Retter):
    Result = MadPlan()
    for n in range(0,7):
        hiscore = 0
        Hiscoreindeks = -1
        for i in range(0, len(Alle_Retter)):
            if Alle_Retter[i].RetScore() > hiscore and (Result.ExistRet(Alle_Retter[i].name) == False):
                hiscore = Alle_Retter[i].RetScore()
                Hiscoreindeks = i                
        if Hiscoreindeks != -1: 
            Result.AddRet(Alle_Retter[Hiscoreindeks])
    return Result

AlleRetter = [MadRet("Hoddogs", 130, 1), MadRet("Spaghetti Bolognese", 40, 3), MadRet("Pizza", 80, 1), MadRet("Bøhgærs", 60, 1), MadRet("Pomfrits", 100, 5), MadRet("Carbonara", 70, 2), MadRet("Grøntsagssuppe mæ det hele", 50, 5)]
plan = MadPlanGenerator(AlleRetter)
plan.displayMadplan()







