import re
import datetime

test_str = "gfdgd2312Ms!@"
arr = re.findall(r'[/\d/]', test_str)

for a in arr:
    print(a, " ==> a")
print(re.search(r'[/\d/]', test_str))

date_var1 = datetime.datetime(2022,8,10)
date_var2 = datetime.datetime(2022,9,11)


string_str = "AB CD"
print(string_str.split(" ")[0])

print(date_var2 > date_var1)