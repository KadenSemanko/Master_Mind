#Kaden Semanko
#11/22/24
# practice_nov_22.py
def string_splosion(str):
    secret = [] #list to put in one line(many ways)
    value = len(str) #assignment to elements #
    for i in range(value): #repeating number of times
        secret.append(str[0:i+1]) #start cutoff 1 before element limit +1 to reach limit
        v2 = ''.join(secret) # join them to display as one
    return v2 # return wanted value
print(string_splosion("code"))
print(string_splosion("abc"))
print(string_splosion("hello"))

def string_splosionv2(str):
    exploded = ""
    value = len(str)
    for i in range(value):
        exploded += str[0:i]
    return exploded + str

print(string_splosionv2("code"))
print(string_splosionv2("abc"))
print(string_splosionv2("hello"))

def find_roots(a,b,c):
    root1 = (-b+(b*b-4*a*c)**0.5)/2*a
    root2 = (-b-(b*b-4*a*c)**0.5)/2*a
    return root1, root2


students = ["Braeden", "Kaden", "Aiden"]
grades = ["3.6", "3.36", "3.4"]
suits = ["spades", "diamond", "clubs"]
nums = ["1","2","3","4","5","6","7","8","9","10"]
print ((students[1]),(grades[1]),(suits[0]),(nums[2]))