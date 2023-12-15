while True:
    try:
        day_old_bread_count = int(input("Enter the number of loaves of day old bread: "))
        break
    except ValueError:
        print("Enter a valid integer!!")
    

regular_price = day_old_bread_count * 3.49
discounted_price = (60*regular_price)/100

print(round(regular_price,2))
print(round(discounted_price,2))