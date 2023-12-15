import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
frame3 = pd.DataFrame({'id':['ball', 'pending','pen','mug','ashtray'],
                        'color': ['white','red','red','black','green'],
                        'brand': ['OMG','ABC','ABC','POD','POD']})

frame4 = pd.DataFrame({'id': ['pencil','pencil','ball','pen'],
                        'brand': ['OMG','POD','ABC','POD']})

frame5 = pd.merge(frame4,frame3, on="id")
print(frame5)
frame6 = pd.merge(frame4, frame3, left_index=True, right_index=True)
print(frame6)

plt.bar
plt.xticks

data = {'series1': [1,4,4,3,5],
        'series2': [2,4,5,2,4],
        'series3': [3,2,3,1,3]}
df = pd.DataFrame(data)
df.plot(kind="bar")
np.random.normal
plt.subplot