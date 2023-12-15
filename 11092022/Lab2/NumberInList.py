three_digits = [123,456,789,120]

for indx in range (0, len(three_digits)):
    print(three_digits[indx])

user_input = int(input("Enter a three digit number: "))

if user_input in three_digits:
    print(three_digits.index(user_input))
else:
    print("Number not in list!!")