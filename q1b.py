
# coding: utf-8

# In[1]:


# Q1
# Determination of the lowest eigenvalue
# Just we need to find inverse of A and we are done 
import numpy as np
a = np.array([[-30,10,20],[10,40,-50],[20,-50,-10]])
c = np.eye(3)
n = len(a)

L = np.eye(n)

for k in range(0, n):
    for i in range(k+1, n):
        l = a[i][k]/(a[k][k])
        L[i][k] = l
        for j in range(k, n):
            a[i][j] = a[i][j] - (l*(a[k][j]))

U = a
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
    A_inv[n-1][s] = Y[n-1]/U[n-1][n-1]  
    for k in range(n-2,-1,-1):
        summ  = 0
        for i in range(k+1, n):
            summ = summ + (U[k][i]*A_inv[i][s])
        A_inv[k][s] = (Y[k] - summ)/U[k][k]    
A_inv    


# In[2]:


import numpy as np
x = np.array([1,1,1], dtype = float)
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

