
# coding: utf-8

# In[17]:


## Aakash Agrawal
# 160122001
# (Jacobi Transformation) Similarity Transformation
# Q1
import numpy as np

A = np.array([[2, np.sqrt(3)], [np.sqrt(3), 4]], dtype = float)
alpha = (A[1][1]- A[0][0])/A[0][1]

# Calculating tan, cos, sin 
t = -(alpha + np.sqrt(alpha*alpha + 4))/2.
c = 1./(np.sqrt(1 + t*t))
s = c*t

R = np.array([[c, s], [-s, c]])
R_trans = R.T

# Similar/Diagonal Matrix 
C = np.matmul(np.matmul(R_trans, A), R) 

# printing the eigenvalues
print(C[0][0], C[1][1])


# In[7]:


# Q2
# Jacobi iteration method
A = np.array([[8,-1,3,-1], [-1,6,2,0], [3,2,9,1], [-1,0,1,7]], dtype = float)

## Sign Function
import numpy as np

def sign(x):
        if x >= 0:
            return 1
        else:
            return -1
        
while True:
    mask = np.ones(A.shape, dtype = bool)
    np.fill_diagonal(mask, 0)
    idx = np.where(abs(A) == abs(A[mask]).max())
    p = idx[0][0]
    q = idx[0][1]
    rho = 0.5*(A[q][q] - A[p][p])/A[p][q]

    t = sign(rho)/(abs(rho) + np.sqrt(rho*rho + 1))
    c = 1./(np.sqrt(1 + t*t))
    s = c*t

    ## Constructing the matrix D    
    D[:] = A[:]
    D[p][q] = 0
    D[q][p] = 0
    D[p][p] = c*c*A[p][p] + s*s*A[q][q] - 2*c*s*A[p][q]
    D[q][q] = s*s*A[p][p] + c*c*A[q][q] + 2*c*s*A[p][q]
    for j in range(len(A)):
        if (j != p) and (j != q):
            D[j][p] = c*A[j][p] - s*A[j][q]
            D[p][j] = D[j][p]
            D[j][q] = c*A[j][q] + s*A[j][p]
            D[q][j] = D[j][q]
    if np.sum(D) == np.sum(np.diag(D)):
        break
    A[:] = D[:]    
print(D)    

