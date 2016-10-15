# -*- coding: utf-8 -*-
"""
BS1819-1617
Data Structures and Algorithms
Group Assignment
Team 3:
  - Ahmad Bilal Aslam
  - Chris Ying
  - Christina Lefkothea Tatli 
  - Joh B
  - Kelvin Goh
  - Selly Salkha

"""


import pandas as pd
import numpy as np
import csv

##### START OF PART 1 - calculate daily returns #####

##~~ KEY VARIABLE: "returns" stores daily returns of stocks

##### To Read company names into a dictionary
def readNamesIntoDict():
    d = dict()
    input_file = csv.DictReader(open("SP_500_firms.csv"))
    for row in input_file:
        #print(row)
        d[row['Symbol']] = [row['Name'],row['Sector']]
    return d

##### To calculate daily returns from stock prices
def returns_Stocks(priceData):      
    # input is a pd.dataframe of stock prices
    # output is a pd.dataframe of daily returns    
    returns = priceData.pct_change()
    # remove index 0 of returns - it's a nan value because the first period data has no daily return
    #returns = returns[1:len(returns)]
    # We had used the built-in function, the next function below is the manual calculation
    return returns

def returns_Stocks_manual_calc(priceData):      
    # Manual calculation of the returns
    returns = priceData / priceData.shift(1) - 1
    # remove index 0 of returns - it's a nan value because the first period data has no daily return
    #returns = returns[1:len(returns)]
    return returns

# make sure that the manual calculation is same as built-in function
def test_returns_Stock_built_in_equals_manual(priceData):  
    returns_built_in = returns_Stocks(priceData)
    returns_manual = returns_Stocks_manual_calc(priceData)
    difference = returns_built_in - returns_manual 
    print("The total difference between built-in and manual way of calculating daily returns, across stocks and time period, is:", difference.sum().sum()) 

##### Several functions to determine which stock has max, min return; which are overall best, worst stocks; and max and min std of daily returns
def max_return(returns, namesDict = readNamesIntoDict()):    
    # input: pd.dataframe of daily returns, and a dictionary of company/sector (call the readNamesIntoDict() function if the dictionary is not passed as an argument)
    # output: returns the maximum daily return along with company name and Sector
    maxDaily_byComp  = returns.max()            #Maximum returns for each company

    maxDaily = maxDaily_byComp.max()            #Overall highest daily return
    maxDaily_CompSym = maxDaily_byComp.idxmax() #Getting index of the maximum return value

    maxDaily_CompName = namesDict[maxDaily_CompSym][0]  #Company Name using its symbol
    maxDaily_Sector = namesDict[maxDaily_CompSym][1]    #Company Sector
    
    return maxDaily_Sector, maxDaily_CompName, maxDaily
    

def min_return (returns, namesDict = readNamesIntoDict()):    
    # input: pd.dataframe of daily returns, and a dictionary of company/sector (call the readNamesIntoDict() function if the dictionary is not passed as an argument)
    # output: returns the minimum daily return along with company name and Sector

    minDaily_byComp  = returns.min()            #Minimum returns for each company

    minDaily = minDaily_byComp.min()            #Overall lowest daily return
    minDaily_CompSym = minDaily_byComp.idxmin() #Getting index of the minimum return value

    minDaily_CompName = namesDict[minDaily_CompSym][0]  #Company Name using its symbol
    minDaily_Sector = namesDict[minDaily_CompSym][1]    #Company Sector
    
    return minDaily_Sector, minDaily_CompName, minDaily


def overall_best (priceData, namesDict = readNamesIntoDict()):    
    # input: pd.dataframe of price data, and a dictionary of company/sector (call the readNamesIntoDict() function if the dictionary is not passed as an argument)
    # output: returns the maximum yearly return along with company name and Sector
    overallReturn_byComp  = priceData.iloc[-1] / priceData.iloc[0] - 1   #yearly returns for each company

    overallBest = overallReturn_byComp.max()            #best yearly return
    overallBest_CompSym = overallReturn_byComp.idxmax() #Getting index of the best yearly return

     #Loading Company Symbols mapping into namesDict
    overallBest_CompName = namesDict[overallBest_CompSym][0]  #Company Name using its symbol
    overallBest_Sector = namesDict[overallBest_CompSym][1]    #Company Sector
    
    return overallBest_Sector, overallBest_CompName, overallBest
    

