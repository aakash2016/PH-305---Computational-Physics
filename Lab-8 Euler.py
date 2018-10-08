
# coding: utf-8

# In[7]:


## Simple Harmonic Oscillator
import numpy as np

## Euler Method
def derivative_pos(v):
    return(v)
def derivative_velocity(x):
    return(-x)

T = 8*np.arctan(1.0)
h = 0.02*T

t0 = 0
x0 = 1. # x0
v0 = 0

pos1 = []
vel1 = []
energy1 = []
time1 = []
E0 = 0.5

for i in range(500):
    pos1.append(x0)
    vel1.append(v0)
    time1.append(t0)
    energy1.append(E0)
    
    x = x0 + h*derivative_pos(v0)       
    v = v0 + h*derivative_velocity(x0)
    t0 = t0 + h
    
    x0 = x
    v0 = v
    E0 = (v0**2 + x0**2)/2.
    
n_time1 = np.divide(time1, T)
n_energy1 = np.multiply(energy1, 2.0) 


# In[26]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.plot(n_time1, n_energy1)
plt.xlabel('t/T')
plt.ylabel('2E')
plt.show()

plt.plot(pos1, vel1)
plt.xlabel('P(momentum)')
plt.ylabel('X(position)')
plt.show()

