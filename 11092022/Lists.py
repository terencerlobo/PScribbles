data = [8.62, 1.41, 3.14, 5.74]

largest_pos = 0

for indx in range(0, len(data)):
    print(indx)
    if data[indx] > data[largest_pos]:
        largest_pos = indx

print("The largest value is: ", data[largest_pos], "which is at index: ", largest_pos)