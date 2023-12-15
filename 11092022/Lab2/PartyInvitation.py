friend_list = []
for indx  in range(0,3):
    friend_list.append(input("Enter your friend name: "))

need_more = input("Do you want to add more? Hint: Say Yes or No: ")

while need_more.lower() == "yes":
    friend_list.append(input("Enter your friend name: "))
    need_more = input("Do you want to add more? Hint: Say Yes or No: ")

print(friend_list)