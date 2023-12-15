vowels = ['a','e','i','o','u']

input_str = input("Enter a String: ")

if input_str[0].lower() not in vowels:
    input_str = input_str[1:len(input_str)] + "ay"
else:
    input_str = input_str + "way"

print(input_str)