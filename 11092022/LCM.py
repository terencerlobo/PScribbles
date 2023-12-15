def least_common_multiple(num1, num2):
    if num1 >= num2:
        greater = num1
    elif num1 < num2:
        greater = num2
    
    

    while(True):
        if ((greater % num1 == 0) and (greater % num2 == 0)):
            lcm = greater
            break

        greater = greater + 1
    
    return lcm


print(least_common_multiple(5,5))


