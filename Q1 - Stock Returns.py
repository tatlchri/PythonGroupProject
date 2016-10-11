# -*- coding: utf-8 -*-
"""

Stock Returns - Bilal

"""


import pandas as pd

import csv

##### To Read company names into a dictionary
def readNamesIntoDict():
    d = dict()
    input_file = csv.DictReader(open("SP_500_firms.csv"))
    for row in input_file:
        #print(row)
        d[row['Symbol']] = [row['Name'],row['Sector']]
    return d


def returns_Stocks(priceData):   #output is a pd.dataframe of daily returns    
    returns = priceData.pct_change()
    #returns = priceData / priceData.shift(1) - 1
    return returns

def max_return(returns):    #returns the maximum daily return along with company name and Sector
    maxDaily_byComp  = returns.max()            #Maximum returns for each company

    maxDaily = maxDaily_byComp.max()            #Overall highest daily return
    maxDaily_CompSym = maxDaily_byComp.idxmax() #Getting index of the maximum return value

    namesDict = readNamesIntoDict() #Loading Company Symbols mapping into namesDict
    maxDaily_CompName = namesDict[maxDaily_CompSym][0]  #Company Name using its symbol
    maxDaily_Sector = namesDict[maxDaily_CompSym][1]    #Company Sector
    
    return maxDaily_Sector, maxDaily_CompName, maxDaily
    

def min_return (returns):    #returns the minimum daily return along with company name and Sector
    minDaily_byComp  = returns.min()            #Minimum returns for each company

    minDaily = minDaily_byComp.min()            #Overall lowest daily return
    minDaily_CompSym = minDaily_byComp.idxmin() #Getting index of the minimum return value

    namesDict = readNamesIntoDict() #Loading Company Symbols mapping into namesDict
    minDaily_CompName = namesDict[minDaily_CompSym][0]  #Company Name using its symbol
    minDaily_Sector = namesDict[minDaily_CompSym][1]    #Company Sector
    
    return minDaily_Sector, minDaily_CompName, minDaily



def overall_best (priceData):    #returns the maximum yearly return along with company name and Sector
    overallReturn_byComp  = priceData.iloc[-1] / priceData.iloc[0] - 1   #yearly returns for each company

    overallBest = overallReturn_byComp.max()            #best yearly return
    overallBest_CompSym = overallReturn_byComp.idxmax() #Getting index of the best yearly return

    namesDict = readNamesIntoDict() #Loading Company Symbols mapping into namesDict
    overallBest_CompName = namesDict[overallBest_CompSym][0]  #Company Name using its symbol
    overallBest_Sector = namesDict[overallBest_CompSym][1]    #Company Sector
    
    return overallBest_Sector, overallBest_CompName, overallBest
    

def overall_worst (priceData):    #returns the minimum yearly return along with company name and Sector
    overallReturn_byComp  = priceData.iloc[-1] / priceData.iloc[0] - 1   #yearly returns for each company

    overallWorst = overallReturn_byComp.min()            #worst yearly return
    overallWorst_CompSym = overallReturn_byComp.idxmin() #Getting index of the worst yearly return

    namesDict = readNamesIntoDict() #Loading Company Symbols mapping into namesDict
    overallWorst_CompName = namesDict[overallWorst_CompSym][0]  #Company Name using its symbol
    overallWorst_Sector = namesDict[overallWorst_CompSym][1]    #Company Sector
    
    return overallWorst_Sector, overallWorst_CompName, overallWorst


def max_std (returns):    #returns the maximum std. dev along with company name and Sector
    std_byComp  = returns.std()            #std. dev of returns for each company

    maxStd = std_byComp.max()            #maximum std. dev
    maxStd_CompSym = std_byComp.idxmax() #Getting index of the maximum std. dev

    namesDict = readNamesIntoDict() #Loading Company Symbols mapping into namesDict
    maxStd_CompName = namesDict[maxStd_CompSym][0]  #Company Name using its symbol
    maxStd_Sector = namesDict[maxStd_CompSym][1]    #Company Sector
    
    return maxStd_Sector, maxStd_CompName, maxStd
    
    
def min_std (returns):    #returns the minimum std. dev along with company name and Sector
    std_byComp  = returns.std()            #std. dev of returns for each company

    minStd = std_byComp.min()            #minimum std. dev
    minStd_CompSym = std_byComp.idxmin() #Getting index of the minimum std. dev

    namesDict = readNamesIntoDict() #Loading Company Symbols mapping into namesDict
    minStd_CompName = namesDict[minStd_CompSym][0]  #Company Name using its symbol
    minStd_Sector = namesDict[minStd_CompSym][1]    #Company Sector
    
    return minStd_Sector, minStd_CompName, minStd


##### Read company names into a dictionary
namesDict = readNamesIntoDict()

##### Read Prices Data into pandas
filename = 'SP_500_close_2015.csv'
priceData = pd.read_csv(filename,index_col = 0)


returns = returns_Stocks (priceData)

a, b, c = max_return (returns)
print(b,", which belongs to the",a,"sector, had the maximum daily return of the year i.e.", c*100, "%.")
#http://investors.fcx.com/investor-center/news-releases/news-release-details/2015/Freeport-McMoRan-Announces-Further-Spending-Cuts-in-Response-to-Market-Conditions/default.aspx

a, b, c = min_return (returns)
print(b,", which belongs to the",a,"sector, had the minimum daily return of the year i.e.", c*100, "%.")
#the company warned that third-quarter results wouldn't be as strong as expected.

a, b, c = overall_best (priceData)
print(b,", which belongs to the",a,"sector, had the best overall performance of the year with a return of", c*100, "%.")

a, b, c = overall_worst (priceData)
print(b,", which belongs to the",a,"sector, had the worst overall performance of the year with a return of", c*100, "%.")

a, b, c = max_std (returns)
print(b,", which belongs to the",a,"sector, exhibited the most volatility in its returns during the year, with a standard deviation of", c*100, "%.")

a, b, c = min_std (returns)
print(b,", which belongs to the",a,"sector, exhibited the least volatility in its returns during the year, with a standard deviation of", c*100, "%.")
