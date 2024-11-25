#ask user for 2 numbers
#print larger number of the two
a = int(input("enter value: "))
b = int(input("enter 2nd value: "))
if a > b:
    print(f"{a} is bigger")
else:
    print(f"{b} is bigger(or they are equal)")


def find_max(a,b):
    if a > b:
        return a
    return b

def top_two(a,b,c,d,e,f):
    stuff = [a,b,c,d,e,f]
    stuff.sort()
    return (stuff[-1] ,stuff[-2])

largest = top_two(345,6457,2234,6578,2,340)
biggest , next_biggest = top_two(345,6457,2234,6578,2,340)
print(next_biggest)