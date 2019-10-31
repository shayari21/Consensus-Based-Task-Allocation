# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:50:06 2019

@author: admin
"""

import numpy as np
import pandas as pd

task_dist=[10,40,20,20,10,50,20,30,10,10,20]
task_dist_GR1=np.array([10,40,20,20,10,50,20,30,10,10,20])
#task_dist_GR2= task_dist_GR1[::-1]
task_dist_UAV1=np.array([70,0,0,0,100,0,40,0,110,110,0])
#task_dist_UAV2=task_dist_UAV1[::-1]
alt=[1600,1800]
#print(task_dist_GR2)
tasks= len(task_dist)
k1=np.array( [1,0,0,0,1,0,1,0,1,1,0]) #capability matrix defines if the tasks defined can be completed by the UAVs or not
k2= np.array(np.ones(11)) #capability matrix defines if the tasks defined can be completed by the GRs or not
slope_LR=(np.array([1.5, -3, 3,4,-3,-2,1,3,-2,2,-3]))
#print(slope_LR)
slope_RL= slope_LR *-1
#print(slope_RL)

task_dist_f= np.c_[task_dist_GR1, task_dist_UAV1]
#print(task_dist_f)
#task_dist_d= pd.DataFrame[{'GR1':task_dist_GR1,'UAV1':task_dist_UAV1}]
#print(task_dist_d)

slope_LR_f=[]
for i in slope_LR:
  slope=i
  #print(slope)
  if(slope<0):
    slope= ((slope*-1)/10)
    slope_LR_f.append(slope)
  elif (slope>0):
    slope_LR_f.append(slope)
  else:
    slope=1
    slope_LR_f.append(slope)

#print(slope_LR_f)
## AUCTION BID CALCULATION 
j=1
#print(j)
bid= np.zeros((11,2))
for i in range(len(task_dist_f)):
  for j in range(len(task_dist_f[i])):
    if (j==1):  
      bid[i][j]= slope_LR_f[i]*task_dist_f[i][j]
      j=j+1   
    else:
      bid[i][j]= task_dist_f[i][j]*10
print("Bids collected by two agents are as follows:")
print(bid)

## Best Bid Slection
m=0
i=0
j=0
best_bid=np.zeros(11)
#print(best_bid)
for m in range(len(bid)):
    i=0
    #print(m)
    #print(bid[m])
    l1=bid[m]
    l1=np.sort(l1)
    #print(l1)
    x=l1[i]
    #print(x)
    best_bid[m]=x
    if (x==0):
        x=l1[i+1]
        best_bid[m]=x
        #print(best_bid[m])
print("best bids for the tasks are as follows:")
print(best_bid)
    

 