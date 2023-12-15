import numpy as np





a_array = np.array([[1, 0], 
                             [0, 0], [0,0]])

u, sigma, vt = np.linalg.svd(a_array)
print(u)
print(vt)
print(sigma)