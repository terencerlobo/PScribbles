def number_validation(label):
    while True:
        try:
            numberX = int(input(label))
            break
        except ValueError:
            print("Enter only Integer!! Try again!!")
    return numberX
        

number1 = number_validation("Enter a number: ")
number2 = number_validation("Enter another number: ")

total = number1 + number2

another_number_add = input("Do you want to add another number? Hint: press Y to continue addition. ").lower()

while another_number_add == 'y':
    numberX = number_validation("Enter another number: ")
    total = total + numberX
    another_number_add = input("Do you want to add another number? Hint: press Y to continue addition. ").lower()

print("The number total is: ", total)