first_name = input("Enter the first name: ")
if len(first_name) < 5:
    last_name = input("Enter the last name: ")
    print((first_name + last_name).upper())
else:
    print(first_name.lower())