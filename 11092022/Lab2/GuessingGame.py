def number_validation(label):
    while True:
        try:
            numberX = int(input(label))
            break
        except ValueError:
            print("Enter only Integer!! Try again!!")
    return numberX

compnum = 50

user_num = number_validation("Enter a Number: ")
count = 0

while user_num != 50:
    count = count + 1
    if user_num > 50:
        print("Too high!!")
        user_num = number_validation("Enter a Number again: ")
    elif user_num < 50:
        print("Too low!!")
        user_num = number_validation("Enter a Number again: ")
    
print("Well Done. It took ", count, " attempts to get it right!!")