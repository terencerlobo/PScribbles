import numpy as np
x = np.ones((5,5))

print("Original array: ")
print(x)
print("1 on the border, and 0 inside...")
x[1:-1,1:-1] = 35
print(x)

np.cos