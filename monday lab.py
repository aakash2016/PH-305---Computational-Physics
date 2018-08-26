
# coding: utf-8

# In[1]:


import numpy as np
import random

#a = np.random.rand(5,5)
a = np.array([[3.01,2.22,4.10], [1.0,3.21,5.3], [0.3,-0.44,6.6]])
#a = a*10
#a = a.astype(int)
b = np.array([4.5,5.1,7.1])

n = len(a)

for k in range(0, n):
    for i in range(k+1, n):
        l = a[i][k]/(a[k][k])
        b[i] = b[i] - (l*b[k])
        for j in range(k, n):
            a[i][j] = a[i][j] - (l*(a[k][j]))
        
x = np.zeros(n)
x[n-1] = b[n-1]/a[n-1][n-1]  
for k in range(n-2,-1,-1):
    summ  = 0
    for i in range(k+1, n):
        summ = summ + (a[k][i]*x[i])
    x[k] = (b[k] - summ)/a[k][k]    
    
x    

