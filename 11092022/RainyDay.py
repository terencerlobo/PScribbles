is_raining = input("Is it raining?").lower().strip()

if is_raining == "yes":
    is_windy = input("Is it windy?").lower().strip()
    if is_windy == "yes":
        print("It is too windy to take an umberlla")
    else:
        print("Take an umberlla")
elif is_raining == "no":
    print("Enjoy your day")
else:
    print("Enter a valid input")