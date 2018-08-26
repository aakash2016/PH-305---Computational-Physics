
# coding: utf-8

# In[1]:


## Gauss jordan
# note here we are touching the b part
import numpy as np
import random

a = np.array([[3.0,-0.1,-0.2], [0.1,7.0,-0.3], [0.3,-0.2,10.0]], dtype = float)
b = np.array([7.85,-19.3,71.4], dtype = float)
c = np.eye(3)
n = len(a)
 
## we are actually normalising everytime
# c is the inverse matrix
for k in range(0, n):
    b[k] = b[k]/(a[k][k])
    c[k] = c[k]/(a[k][k])
    a[k] = a[k]/(a[k][k])
    
    skips = set((k,))
    for i in (x for x in range(0,n) if x not in skips):
        l = a[i][k]
        b[i] = b[i] - (l*b[k])
        for j in range(k, n):
            a[i][j] = a[i][j] - (l*(a[k][j]))
            c[i][j] = c[i][j] - (l*(c[k][j])) 
print(b)
print('inverse matrix of a',c)


# In[2]:


np.matmul( np.matrix([[3.0,-0.1,-0.2], [0.1,7.0,-0.3], [0.3,-0.2,10.0]], dtype = float), c)

