# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#1a
l1 = list(("Name", "Business Statistics", "Simulation","Machine Learning"))
l2 = list(("John", 65, 60,70))
#
t1 = tuple(("Name", "Business Statistics", "Simulation","Machine Learning"))
t2 = tuple(("John", 65, 60,70))

s1 = set(("Name", "Business Statistics", "Simulation","Machine Learning"))
s2 = set(("John", 65, 60,70))


#1b
tuple(l1); tuple(l2)

set(t1); set(t2)

list(s1); list(s2)

#1c
d1 = dict(Name = "John", BusinessStatistics = 65, Simulation = 60,MachineLearning = 70)

#1d
l1 = list(("Name", "Business Statistics", "Simulation","Machine Learning"))
l2 = list(("John", 65, 60,70))

t1 = tuple(("Name", "Business Statistics", "Simulation","Machine Learning"))
t2 = tuple(("John", 65, 60,70))

s1 = set(("Name", "Business Statistics", "Simulation","Machine Learning"))
s2 = set(("John", 65, 60,70))

l1.append("Big Data")
l2.append(68)

#tuples are immutable so convert it to a new variable list, then append and then if required convert it back to a tuple
t3 = list(t1);
t4 = list(t2)
t3.append("Big Data")
t4.append(68)


s1.add("Big Data")
s2.add(68)

d1 = dict(Name = "John", BusinessStatistics = 65, Simulation = 60,MachineLearning = 70)

d1.update({"Big Data" : 68})


#3
import random
print(random.randrange(1,100))

import random
print(random.randrange(1,100))

import random
print(random.randrange(1,100))

#4
import math
x = math.sqrt(137)+math.exp(-1.4)+math.log(134)
round(x,3)
print(x)

#5
#a
import numpy as np
x = np.array([9,11,13,15,17,19,21,23}])

#b
x1 = x.reshape(2,4)
x1
x2 = x1.reshape(-1)
x2

#6a
import numpy as np
arr1 = np.array([1, 2, 3,5,'W']) 
arr2 = np.array([4, 5, 6,7,'QW'])
newArray = np.concatenate((arr1,arr2))
print(newArray)

#b
p = np.array_split(newArray,3)
p

#c
newArrayNew = np.array_split(newArray,3)
z = np.sort(arr1)
z

