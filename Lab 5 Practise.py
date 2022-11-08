#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 17:45:21 2022

@author: nikitabaruah
"""

#Q 1. Download surveys.csv from moodle.kent.ac.uk, answer the following questions, respectively
#(a) Are there any missing values in the file? If so, which variables include missing values
#Yes


#(b) Are there any outliers within the first 5 rows? Write a Python program to show which one includes an outlier


import pandas as pd

df1 = pd.read_csv("/Users/nikitabaruah/Desktop/surveys.csv",header=1)
df1.describe()

df1.info()

df1.shape

df1.head()


#year3 has value 2300 which means incorect data


#(c) Write a Python program to delete the rows with missing values. How can you confirm whether you have successfully dropped the missing values?


df2 = df1.dropna()
df2.describe()


#(d) Are there any duplicates? Write a Python program to confirm it


df2.duplicated()

#(e) Based on the data from part (c), write a Python program to remove the duplicate

df2.drop_duplicates()


#Q2 Write a Python function to calculate 𝑓(𝑥) = 1 − 𝑒−(𝑥/𝛼)𝛽  


def fx(x, alpha, beta):
    import math
    val1=1-math.exp((-x/alpha)**beta)
    return val1
fx(10,10,1)

#Q3 Write a Python function to calculate 𝑦 = ∑𝑛 𝑖=0 i**1.5

def val2(n):
    total = 0
    for x in range(n+1):
        total = total + x**1.5
    return total

val2(100)

#Q4 


import pandas as pd

dfBMI = pd.read_csv("/Users/nikitabaruah/Desktop/weight-height.csv",header=1)
dfBMI.describe()

def BMI(mass,height):
    #mass = 50
    #height = 6
    BMI = 0
    BMI = mass/(height**2)
    return BMI
#print(BMI)
    yourHealthCondition = 0
    yourHealthCondition = BMI
    
    if BMI>=18.5:
        print("you're in the underweight range.")
    elif BMI >=18.5 and BMI <25:
        print("you're in the healthy weight range.")
    elif BMI >=25 and BMI <30:
        print("you're in the overweight range.")
    elif BMI >=30 and BMI <40:
        print("you're in the obese range.")
    else:
        print("you're in the over obese range.")
        
BMI(50,6)



    





    
    

