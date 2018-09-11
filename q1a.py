
# coding: utf-8

# In[1]:


## Aakash Agrawal -- 160122001
# Lab - 5 Power Method Q1
# Determination of the largest eigen value

import numpy as np
a = np.array([[-30,10,20],[10,40,-50],[20,-50,-10]], dtype = float)
x = np.array([1,1,1], dtype = float)
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
print(eigval)        

