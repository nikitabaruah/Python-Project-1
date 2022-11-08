#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 19:17:22 2022

@author: nikitabaruah
"""

#Write a Python function to calculate a factorial of a number 

def val3(n):
    fact = 1
    for x in range(1, n+1):
        fact = fact *  x
    return fact

val3(4)