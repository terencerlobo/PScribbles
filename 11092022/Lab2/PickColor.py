import random
color_list = ["Red","Green","Blue","Yellow","Pink"]

random_color = random.choice(color_list)
print(color_list)

while True:
    user_choice = input("Pick a color from the above list: ")
    if user_choice.lower() != random_color.lower():
        print("Wrong choice. It is as good as ", random_color.upper(), ". Try again!!")
    else:
        print("Well Done!! You Got it right this time!!")
        break