while True:
    try:
        user_input = int(input("Enter a number: "))
        break
    except ValueError:
        print("Enter only Integer!!")

if user_input % 2 == 0:
    print("Even")
else:
    print("Odd")
