def listValidation():
    print("Hre.")

name_list = ["UserA", "UserB", "UserC", "UserD"]
print(name_list)

menu = {"A": "Add a name", "B": "Update a name", "C": "Delete a name", "D": "View List", "E": "Exit"}

print(menu)
while True:
    user_choice = input("Enter your choice from the above list: ")
    if user_choice in menu.keys():
        break
    else:
        print("Enter a choice from the Menu!!")

if user_choice == "A":
    add_name = input("Enter a name to add to the list: ")
    name_list.append(add_name)
if user_choice == "B":
    len_break = True
    while True:
        try:
            update_indx = int(input("Enter the index to update: "))
            update_indx_break = True
        except ValueError:
            print("Enter only integer!!")
            update_indx_break = False
        if update_indx >= len(name_list) and update_indx_break:
            print("Enter a number between 0 and ", len(name_list))
            len_break = False
        else:
            len_break = True
        if len_break and update_indx_break:
            break
    update_name = input("Enter the updated name: ")
    name_list[update_indx] = update_name

print(name_list)
