
# coding: utf-8

# In[19]:


## Numerical Integration

import numpy as np

def f(x, y):
    return 2*x*y + 2*x + 72 - x**2 - 2*y**2

def trapezoidal(ax,bx,n,k):
    h = (bx-ax)/n
    summ = 0
    for i in range(1, n): 
        summ += f(ax + i*h, k)
    I = h*(f(ax, k)/2 + f(bx, k)/2 + summ)
    return I

def simpson(ax,bx,n,k):
    h = (bx-ax)/n
    summ1 = 0
    summ2 = 0
    for i in range(1, int(n/2) + 1):
        summ1 += f(ax + h*(2*i - 1), k) 
    for i in range(1, int(n/2)):
        summ2 += f(ax + h*(2*i), k)
    I = (h/3)*(f(ax, k) + f(bx, k) + 4*summ1 + 2*summ2) 
    return I

def simpson38(ax,bx,n,k):
    h = (bx-ax)/n+1
    I = (bx-ax)*(f(ax, k) + f(bx, k) + 3*f(ax+h, k) + 3*f(ax+2*h, k))/8 
    return I

integrated1 = []
integrated2 = []
## For n = 2
integrated3 = []

ay = 0
by = 6
n = 2
hy = (by - ay)/n
for j in range(0,n+1):
    y = ay + hy*j
    integrated1.append(simpson(0,8,n,y))    
    integrated2.append(trapezoidal(0,8,n,y))
    integrated3.append(simpson38(0,8,n,y))
    
s1 = 0
s2 = 0
s3 = 0
t = len(integrated1)
for k in range(1,t-1):
    s1 += integrated1[k]
    s2 += integrated2[k]
    s3 += integrated3[k]
answer1 = hy*(integrated1[0]/2 + integrated1[t-1]/2 + s1)    
answer2 = hy*(integrated2[0]/2 + integrated2[t-1]/2 + s2)    
answer3 = hy*(integrated3[0]/2 + integrated3[t-1]/2 + s3)    

print('average temp for simpson13, trapezoidal, simpson38 methods')
print(answer1/48, answer2/48, answer3/48)

