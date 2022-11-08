#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:06:28 2022

@author: nikitabaruah
"""
#Q3

#(a) Read the file into a dataframe called AE_df;
import pandas as pd

AE_df = pd.read_csv("/Users/nikitabaruah/Desktop/Adult.csv", header=1)

AE_df.describe()

#(b) Show the first 5 rows and the last 5 rows of AE_df, respectively;
AE_df.head()

AE_df.tail()

#(c) Find out the data structure of AE_df;

AE_df.info()


#Write basicStatistics to a csv-formatted file named bS.csv;

AE_df.to_csv("/Users/nikitabaruah/Desktop/bS.csv") 

#(g) Create a new dataframe, named sampled_df, that contains 1,000 observations randomly sampled from AE_df;

sampled_df = AE_df.sample(1000) 

sampled_df.describe()


#(h)to find the number of observations (i.e., rows) and that of variables (i.e., columns) in sampled_df.

sampled_df.shape

