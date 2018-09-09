
# coding: utf-8

# In[1]:


# Q2 Lab - 5

import numpy as np
a = 4*np.eye(10) + 2*np.eye(10, k=1) + 2*np.eye(10, k=-1) + np.eye(10, k=2) + np.eye(10, k=-2)

x = np.ones(10)
eigval_old = 1

while True:  
    b = np.dot(a,x)
    idx = abs(b).argmax()
    eigval = b[idx]
    b /= eigval
    error = abs((eigval - eigval_old)/eigval)
    eigval_old = eigval
    x[:] = b[:]
    if (error < 10e-16):
        break
        
print('\n', a)
print('\n\nlargest Eigen Value', eigval)        


# In[2]:


## Finding the smallest eigenvalue
import numpy as np

a = 4*np.eye(10) + 2*np.eye(10, k=1) + 2*np.eye(10, k=-1) + np.eye(10, k=2) + np.eye(10, k=-2)

n = len(a)
c = np.eye(n)
L = np.eye(n)

for k in range(0, n):
    for i in range(k+1, n):
        l = a[i][k]/(a[k][k])
        L[i][k] = l
        for j in range(k, n):
            a[i][j] = a[i][j] - (l*(a[k][j]))

U = a
# Solving the inverse using LU Decomposition
A_inv = np.zeros((n,n))
I = np.eye(n)

for s in range(0,n):
    Y = np.zeros(n)
    Y[0] = I[:][s][0]
    for k in range(1,n):
        summ  = 0
        for i in range(0, k):
            summ = summ + (L[k][i]*Y[i])
        Y[k] = (I[:][s][k] - summ)  
    A_inv[n-1][s] = Y[n-1]/U[n-1][n-1]  
    for k in range(n-2,-1,-1):
        summ  = 0
        for i in range(k+1, n):
            summ = summ + (U[k][i]*A_inv[i][s])
        A_inv[k][s] = (Y[k] - summ)/U[k][k]    


# In[3]:


x = np.ones(n)
eigval_old = 1

while True:  
    b = np.dot(A_inv,x)
    idx = abs(b).argmax()
    eigval = b[idx]
    b /= eigval
    error = abs((eigval - eigval_old)/eigval)
    eigval_old = eigval
    x[:] = b[:]
    if (error < 10e-16):
        break
print(1/eigval)    # which is the min. eigen value   

