while True:
    try:
        user_age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Enter only Integer!!")


if user_age >= 18:
    print("You can vote!!")
if user_age == 17:
    print("You can learn how to drive!!")
if user_age == 16:
    print("You can buy a lottery ticket!!")
if user_age < 16:
    print("You can go Trick-or-Treating!!")
