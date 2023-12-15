favourite_song = input("Enter the first line of your favourite song:").strip()

print("The length: ", len(favourite_song))

try:
    starting_num = int(input("Enter the starting number:"))
except ValueError:
    print("Enter only integers.")
    starting_num = int(input("Enter the starting number:"))
try:
    ending_num = int(input("Enter the ending number:"))
except ValueError:
    print("Enter only integers.")
    ending_num = int(input("Enter the ending number:"))


if starting_num < len(favourite_song) and ending_num < len(favourite_song) and starting_num < ending_num:
    print(favourite_song[starting_num:ending_num])
else:
    print("Not a valid input")