# -*- coding: utf-8 -*-
"""
BS1819-1617
Data Structures and Algorithms
Group Assignment-Part 3
Team 3:
  - Ahmad Bilal Aslam
  - Chris Ying
  - Christina Lefkothea Tatli 
  - Joh B
  - Kelvin Goh
  - Selly Salkha
"""

import sys
import networkx as nx
import matplotlib.pyplot as plt


##### START OF PART 3 - clustering algorithm #####

##### Add all pairwise correlation, into a list and sort them in ascending order
def SortEdges(correlationTable):
    comp=correlationTable.columns

    #Initialize the list of edges where each element is a tuple (weight,source,destination)
    corrTable=[]
    
    for i in range(0,correlationTable.shape[0]-1):
        for j in range(i+1,correlationTable.shape[0]):
            corrTable.append((printCor(correlationTable, comp[i],comp[j],compData)[2],comp[i],comp[j]))
            
            
    corrTable=sorted(corrTable, key=lambda x:x[0])
    return corrTable



corrTable=SortEdges(correlationTable)


#Divide the graph into clusters, based on edge weight(correlation)
def clustering(corrTable,k,companies):
     #Initialize a dictionary called nodePointers where the keys are each node, with the corresponding value the node itself
     nodePointers=dict([ (p, p) for p in companies ])
     
     #Initialize graph G for visualization
     G = nx.Graph()
     
     #Repeat the algorithm k times
     for i in range(1,k+1):
         
         #Pick the highest-weight edge ("greedy" choice)
         edge=corrTable[-i]
         source=edge[1]
         dest=edge[2]
         
         #Merge the sets containing the source and the destination of the edge
         while nodePointers[source]!=source:
             source=nodePointers[source]
             
         while nodePointers[dest]!=dest:
             dest=nodePointers[dest]
         
         #Update the dictionary
         nodePointers[source]=dest
         
         
         #Test if source and destination nodes are not aldready in the G graph and add them
         if source not in G.nodes():
             G.add_node(source)
         if dest not in G.nodes():
             G.add_node(dest)
             
         #Test if the edge (source,dest) is not aldready in the G graph and add it
         if (source,dest) not in G.edges():
             G.add_edge(source,dest)
             
     return nodePointers,G
         
nodePointer,G=clustering(corrTable,20,correlationTable.columns)


#Recover the sets, creating a dictionary with indices of the clusters/sets as keys and nodes in each cluster as values of each element of the dictionary 
def clusterRecover(nodePointer):
    nodeList={}
    flag=1
    
    #Initialize a dictionary with all different nodes as keys and value 0 if they hadn't been visited,value 1 if visited
    visited={k:0 for k in nodePointer.keys()}
    
    for i in nodePointer.keys():
        #For each node, if it and its neighbor is not visited, add the node and the neighbor to a new cluster
        if visited[nodePointer[i]]==0 and visited[i]==0:
            nodeList[flag]=[]
            nodeList[flag].append(i)
            visited[i]=flag
            if nodePointer[i]!=i:
                nodeList[flag].append(nodePointer[i])
                visited[nodePointer[i]]=flag
            flag+=1
        #Else If the neighbor is visited, but the node is not visited, add the node to the cluster of the neighbor
        elif visited[nodePointer[i]]!=0 and visited[i]==0:
            nodeList[visited[nodePointer[i]]].append(i)
            visited[i]=visited[nodePointer[i]]
        #Else if the node is visited and the neighbor is not visited, add the neighbor to the cluster of the node
        elif visited[nodePointer[i]]==0 and visited[i]!=0:
            nodeList[visited[i]].append(nodePointer[i])
            visited[nodePointer[i]]=visited[i]
        #Else if node and its neighbor are in different clusters,merge them
        else:
            if visited[nodePointer[i]]!=visited[i]:
                temp=visited[nodePointer[i]]
                for j in nodeList[visited[nodePointer[i]]]:
                    print(j)
                    nodeList[visited[i]].append(j)
                    visited[j]=visited[i]
                del nodeList[temp]
    return nodeList
        
nodeList=clusterRecover(nodePointer)           

#Create a list of different colors of size n expressed in color codes
def get_spaced_colors(n):
    max_value = 16581375 #255**3
    interval = int(max_value / n)
    colors = [hex(I)[2:].zfill(6) for I in range(0, max_value, interval)]
    colors_=[(int(i[:2], 16), int(i[2:4], 16), int(i[4:], 16)) for i in colors]
    return ['#%02x%02x%02x' % i for i in colors_[0:n]]
    
colors=get_spaced_colors(len(nodeList))


#Assign a color to each node based on each cluster
def nodecoloring(nodeList,colors):
    z={}
    flag=0
    for i in nodeList.values():
        color=colors[flag]
        for j in i:
            z[j]=color
        flag+=1
    return z


z=nodecoloring(nodeList,colors) 
       
nx.draw_shell(G, node_color=[z[node] for node in G] ,with_labels = True)

plt.show()   