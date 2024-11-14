def check_within_ten(num): #function with value inside
    if (num <= 100) and (num >= 10): #the inputed number is less than 100 but more than 10
        within_ten = True #number is in the range 
    else: # every number outside range
        within_ten = False # is False
    return within_ten #displays True or False
print(check_within_ten(73)) #True should be displayed
print(check_within_ten(95)) #True should be displayed
print(check_within_ten(103)) #False should be displayed
print(check_within_ten(117)) #False should be displayed