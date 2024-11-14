#Kaden Semanko
#Computer makes random 4 digit number without repeats
#user gets 10 tries
#correct display as green for the charater
#yellow if correct but in the wrong spot
import random as r
value = list("1234567890")
r.shuffle(value)
secret = value[:4]
for loop in range(10):
    guess = list(input("Enter a 4-digit number(not repeats(ex:1122, doesn't work)): "))#enter value

    if guess == "" .join(secret):
        print(guess, "is correct!") #Game is finished you guessed the number
        break
    green = 0
    yellow = 0
    black = 0
    for i in range(4): #sequence list 
        if guess[i] == secret[i]:
            green += 1 # Correct digit and position
            print("green")
        elif guess[i] in secret:
            yellow += 1 # Correct digit, wrong position
            print("yellow")
        if guess[i] not in secret:
            black += 1 #Wrong digit
            print("black")
    print("Black "* black + "Green " * green + "Yellow " * yellow )
else:
    print("You lose")