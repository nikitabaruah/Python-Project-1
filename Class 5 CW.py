#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 10:52:59 2022

@author: nikitabaruah
"""

from math import * 

def expProb(nu,t):
    prob = 1 - exp(-nu*t)
    return prob
expProb(0.01, 10)

#Local Variable

from math import * 

def expProb(nu,t):
    prob = 1 - math.exp(-nu*t) 
    t=1 #nu or t is a local variable 
    return prob #return the value prob

expProb(0.01, 10)


#Global Variable

from math import *
t=1 #t is a global variable 
def expProb(nu):
    prob = 1 - math.exp(-nu*t) 
    return prob #return the value prob

expProb(0.01)

#Example 1: Loop through a string 

for x in "Python":
    print(x)

#Example 2: Loop through a list/set/tuple/dictionary

Modules= ['BusinessStats','MachineLearning','Simulation','BigData']

for x in Modules: 
    print(x)
    
    
    
for x in range(6): 
    print(x)
    

for x in range(2, 6):
    print(x)
    
    
for x in range(2, 30, 3): 
    print(x)
    
    
var=[] #to define an empty array
arr = [0 for i in range(5)] #to assign 0’s to the array