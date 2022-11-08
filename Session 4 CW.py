#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:48:50 2022

@author: nikitabaruah
"""

import pandas as pd

marks=pd.DataFrame({'Module': ['BusinessStats','MachineLearning','Simulation','BigData', 'MachineLearning', 'MachineLearning'], 'StudentLogin':['A00010', 'C00030', 'E00120','F00130', 'E00120', 'G00120'],'Marks':[70,65,58,81,73,65]})

print(marks)

marks.sample(2)

marks.drop(['Module','Marks'], axis=1)

marks.sample(2)

marks.drop([0,1])

marks['Grade'] = ['Dis', 'Merit', 'Pass', 'Dis', 'Dis','Merit']

new_row={'Module':'BigData','StudentLogin':'H00120','Marks':56,'Grade':'Pass'} 
marks = marks.append(new_row, ignore_index=True)

import pandas as pd
#to define two matrices 
matrix1 = [(1, 1, 2),(0, 2, 1), (2, 0, 1)]
matrix2 = [(2, 0, 2), (1, 1, 1),(2, 2, 2)]

dataFrame1 = pd.DataFrame(data=matrix1)
dataFrame2 = pd.DataFrame(data=matrix2)

print(dataFrame1)
print(dataFrame2)

Dim1 = dataFrame1.shape
Dim2 = dataFrame2.shape

print(Dim1)

addResult = dataFrame1+dataFrame2

