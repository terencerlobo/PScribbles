print("Please input the size of every field")
x = int(input("Name_size: "))
y = int(input("SSN_size: "))
z = int(input("ADDRESS_size: "))
print("Please input the block size")
block = float(input("The block size is: "))
tupl = float(input("How many tuples: "))
print(int(block/90))
if (tupl % (int(block/(x+y+z)))) == 0:
	number = int(tupl/(int(block/(x+y+z))))
else:
	number = int(tupl/(int(block/(x+y+z))))+1
print(number)


