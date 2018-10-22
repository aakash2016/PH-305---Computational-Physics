
# coding: utf-8

# In[25]:


## Finite Difference Method 
import numpy as np

h1 = 0.01
dx = 10.0/11
T_atm = 20
Tf = 200
Ti = 40

lambd = h1*T_atm*(dx**2)
pts = 10

T = np.zeros(pts) ## we have to find this
## We have to first create the banded matrix.
A = np.zeros((pts, pts))
R = np.zeros(pts)
R[0] = lambd + Ti
R[pts-1] = lambd + Tf

for i in range(pts):
    A[i][i] = 2.0 + h1*(dx**2)
for i in range(0, pts-1):    
    A[i][i+1] = -1.0
for i in range(1, pts):    
    A[i][i-1] = -1.0
for i in range(1, pts-1):
    R[i] = lambd
    
## Banded Matrix has been created    
# Using Thomas Algo. to solve the problem.
## Decomposition
for i in range(1,pts):
    A[i][i-1] = A[i][i-1]/A[i-1][i-1]
    A[i][i] -= A[i][i-1]*A[i-1][i]

## Forward Elimination
for i in range(1,pts):
    R[i] -= A[i][i-1]*R[i-1]

## Backward Subs.
T[pts-1] = R[pts-1]/A[pts-1][pts-1]
for i in range(pts-2, 0, -1):
    T[i] = (R[i] - A[i][i+1]*T[i+1])/A[i][i]
    
T    

