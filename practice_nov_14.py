#Kaden Semanko
#11/14/24
#practice_nov_14.py
def in1020(a,b):
    if a >= 10  and a <= 20: #if a is in the range(10,20) it is true 
        print(True)        
    elif b >= 10  and b <= 20: #if b is in range(10,20) it is true
        print(True)
    else:
        print(False) # outside range(10,20) for both numbers

def not_string(string):
    #check if "not" starts the string and return as is
    if "not" in string:
        print(string)
    #otherwise return "not" + string
    elif "not" not in string:
        print("not" ,string)
not_string("hello")
def not_not_string(string):
    if "not" in string:
        print(string.replace('not' , " "))
    if "not" not in string:
        print(string)
not_not_string("hello")
alien = {"home planet": "Mars",
        "number of ears": 0,  
        "number of eyes": 7,   
        "skin color": "orange"}
print(alien.keys())
print(alien.values())
print(alien.items())

for item in alien.items():
    print(item)
for key in alien.keys():
    print(key, alien[key])