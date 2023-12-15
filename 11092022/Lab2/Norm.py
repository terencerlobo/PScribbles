from math import inf
import numpy as np
from numpy.linalg import norm

import pandas as pd

arr = np.array([-2,1,-8,4])

maxnorm =norm(arr,inf) 
print(maxnorm)

pd.DataFrame