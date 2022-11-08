#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 10:37:00 2022

@author: nikitabaruah
"""

#Q1 a)
import pandas as pd

marks = pd.DataFrame({"Name":["John", "Anna", "Emma"],"Business Statistics":["65","72","56"],"Simulation":["60","65","64"]})
                             
print(marks)                              

#b0
marks["Simulation"]

#c)
marks.loc[0]

#d)
marks.drop(["Simulation"],axis=1)

#e)
marks.drop([1,2])


#f)
marks["Grades"]=["Merit","Merit","Merit"]


#Q2

A = [(1,2,6,7),
     (0,7,1,3),
     (4,0,2,1)]

B = [(5,2,3,2),
     (2,1,4,4),
     (2,5,7,1)]

dataframe1 = pd.DataFrame(data=A)
dataframe2 = pd.DataFrame(data=B)

Dim1 = dataframe1.shape
Dim2 = dataframe2.shape

addResult = dataframe1 + dataframe2
subResult = dataframe1 - dataframe2
dotResult = dataframe1.dot(dataframe2)
