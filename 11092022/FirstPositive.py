data = [0,-1,3,5,0]

indx = 0

while indx < len(data) and data[indx] <= 0:
    indx = indx+1

print(indx)
print(data[indx])