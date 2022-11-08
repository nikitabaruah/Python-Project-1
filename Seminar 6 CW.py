#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:05:02 2022

@author: nikitabaruah
"""

import pandas as pd

#1) Write a Python program to calculate 𝑦 = ∑10 ∑10 𝑖 × 𝑗

sum=0
for i in range (11):
        for j in range (11):
            y = i*j
            sum = sum + y
            
print(sum)

#2)

employee = pd.DataFrame({'empno':['00010','00020','00030','00110','00120','00130'],'lastname':['HASS','THOMPSON','KWAN','LUCCHES SI','OCONNELL','QUINTANA'],'workdept':['A00','B01','C01','A00','A00','C01']})

department = pd.DataFrame({'deptno':['A00','B01','C01','D01'], 'deptname':['SPIFFY COMPUTER SERVICE DIV.','PLANNING','INFORMATION CENTER','DEVELOPMENT CENTER'],'mgrno':['000010','000020','000030','']});

project = pd.DataFrame({'projno':['AD3100','IF1000','IF2000','MA2100','PL2100'],'projname':['ADMIN SERVICES','QUERY SERVICES','USER EDUCATION','WELD LINE AUTOMATION','WELD LINE PLANNING'],'deptno':['D01','C01','E01','D01','B01'],'respemp':['000010','000030','000030','000010','000020']});

print(employee)

print(department)

print(project)

#Write one statement in Python to perform a left join on Table project and Table department according to deptno;
leftOuterJoin = pd.merge(project, department, on="deptno", how="left")
leftOuterJoin

#Write one statement in Python to perform a right join on Table project and Table department according to deptno;
rightOuterJoin = pd.merge(project, department, on="deptno", how="right")
rightOuterJoin

#Write one statement in Python to perform an inner join on Table project and Table department according to deptno;
innerJoin = pd.merge(project, department, on="deptno")
innerJoin

#Write one statement in Python to perform a full join on Table project and Table department according to deptno;
FullOuterJoin = pd.merge(project, department, on="deptno", how="outer")
FullOuterJoin

#replace empno in employee to mgrno, replace project with employee, replace deptno with mgrno in the above questions, and then repeat the above joins.

#Q3
#pwd  #to find the current working directory

f1 = open("c:\\Users\\nikitabaruah\\newFile.txt","a")
f1.write("Once upon a time, there were three little pigs. The pigs lived in a small house with their mum. One day, their mum sent them off to build houses of their own.\n As they walked down the road, the first little pig met a farmer pulling a cart of straw. It looked very warm - just right for building a house. He asked if he could have some. The farmer agreed and the first little pig began to build his straw house.") 
f1.close()

f1=open("c:\\Users\\nikitabaruah\\newFile.txt","a") #to open the existing file with the mode Append
f1.write("\n A little way down the road, the second little pig saw a woodcutter with a cart of sticks. They looked thick and long - just right for building a house. He asked if he could have some. The woodcutter agreed and the second little pig began to build his wooden house.") #note: \n will start a new paragraph
f1.close()


f1=open("c:\\Users\\nikitabaruah\\newFile.txt","r")
str1 = f1.readline()
f1.close()

import os
os.remove(“tewFile.txt")

#Q4) Write a Python script to print out “I bought x lamps with product no y, which costs me z pounds” with three different methods, where values x=4, y=”2345” and z=65.67.












