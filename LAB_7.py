
# coding: utf-8

# In[1]:


##### Q1
# Simple Euler Method
import numpy as np

# setting up the initial conditions
h = 0.25 #let
k = int(4./h)
y = np.zeros(k)
x = np.zeros(k)
x[0] = 0.
y[0] = 2.

# derivative function
def derivative(x,y):
    return(4*np.exp(0.8*x) - 0.5*y) 

for i in range(k-1):
    y[i+1] = y[i] + h*derivative(x[i], y[i])
    x[i+1] = x[i] + h
    
y_euler = list(y)    
    
# Heuns or Improved Euler Method            
for i in range(k-1):
    y[i+1] = y[i] + 0.5*h*(derivative(x[i], y[i]) + derivative(x[i+1], y[i+1]))
    x[i+1] = x[i] + h    
y_heuns = list(y)
    
# Mid Point Method
for i in range(k-1):
    y[i+1] = y[i] + h*(derivative(x[i] + 0.5*h, y[i] + 0.5*h))
    x[i+1] = x[i] + h      
y_mp = list(y)
    
f = open('q1.txt', "w") 
for idx in range(len(x)):
    f.write(str(x[idx]) + ' ' + str(y_euler[idx]) + ' ' + str(y_mp[idx]) + ' ' + str(y_heuns[idx]) + '\n')
f.close()    


# In[2]:


##### Q2
v = np.zeros(k)
x = np.zeros(k)
t = np.zeros(k)
t[0] = 0
x[0] = 1. # x0
v[0] = 0

def derivative_pos(t,x,i):
    return(v[i])
def derivative_velocity(t,v,i):
    return(-x[i])

for i in range(k-1):
    x[i+1] = x[i] + h*derivative_pos(t[i], x[i], i)       
    v[i+1] = v[i] + h*derivative_velocity(t[i], v[i], i)
    t[i+1] = t[i] + h
x_euler = list(x)  
v_euler = list(v)
    
# Mid Point Method    
for i in range(k-1):
    x[i+1] = x[i] + h*(derivative_pos(t[i] + 0.5*h, x[i] + 0.5*h, i))
    v[i+1] = v[i] + h*(derivative_velocity(t[i] + 0.5*h, v[i] + 0.5*h, i))
    t[i+1] = t[i] + h           
x_mp = list(x)
v_mp = list(v)
    
# Heuns or Improved Euler Method         
for i in range(k-1):
    x[i+1] = x[i] + 0.5*h*(derivative_pos(t[i], x[i], i) + derivative_pos(t[i+1], x[i+1], i+1))
    v[i+1] = v[i] + 0.5*h*(derivative_velocity(t[i], v[i], i) + derivative_velocity(t[i+1], v[i+1], i+1))
    t[i+1] = t[i] + h    
x_heuns = list(x)
v_heuns = list(v)
    
f = open('q2.txt', "w") 
for idx in range(len(t)):
    f.write(str(t[idx]) + ' ' + str(x_euler[idx]) + ' ' + str(x_mp[idx]) + ' ' + str(x_heuns[idx]) + '\n')
f.close()        

