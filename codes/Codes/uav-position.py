# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:55:00 2019

@author: admin
"""

import numpy as np

trip_distance=[120,100,140,90,180,90]
trip_cord=[[0,120],[0,100],[70,210],[90,180],[30,210],[120,210]]
y=1800
uav1=0
uav2=210
d1=0
d2=0
allocated_agent=[]
op_cost=np.zeros(2)
total_cost=0
j=0
for i in range(len(trip_cord)):
    
    x1=trip_cord[i][0]
    x2=trip_cord[i][1]
    if x1 <= uav1 <= x2:
        allocated_agent.insert(i,"UAV1")
    elif x1 <= uav2 <= x2:
        allocated_agent.insert(i,"UAV2")
    else:
        allocated_agent.insert(i,"NA")
        
    
        
print("Allocated agents are:")
print(allocated_agent)
print("\nTotal cost of operation:")
print(total_cost)
