#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:53:07 2022

@author: nikitabaruah
"""

#Q2
#Write a Python script to answer the following questions 
#(a) Calculate 𝐴 + 𝐵, 𝐴 − 𝐵, 𝐴 ∘ 𝐵, 𝐴 ⊘ 𝐵, respectively, and

import pandas as pd

A = [(1,2,6,7),
     (0,7,1,3),
     (4,0,2,1)]

B = [(5,2,3,2),
     (2,1,4,4),
     (2,5,7,1)]

dataframe1 = pd.DataFrame(data=A)
dataframe2 = pd.DataFrame(data=B)


dataframe1.describe()
dataframe2.describe()

Dim1 = dataframe1.shape
Dim2 = dataframe2.shape

addResult = dataframe1 + dataframe2
subResult = dataframe1 - dataframe2
dotResult = dataframe1.dot(dataframe2)
divResult = dataframe1/dataframe
