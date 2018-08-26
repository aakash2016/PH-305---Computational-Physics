
# coding: utf-8

# In[7]:


## Solving the system of equations using LU Decomposition

import numpy as np
import random

a = np.array([[3.0,-0.1,-0.2], [0.1,7.0,-0.3], [0.3,-0.2,10.0]], dtype = float)
b = np.array([7.85,-19.3,71.4], dtype = float)
n = len(a)

L = np.eye(n)

for k in range(0, n):
    for i in range(k+1, n):
        l = a[i][k]/(a[k][k])
        L[i][k] = l
        for j in range(k, n):
            a[i][j] = a[i][j] - (l*(a[k][j]))

U = a

Y = np.zeros(n)
Y[0] = b[0]
for m in range(1,n):
    som = 0
    for w in range(0, m-1):
        som = som + (L[m][w])*Y[w]
    Y[m] = b[m] + som


x = np.zeros(n)
x[n-1] = Y[n-1]/U[n-1][n-1]  
for k in range(n-2,-1,-1):
    summ  = 0
    for i in range(k+1, n):
        summ = summ + (U[k][i]*x[i])
    x[k] = (Y[k] - summ)/U[k][k]    

x


# In[27]:


# Solving the inverse using LU Decomposition
A_inv = np.zeros((3,3))
I = np.eye(3)

for s in range(0,n):
    Y = np.zeros(3)
    Y[0] = I[:][s][0]
    for k in range(1,n):
        summ  = 0
        for i in range(0, k):
            summ = summ + (L[k][i]*Y[i])
        Y[k] = (I[:][s][k] - summ)  
    print(Y)
    A_inv[n-1][s] = Y[n-1]/U[n-1][n-1]  
    for k in range(n-2,-1,-1):
        summ  = 0
        for i in range(k+1, n):
            summ = summ + (U[k][i]*A_inv[i][s])
        A_inv[k][s] = (Y[k] - summ)/U[k][k]    
A_inv    


# In[29]:


np.matmul(np.array([[3.0,-0.1,-0.2], [0.1,7.0,-0.3], [0.3,-0.2,10.0]], dtype = float), A_inv)

