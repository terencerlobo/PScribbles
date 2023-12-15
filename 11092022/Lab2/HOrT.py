import random
user_input = input("Enter either 'H' or 'T'")
while True:
    if user_input.lower() != 'h' and user_input.lower() != 't':
       print("Enter either 'H' or 'T'")
       user_input = input("Enter either 'H' or 'T'")
    else:
        break
    
random_choice = random.choice(['H','T'])

if user_input.lower() == random_choice.lower():
    print("You Won!!")
else:
    print("Bad luck")