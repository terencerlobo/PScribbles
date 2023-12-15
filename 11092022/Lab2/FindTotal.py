total = 0

indx = 0
while indx != 5:
    while True:
        try:
            number_to_sum = int(input("Enter a number to find the sum: "))
            break
        except ValueError:
            print("Enter only Numbers!!")
    to_be_included = input("Do you want to include the number to find the sum? Hint: Enter Yes or No: ").lower()
    if to_be_included.lower() == "yes":
        total = total + number_to_sum
    indx = indx+1

print("The total number is: ", total)