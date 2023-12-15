from array import *

def find_median(array1, array2):
    
    for indx in range(len(array2)):
        array1.append(array2[indx])
    array1.sort()
    #print(array1)

    if len(array1) % 2 != 0:
        #print(len(array1) // 2 )
        median = array1[(len(array1) // 2)]
        #print(median)
    elif len(array1) % 2 == 0:
        median = (array1[(len(array1) // 2) - 1 ] + array1[(len(array1) // 2)])/2
       # print(median)

    return median
    
    
print(find_median())