def overall_worst (priceData, namesDict = readNamesIntoDict()):    
    # input: pd.dataframe of price data, and a dictionary of company/sector (call the readNamesIntoDict() function if the dictionary is not passed as an argument)
    # output: returns the minimum yearly return along with company name and Sector
    overallReturn_byComp  = priceData.iloc[-1] / priceData.iloc[0] - 1   #yearly returns for each company

    overallWorst = overallReturn_byComp.min()            #worst yearly return
    overallWorst_CompSym = overallReturn_byComp.idxmin() #Getting index of the worst yearly return

    overallWorst_CompName = namesDict[overallWorst_CompSym][0]  #Company Name using its symbol
    overallWorst_Sector = namesDict[overallWorst_CompSym][1]    #Company Sector
    
    return overallWorst_Sector, overallWorst_CompName, overallWorst


def max_std (returns, namesDict = readNamesIntoDict()):    
    # input: pd.dataframe of price data, and a dictionary of company/sector (call the readNamesIntoDict() function if the dictionary is not passed as an argument)
    # output: returns the maximum std. dev along with company name and Sector
    std_byComp  = returns.std()            #std. dev of returns for each company

    maxStd = std_byComp.max()            #maximum std. dev
    maxStd_CompSym = std_byComp.idxmax() #Getting index of the maximum std. dev

    namesDict = readNamesIntoDict() #Loading Company Symbols mapping into namesDict
    maxStd_CompName = namesDict[maxStd_CompSym][0]  #Company Name using its symbol
    maxStd_Sector = namesDict[maxStd_CompSym][1]    #Company Sector
    
    return maxStd_Sector, maxStd_CompName, maxStd
    
    
def min_std (returns, namesDict = readNamesIntoDict()):    
    # input: pd.dataframe of price data, and a dictionary of company/sector (call the readNamesIntoDict() function if the dictionary is not passed as an argument)
    # output: returns the minimum std. dev along with company name and Sector
    std_byComp  = returns.std()            #std. dev of returns for each company

    minStd = std_byComp.min()            #minimum std. dev
    minStd_CompSym = std_byComp.idxmin() #Getting index of the minimum std. dev

    minStd_CompName = namesDict[minStd_CompSym][0]  #Company Name using its symbol
    minStd_Sector = namesDict[minStd_CompSym][1]    #Company Sector
    
    return minStd_Sector, minStd_CompName, minStd


##### Read company names into a dictionary
namesDict = readNamesIntoDict()

##### Read Prices Data into pandas
filename = 'SP_500_close_2015.csv'
priceData = pd.read_csv(filename,index_col = 0)

##### Call the function to calculate stocks' daily returns from the price data
returns = returns_Stocks (priceData)

# test that manual and built-in calculations are the same
# uncomment the next line of code to run test
#test_returns_Stock_built_in_equals_manual(priceData)

# UNCOMMENT THIS WHEN DONE WITH TESTING
###### Print results
#a, b, c = max_return (returns, namesDict)
#print(b,", which belongs to the",a,"sector, had the maximum daily return of the year i.e.", c*100, "%.")
##http://investors.fcx.com/investor-center/news-releases/news-release-details/2015/Freeport-McMoRan-Announces-Further-Spending-Cuts-in-Response-to-Market-Conditions/default.aspx
#
#a, b, c = min_return (returns, namesDict)
#print(b,", which belongs to the",a,"sector, had the minimum daily return of the year i.e.", c*100, "%.")
##the company warned that third-quarter results wouldn't be as strong as expected.
#
#a, b, c = overall_best (priceData, namesDict)
#print(b,", which belongs to the",a,"sector, had the best overall performance of the year with a return of", c*100, "%.")
#
#a, b, c = overall_worst (priceData, namesDict)
#print(b,", which belongs to the",a,"sector, had the worst overall performance of the year with a return of", c*100, "%.")
#
#a, b, c = max_std (returns, namesDict)
#print(b,", which belongs to the",a,"sector, exhibited the most volatility in its returns during the year, with a standard deviation of", c*100, "%.")
#
#a, b, c = min_std (returns, namesDict)
#print(b,", which belongs to the",a,"sector, exhibited the least volatility in its returns during the year, with a standard deviation of", c*100, "%.")

##### END OF PART 1 #####



##### START OF PART 2 - find correlations between stocks' daily returns #####

##~~ KEY VARIABLE: "correlationTable" stores correlation results 

##### Generate pairwise correlation table using panda
def corTable(returns):
    # this uses the built-in function. The manual calculation is as below.
    return returns.corr()
    
