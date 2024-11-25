#Kaden Semanko
#24/11/15
#practice_nov_15.py
def unique_squares(list_nums): 
    num = []
    for list_num in list_nums:
        if list_num**2 not in num:
            num.append(list_num**2)
    return num
print(unique_squares([7,2,8,1]))

import random as r
a = [i for i in range(1,366)]
b = []
for loop in range(30):
    print(a,b)
    if a == b:
        print(a,b)
        exit(0)