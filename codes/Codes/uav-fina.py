# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:49:59 2019

@author: admin
"""

import numpy as np

trip_distance=[120,100,140,90,180,90]
trip_cord=[[10,130],[10,110],[80,220],[100,190],[40,220],[130,220]]
y=1800
uav1=0
uav2=230
total_d=230
d1=0
d2=0
d=0
cost=np.zeros((total_d,total_d))
min_cost_row=[]
item='NA'
iter_1=0
#allocated_agent=['NA', 'NA', 'NA', 'NA', 'NA', 'NA']

" Finding the task allocation between two agents and the cost associated to the allocation"
for i in range(total_d):
    for j in range(total_d):
        allocated_agent=[]
        for m in range(len(trip_cord)):
            x1=trip_cord[m][0]
            #print(x1)
            x2=trip_cord[m][1]
            
            if x1 <= i <= x2:
                allocated_agent.insert(m,"UAV1")
            elif x1 <= j <= x2:
                allocated_agent.insert(m,"UAV2")
            #print(allocated_agent)
            if (len(allocated_agent)!=len(trip_cord)):
                cost[i][j]=0
            else:
                iter_1=iter_1+1
                d1=abs(i-uav1)
                d2=abs(j-uav2)
                d=d1+d2
                cost[i][j]=d*10
                 
#print(cost)
"finding the minimum cost and position of uav"
print("Possible optimised solutions")
print(iter_1)
min_cost=np.max(cost)
min_cost=0
for i in range(len(cost)):
    for j in range(len(cost[i])):
        if (min_cost==0):
            min_cost=cost[i][j]
            d1_min=i
            d2_min=j
        elif(min_cost>cost[i][j] and cost[i][j]!=0):
            min_cost=cost[i][j]
            d1_min=i
            d2_min=j
print("Minimum cost is:")
print(min_cost)
print("Distance travelled by uav 1")
print(abs(d1_min-uav1))
print("Distance travelled by uav 2")
print(abs(d2_min-uav2))
print("Cordinates of UAV1")
print(d1_min)
print("Cordinates of UAV2")
print(d2_min)
print("task allocation is:")
allocated_agent=[]
for i in range(len(trip_cord)):
    
    x1=trip_cord[i][0]
    x2=trip_cord[i][1]
    if x1 <= d1_min <= x2:
        allocated_agent.insert(i,"UAV1")
    elif x1 <= d2_min <= x2:
        allocated_agent.insert(i,"UAV2")
    else:
        allocated_agent.insert(i,"NA")
print(allocated_agent)
        
 