# store correlation results (to use as input to other functions)
correlationTable = corTable(returns) 

##### read company names into pd dataframe
compData = pd.read_csv('SP_500_firms.csv', index_col = 0)

##### Print correlation between company A and B
def printCor(correlationTable, companyA, companyB):
    corr = correlationTable.loc[companyA,companyB]
    nameA = compData.loc[companyA,'Name']
    nameB = compData.loc[companyB,'Name']
    return nameA, nameB, corr

##### Compare panda method and python manual method of calculating correlations
def testCor_pairwise(correlationTable, companyA, companyB):
    print('Panda method:')
    print(correlationTable.loc[companyA,companyB])
    print('Standard data structure method')
    returns_for_manual = returns[1:len(returns)]
    a,b = np.array(returns_for_manual.get(companyA).tolist(),dtype = float),np.array(returns_for_manual.get(companyB).tolist(),dtype = float)
    print(np.sum((a - np.mean(a))/np.std(a)*(b - np.mean(b))/np.std(b))/(len(a)))

##### The above does a pairwise correlation manually
#     This chunk of code computes all pairwise correlations manually
def testCor_allprices(returns):
    # copy returns dataframe to initialise corr_matrix. Will edit the cell contents in code below.
    corr_matrix = returns.copy()
    col_names = list(returns.columns.values)
    # remove index 0 of returns - it's a nan value because the first period data has no daily return
    returns = returns[1:len(returns)]
    for i in range(len(col_names)):
        for j in range(i, len(col_names)):
            companyA = col_names[i]
            companyB = col_names[j]
            a,b = np.array(returns.get(companyA).tolist(),dtype = float),np.array(returns.get(companyB).tolist(),dtype = float)
            corr_matrix.ix[companyA, companyB] = (np.sum((a - np.mean(a))/np.std(a)*(b - np.mean(b))/np.std(b))/(len(a)))
            corr_matrix.ix[companyB, companyA] = (np.sum((a - np.mean(a))/np.std(a)*(b - np.mean(b))/np.std(b))/(len(a)))
    return corr_matrix


##### make sure that the manual calculation is same as built-in function
def test_correlation_Stock_built_in_equals_manual(returns):  
    corr_built_in = corTable(returns)
    corr_manual = testCor_allprices(returns)
    difference = corr_built_in - corr_manual 
    print("The total difference between built-in and manual way of calculating correlations across stocks is:", difference.sum().sum()) 

# To test if built-in and manual way of finding correlations are the same
# Uncomment the lines below to test it. (have tested, values returned are the same. There is a very small difference 3.1778630833582955e-12, for the manual and built-in way of computing all correlations, likely due to rounding errors)
#testCor_pairwise(correlationTable, 'GOOGL', 'FB')
#test_correlation_Stock_built_in_equals_manual(returns)

    
##### List top and bottom correlated companies of a company   
def top_bottom_Cor(correlationTable,company):
    print('Finding the top and bottom correlated companies for ', company, ':')
    print('===================================================')
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
    print('Bottom correlated :')
    print('-----------------')
    print(min)
    print('') # break line
    print('Top correlated:')
    print('---------------')
    print(max)


# UNCOMMENT THIS WHEN DONE WITH TESTING
#top_bottom_Cor(correlationTable,'AAPL')
#print("") # break line
#top_bottom_Cor(correlationTable,'AMZN')
#print("") # break line
#top_bottom_Cor(correlationTable,'MSFT')
#print("") # break line
#top_bottom_Cor(correlationTable,'FB')
#print("") # break line
#top_bottom_Cor(correlationTable,'GOOGL')

##### END OF PART 2 #####



##### START OF PART 3 - clustering algorithm #####

##~~ KEY VARIABLE: " " stores {} 

##### END OF PART 3 #####




##### START OF PART 4 part 1 - more efficient clustering algorithm #####

##~~ KEY VARIABLE: " " stores {} 

##### Store all stock names into a list
all_stock_names = list(correlationTable.columns.values)
n = len(all_stock_names)
#print("length of correlationTable: ", n)
#print("length of namesDict: ", len(namesDict))
# COMMENT: The length of namesDict and all_stock_names 
#          DO NOT MATCH! all_stock_names is correct, 
#          there are 496 stock names in the price csv file
#          len(namesDict) shows 504, which matches 
#          the firms csv file
#          So the results differ because of the csv files.
#          To check that the usage of namesDict is correct.

