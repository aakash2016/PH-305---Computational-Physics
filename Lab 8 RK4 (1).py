
# coding: utf-8

# In[1]:


## RK4 Method 
import numpy as np

def derivative_pos(v):
    return(v)
def derivative_velocity(x):
    return(-x)

T = 8*np.arctan(1.0)
h = 0.02*T

t0 = 0
x0 = 1.0
v0 = 0
E0 = 0.5

pos = []
vel = []
energy = []
time = []

for i in range(100):
    pos.append(x0)
    vel.append(v0)
    time.append(t0)
    energy.append(E0)
    
    l1 = derivative_velocity(x0)
    s1 = derivative_pos(v0)
 
    l2 = derivative_velocity(x0 + s1*h/2)
    s2 = derivative_pos(v0 + l1*h/2)    

    l3 = derivative_velocity(x0 + s2*h/2)
    s3 = derivative_pos(v0 + l2*h/2)

    l4 = derivative_velocity(x0 + s3*h)
    s4 = derivative_pos(v0 + l3*h)    

    v0 = v0 + (l1 + 2*l2 + 2*l3 + l4)*h/6
    x0 = x0 + (s1 + 2*s2 + 2*s3 + s4)*h/6
    
    t0 = t0 + h
    E0 = (v0**2 + x0**2)/2.0

n_time = np.divide(time, T)
n_energy = np.multiply(energy, 1.0)       


# In[2]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.plot(n_time, n_energy)
plt.xlabel('t/T')
plt.ylabel('2E')
plt.show()

plt.plot(pos, vel)
plt.xlabel('P(momentum)')
plt.ylabel('X(position)')
plt.show()

