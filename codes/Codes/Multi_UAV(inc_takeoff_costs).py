# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:18:23 2019

@author: admin
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:36:16 2019

@author: admin
"""

import numpy as np

trip_distance=[120,100,140,90,180,90]
trip_cord=[[10,130],[10,110],[80,220],[100,190],[40,220],[130,220]]
u_alt=1800
r_alt=[0,100,300,250,200,200,100]
r_pos=[10,50,90,105,130,180,220]
uav=[]
total_d=220
d1=np.zeros((total_d,total_d))
d2=np.zeros((total_d,total_d))
d11=0
d21=0
d=0
cost=np.zeros((total_d,total_d))
min_cost=np.zeros((7,7))
d1_min=np.zeros((7,7))
d2_min=np.zeros((7,7))
item='NA'
iter_1=0

for x in range(len(r_pos)):
    for y in range(len(r_pos)):
        x_1=r_pos[x]
        y_1=r_pos[y]
        for i in range(total_d):
            for j in range(total_d):
                allocated_agent=[]
                for m in range(len(trip_cord)):
                    x1=trip_cord[m][0]
                    #print(x1)
                    x2=trip_cord[m][1]
                    if x1 <= x_1 <= x2:
                        allocated_agent.insert(m,"UAV1")
                    elif x1 <= y_1 <= x2:
                        allocated_agent.insert(m,"UAV2")
                    #print(allocated_agent)
                    if (len(allocated_agent)==len(trip_cord)):
                      #print(allocated_agent)
                      #cost[i][j]=0
                      #d1[i][j]=i
                      #d2[i][j]=j
                      #else:
                      #print('hi')
                      iter_1=iter_1+1
                      d11=abs(i-x_1)
                      d21=abs(j-y_1)
                      d=d11+d21
                      cost[i][j]=(d*10+ ((u_alt-r_alt[x])*20)+ ((u_alt-r_alt[y])*20))
                      d1[i][j]=i
                      d2[i][j]=j
        temp_cost=0
        temp_d1=0
        temp_d2=0
        for a in range(len(cost)):
            for b in range(len(cost[a])): 
                if (cost[a][b]!=0):
                  if(temp_cost==0):
                    temp_cost=cost[a][b]
                    temp_d1=d1[a][b]
                    temp_d2=d2[a][b]
                  if(temp_cost>cost[a][b]):
                    temp_cost=cost[a][b]
                    temp_d1=d1[a][b]
                    temp_d2=d2[a][b]
                min_cost[x][y]=temp_cost
                d1_min[x][y]=temp_d1
                d2_min[x][y]=temp_d2   
print('Minimum cost for all possible combination of reflex points are:')
print(min_cost)
print('Associated distances travelled by UAVs are:')
print(d1_min)
print(d2_min)
min_cost_f=0
d1_min_f=0
d2_min_f=0
for i in range(len(min_cost)):
    for j in range(len(min_cost[i])):
        if (min_cost_f==0):
            min_cost_f=min_cost[i][j]
            c=i
            d=j
            d1_min_f=d1_min[i][j]
            d2_min_f=d2_min[i][j]
        elif(min_cost_f>min_cost[i][j] and min_cost[i][j]!=0):
            min_cost_f =min_cost[i][j]
            d1_min_f=d1_min[i][j]
            d2_min_f=d2_min[i][j]
            c=i
            d=j
print('Cost of operation:')
print(min_cost_f)
print('Coordinate of UAV1:')
print(d1_min_f)
print('Coordinate of UAV2:')
print(d2_min_f)
print('Take-off point of UAV1:')
print(r_pos[c])
print('Reflex point of UAV1:')
print(c+1)
print('Take-off point of UAV2:')
print(r_pos[d])
print('Reflex point of UAV2:')
print(d+1)
allocated_agent=[]
for i in range(len(trip_cord)):
    
    x1=trip_cord[i][0]
    x2=trip_cord[i][1]
    if x1 <= d1_min_f <= x2:
        allocated_agent.insert(i,"UAV1")
    elif x1 <= d2_min_f <= x2:
        allocated_agent.insert(i,"UAV2")
    #else:
        #allocated_agent.insert(i,"NA")
print('Task allocation is as follows:')
print(allocated_agent)