##### Add all pairwise correlation (upper-triangle matrix), into a list
edge_list = []
for i in range(len(all_stock_names)-1):
    for j in range(i+1, len(all_stock_names)):
        # add tuple (weight, source, destination) to list
        edge_list.append( (correlationTable.loc[all_stock_names[i], all_stock_names[j]], i, j) )


# sort them in descending order
edge_list = sorted(edge_list, reverse = True)

##### Create a node class with:
#       node_name: prints the stock's name
#       parent: nodes with the same parent will belong to the same cluster
#       rank: depth of the node. Use this for efficient merging - tries to keep tree as balanced as possible - shorter search time
#       setlist: stores the names of all the nodes that belong to the same cluster. Updates this when sets are merged 
#                (the root of the tree at any time will always store the complete set of nodes belonging to the same cluster)

class Node():
    def __init__(self, node_name):
        self.name = node_name
        # maintain a list that stores all the nodes
        # in the same cluster. Update this list when
        # clusters merge (i.e. update the root node list)
        self.setlist = [node_name];
    
    def setParent(self, node):
        self.parent = node
        
    def getParent(self):
        return self.parent
        
    def setRank(self, rank):
        self.rank = rank

    def getRank(self):
        return self.rank
        
    def getSet(self):
        return self.setlist
        
    def mergeSet(self, node):
        # update the root node list whenever there is a merge operation. Root of the tree will have the complete set list
        node.getSet().extend(self.setlist)

    def __str__(self):
        return self.name
    

def MakeSet(x):
    x.setParent(x)
    x.setRank(0)
    
def Union(x, y):
    # Union in a way such that the depth of the tree is minimised
    # always add the shorter tree under the deeper tree so that the height doesn't increase
    xRoot = Find(x)
    yRoot = Find(y)
    if xRoot == yRoot:
        return

    # x and y are not already in same set. Merge them.
    # always merge the smaller subtree into the bigger one
    # to minimise the tree height
    if xRoot.getRank() < yRoot.getRank():
        xRoot.setParent(yRoot)
        xRoot.mergeSet(yRoot)
        
    elif xRoot.getRank() > yRoot.getRank():
        yRoot.setParent(xRoot)
        yRoot.mergeSet(xRoot)
    else:
        yRoot.setParent(xRoot)
        yRoot.mergeSet(xRoot)
        xRoot.setRank(xRoot.getRank() + 1)
        
def Find(x):
    # Path compression - whenever you're finding the root of a node, set the parent to the root directly
    if x.getParent() != x:
        x.setParent(Find(x.getParent()))
    return x.getParent()
    
def link_clusters(edge_list, node_names, k):
    # edge_list is list of sorted edges in tuple form (weight, source, destination)
    # node_names is the list of nodes' names
    # k is the number of iterations

    # get number of nodes
    n = len(node_names)
    
    # initialise nodePointers dictionary of linked nodes
    nodeList = []

    # add all the node names as Nodes into the list and init MakeSet (each node is a set of itself at the beginning)
    for i in range(n):
        nodeList.append(Node(node_names[i]))
        MakeSet(nodeList[i])        
        
    # loop this k times
    for i in range(k):
        # extract the k highest weights / correlations from the list
        # Negative correlated nodes should be nearer to the end of the list (i.e. stocks that are dissimiliar to each other, in opposite direction)
        # Negative weights should not affect the algorithm correctness
        weight, source, dest = edge_list[i]
        print(weight, source, dest) # for debugging purposes
        Union(nodeList[source], nodeList[dest])
        
    return nodeList
    
# test cluster algorithm
k = 300
nodeList = link_clusters(edge_list, all_stock_names, k)

# test result
# store clusters in a dictionary so that each look-up is O(1), and so over total of n iterations, the overall efficiency is O(n);
#   whereas a list may take O(n), which will make this cluster finding process O(n^2)
cluster_list = {}
for i in range(n):
    # use the following line if you want to know a particular node's cluster
    #print("Node", nodeList[i], "is in same set as Node ", Find(nodeList[i]), ". Cluster of nodes are:", Find(nodeList[i]).getSet())
    cluster_found = str(Find(nodeList[i]).getSet())    
    if (cluster_found not in cluster_list):
        cluster_list[cluster_found] = 1
        
print("After", k, "iterations, we have these clusters:")
cluster_num = 0
for cluster in cluster_list:
    cluster_num += 1
    print("Cluster #", cluster_num, ": =", cluster)

##### END OF PART 4 part 1 #####
