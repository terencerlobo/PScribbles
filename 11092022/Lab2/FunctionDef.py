def user_number():
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Enter only Integers")
    return num

def increment_number(num):
    return num+1


print("The final value is: ", increment_number(user_number()))