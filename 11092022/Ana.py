def get_data():
    username = input("Enter your name: ")
    age = int(input("Enter your age: "))
    data_tuple = (username, age)
    return data_tuple

def message(username, age):
    if age <= 10:
        print("Hi", username)
    else:
        print("Hello", username)

def main():
    username, age = get_data()
    message(username, age)

main()