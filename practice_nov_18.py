import random as r
def make_random_limit(a,b,c): # 3 inputs 1st is range 2nd is base number and 3rd is max number
    value = [] #made it a list
    for a in range(a): #range used
        num = r.randint(b,c) #random number in between b and c, a of times
        value.append(num) #add it to the list
    return value # returns the value
print(make_random_limit(23,1,365))

def ask_for_list():
    a = int(input("Enter range number: ")) 
    b = int(input("Enter lowest number: ")) # your numbers that user inputs
    c = int(input("Enter highest number: ")) 
    return make_random_limit(a,b,c) # inputs a created function
#print(ask_for_list())

def birthdays():
    for i in range(1):
        a = r.randint(1,12)
        if a == 2:
                b = r.randint(1,29)
        if a == 4 or a == 6 or a == 9 or a == 11:
            b = r.randint(1,30)
        b = r.randint(1,31)
        print(a ,"/", b)
birthdays()