
# coding: utf-8

# In[49]:


## Finding Inverse using Gauss jordan
# note here we are touching the b part
import numpy as np
a = np.array([[3.0,-0.1,-0.2], [0.1,7.0,-0.3], [0.3,-0.2,10.0]], dtype = float)
c = np.eye(3)
n = len(a)
print(c)
## we are actually normalising everytime

for k in range(0, n):
    c[k] = c[k]/(a[k][k])
    a[k] = a[k]/(a[k][k])
    skips = set((k,))
    for i in (x for x in range(0,n) if x not in skips):
        for j in range(k, n):
            a[i][j] = a[i][j] - (a[i][k]*(a[k][j]))
            c[i][j] = c[i][j] - (a[i][k]*(c[k][j]))     
c

