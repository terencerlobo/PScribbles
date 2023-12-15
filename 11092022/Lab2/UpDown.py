def number_input():
    while True:
        try:
         loop_count = int(input("Enter the count: "))
         break
        except ValueError:
         print("Enter only Numbers!!")
    
    return loop_count

up_or_down = input("Enter Up or Down: ").lower()



while True:
    if up_or_down != "up" and up_or_down != "down":
        print("I don't understand!! Enter again")
        up_or_down = input("Enter Up or Down: ").lower()
    else:
        break

loop_count = number_input()

while True:
    if up_or_down == "down" and loop_count > 20:
        print("Enter number within 20!! Enter again")
        loop_count = number_input()
    else:
        break

if up_or_down == "up":
    for indx in range(0, loop_count):
        print("Index is: ", indx)
elif up_or_down == "down":
    for indx in range(loop_count, 0, -1):
        print("Index is: ", indx)



