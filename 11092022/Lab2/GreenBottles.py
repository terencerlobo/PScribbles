no_of_green_bottles = 10

while no_of_green_bottles != 0:
    print("There are ", no_of_green_bottles, " hanging on the wall, and is 1 green bottle should accidently fall.")
    print("There are no more green bottles hanging on the wall!!")
    no_of_green_bottles = no_of_green_bottles -1
    while True:
        while True:
            try:
                user_input = int(input("How many green bottles will be hanging on the wall? "))
                break
            except ValueError:
                print("Enter only Integer!! Try again!!")
         
        if user_input == no_of_green_bottles:
            if no_of_green_bottles != 0:
                print("There will be ", no_of_green_bottles, " green bottles hanging on the wall.")
            else:
                print("There are no more green bottles hanging on the wall!!") 
            break
        else:
            print("No, try again")
        