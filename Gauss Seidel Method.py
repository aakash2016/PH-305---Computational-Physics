
# coding: utf-8

# In[1]:


## PH 305 - Lab no. 4
## Aakash Agrawal
# 160122001 

#### Iterative Methods #### 
# 1. Gauss Seidel Method
import numpy as np

a = np.array([[3,7,13], [1,5,3], [12,3,-5]], dtype = float)
b = np.array([76,28,1], dtype = float)
n = len(a)
x = np.zeros(n, dtype = float)
old = np.zeros(n, dtype = float)


# In[2]:


## Checking for the diagonally Dominant matrixxx
for i in range(n): 
    summ1 = 0
    for j in range(n):
        if i != j:
            summ1 += a[i][j]
    if a[i][i] <= summ1:
        print('not diagonally dominant')
        break
    print('Diagonally Dominant bro')


# In[3]:


# Making Diagonally Dominant
m = a.argmax(axis = 1)
t = m.argmin(axis = 0) 
    
temp = a[[i]]
a[i][:] = a[t][:]  
a[t][:] = temp  


temp1 = b[0]
b[0] =b[t]  
b[t] = temp1

print(a, b)


# In[4]:


def GS(a, b, n, x):
    for i in range(n):
        b[i] = b[i]/a[i][i]
        a[i] = a[i]/a[i][i]
    
        summ = b[i]
        for j in range(n):
            if i != j:
                summ = summ - (a[i][j])*x[j]
        x[i] = summ    
    return x


# In[5]:


i = 1
while True:
    old[:] = x[:]
    print('iteration{}'.format(i))
    GS(a, b, n, x)
    print(x, old)
    error = abs((x - old)/x)*100
    i += 1
    if np.all(error < 0.0000001):
        break

