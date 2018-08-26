
# coding: utf-8

# In[1]:


## Lab no. 3 PH 305
# Aakash Agrawal
# 160122001
# Method 1
import numpy as np
import random

a = np.zeros((4,4), dtype = float)
n = len(a)
for i in range(n):
    a[i][i] = n - i
    for j in range(i):
        a[i][j] = n - i
        a[j][i] = a[i][j]
A = a        
print(a)
print('\n\n')
# So there we have our matrix A

for k in range(0, n):
    for i in range(k+1, n):
        l = a[i][k]/(a[k][k])
        for j in range(k, n):
            a[i][j] = a[i][j] - (l*(a[k][j]))
print(a)
print('\n\n')
U = a

## Lambda Matrix
# Now we have to decompose U into Lambda and W
lamb = np.eye(4)
for i in range(n):
    lamb[i][i] = U[i][i]
print(lamb)
print('\n\n')

## W matrix
W = np.zeros((n,n), dtype = float)

for k1 in range(0,n):
    W[k1] = U[k1]/U[k1][k1]
print(W)    
print('\n\n')
# There we go we got our lambda and W matrix

# D matrix
D = np.sqrt(lamb)
L_cholesky = np.matmul(D,W)
print(L_cholesky)
print('\n\n')

# Now our original A matrix should be pdt of L_cholesky.T and L_cholesky.
C = np.matmul(L_cholesky.T, L_cholesky)
print(C)


# In[2]:


## method 2
## or using the formula given by Sir

L = np.zeros((n,n), dtype = float)
for k in range(n):
    for i in range(k+1):
        summ = 0
        if i == k:
            for j in range(0, k):
                summ = summ + (L[k][j])**2
            L[k][k] = np.sqrt(C[k][k] - summ)    
        
        summ2 = 0
        if i != k:
            for j in range(0, i):
                summ2 = summ2 + (L[i][j])*(L[k][j])
            L[k][i] = (C[k][i] - summ2)/L[i][i]    
print(L)        
print('\n\n')
print(np.matmul(L, L.T))

