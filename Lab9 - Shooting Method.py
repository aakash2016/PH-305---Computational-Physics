
# coding: utf-8

# In[62]:


## RK4 Method from Lab 8
## Shooting Method - converting the boundary to initial value problem.
import numpy as np

T_surr = 20.0
h1 = 0.01
Tf = 200.0 # given

def derivative_T(z):
    return(z)

def derivative_z(T):
    return(h1*(T - T_surr))

def Tempat10(z0):
    L = 10.0
    h = L/11

    x0 = 0.0
    T0 = 40.0
    
    Temp = []
    Z = []
    pos = []
    for i in range(12):
        Temp.append(T0)
        Z.append(z0)
        pos.append(x0)

        l1 = derivative_z(T0)
        s1 = derivative_T(z0)

        l2 = derivative_z(T0 + s1*h/2)
        s2 = derivative_T(z0 + l1*h/2)    

        l3 = derivative_z(T0 + s2*h/2)
        s3 = derivative_T(z0 + l2*h/2)

        l4 = derivative_z(T0 + s3*h)
        s4 = derivative_T(z0 + l3*h)    

        z0 = z0 + (l1 + 2*l2 + 2*l3 + l4)*h/6
        T0 = T0 + (s1 + 2*s2 + 2*s3 + s4)*h/6

        x0 = x0 + h
    return Temp[11]

## Finding correct Z[0]
Z0 = (Tf - Tempat10(10.0))*(20.0 - 10.0)/(Tempat10(20.0) - Tempat10(10.0)) + 10.0
## Now we have got the correct initial condition for which Tf will be 200.

Tempat10(Z0)

