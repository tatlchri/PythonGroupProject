# -*- coding: utf-8 -*-
"""
Chis & Selly: Correlation part

Assume returns are returned in the first function in a dataframe as well
"""


import pandas as pd
import numpy as np
import csv
##### Prices into standarad Python data structures

# Read prices into dictionary of lists

def readPricesIntoDict():
    input_file = csv.DictReader(open('SP_500_close_2015.csv', 'r')) 
    d = dict()
    for row in input_file:
        for column, value in row.items():
            d.setdefault(column, []).append(value)
    return d


prices = readPricesIntoDict()


##### Prices into pandas

# Open data with pandas 
filename = 'SP_500_close_2015.csv'
filename2 = 'SP_500_firms.csv'
priceData = pd.read_csv(filename,index_col = 0)
compData = pd.read_csv(filename2,index_col = 0)
compData2 = pd.read_csv(filename2,index_col = 1)


# Generate pairwise correlation table using panda
def corTable(returns):
    return returns.corr()
    
correlationTable = corTable(priceData) #ATTENTION!!!!!to change priceData to actual returns

#Print correlation between company A and B
def printCor(correlationTable, companyA, companyB):
    corr = correlationTable.loc[companyA,companyB]
    nameA = compData.loc[companyA,'Name']
    nameB = compData.loc[companyB,'Name']
    return nameA, nameB, corr

#Compare panda method and python manual method of calculating correlations
def testCor(correlationTable, companyA, companyB):
    print('Panda method:')
    print(correlationTable.loc[companyA,companyB])
    print('Standard data structure method')
    a,b = np.array(prices[companyA],dtype = float),np.array(prices[companyB],dtype = float)
    print(np.sum((a - np.mean(a))/np.std(a)*(b - np.mean(b))/np.std(b))/(len(a)))
    
#List top correlated companies of a company   
def topCor(correlationTable,company):
    min = correlationTable[company].sort_values()[0:5]
    max = correlationTable[company].sort_values(ascending=False)[1:6]
    list1 = []
    list2 = []
    for i in min.index:
        list1.append(compData.loc[i,'Name'])
    for i in max.index:
        list2.append(compData.loc[i,'Name'])
    min.index = list1
    max.index = list2
    print('Most -ve correlated:')
    print(min)
    print('Most +ve correlated:')
    print(max)
    
topCor(correlationTable,'AAPL')
topCor(correlationTable,'AMZN')
topCor(correlationTable,'MSFT')
topCor(correlationTable,'FB')
topCor(correlationTable,'GOOGL')