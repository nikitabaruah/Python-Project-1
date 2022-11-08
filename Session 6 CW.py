#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 10:30:25 2022

@author: nikitabaruah
"""

#Continue Statement

for letter in "Ten I'll huff and I'll puff and I’ll blow your house in": #letter is a variable
    if letter == 'f' or letter == 's' : 
        continue
    print("Current Letter :", letter) #all the letters in the string will be printed except f & s,


#Break Statement


if letter == 'f ' or letter == 's': 
    break
print("Current Letter :", letter) #once it comes across f or s, the for-loop will break

#Pass statement

for letter in 'Then I’ll huff and I’ll puff and I’ll blow your house in':
    pass
def function(args): 
    pass


#An example: to grade student marks

import pandas as pd

}) 
#to create a data frame named students
students=pd.DataFrame({'StudentLogin': ['A00010','B00020','C00030','D00110','E00120','F00130'],
'Lastname':['POLLARD','SIMMS','CHAN','WHITEING','MEYER','HAMNAM'],
'Programme': ['BusinessAnalytics','SupplyChain','SupplyChain','Banking',' BusinessAnalytics',' BusinessAnalytics']


#to create a data frame named marks
marks=pd.DataFrame({'Module': ['BusinessStats','MachineLearning','Simulation','BigData', 'MachineLearning', 'MachineLearning'],
'StudentLogin':['A00010', 'C00030', 'E00120','F00130', 'E00120', 'G00120'], 'Marks':[70,65,58,81,73,65]
}) 


#to conduct an inner join between the two tables: students and marks 
innerJoin=pd.merge(students,marks,on='StudentLogin')

innerJoin

#to conduct a left outer join between the two tables: students and marks
leftOuterJoin=pd.merge(students,marks,on='StudentLogin',how='left')

leftOuterJoin

#to conduct a right outer join between the two tables: students and marks
rightOuterJoin=pd.merge(students,marks,on='StudentLogin',how='right') 

rightOuterJoin

#to conduct a full join between the two tables: students and marks
fullJoin=pd.merge(students,marks,on='StudentLogin',how='outer')

fullJoin

#to find the number of rows in the data frame and assign it to numRows 
numRows = len(innerJoin) 

#to assign the marks to temp, which is a vector
temp = innerJoin.Marks 

#to to initialize by assigning 0’s to the array Grade
grade = [0 for i in range(numRows)] 


for i in range(numRows): #to iterate each student marks 
    if temp[i] >= 70:
        grade[i] = "distinction" #if a student’s grade is greater than 70, his/her grade is distinction 
    elif temp[i] < 70 and temp[i] >= 60:
        grade[i] = "merit" #if a student’s grade is between 60 an 70, his/her grade is merit 
    else:
        grade[i] = "pass" #if a student’s grade is less than 60, his/her grade is pass
    
innerJoin['grade']=grade #insert the final marks back to the resulting_table 
innerJoin #print out the results












