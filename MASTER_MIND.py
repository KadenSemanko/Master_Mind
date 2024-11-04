#Kaden Semanko
#Computer makes random 4 digit number without repeats
#user gets 10 tries
#correct display as green for the charater
#yellow if correct but in the wrong spot
#sort 1,2,3,4 if one is right in the right spot displaying green
import random as r
value = list("1234567890")
r.shuffle(value)
secret = value[:4]
for _ in range(10):
    guess = input("Enter a 4-digit number(not repeats(ex:1111 doesn't work)): ")

    if guess == "" .join(secret):
        print(guess, "is correct!") #Game is finished you guessed the number
        break
    green = 0
    yellow = 0
    black = 0
    for i in range(4):
        if guess[i] == secret[i]:
            green += 1 # Correct digit and position
            print("green")
        elif guess[i] in secret:
            yellow += 1 # Correct digit, wrong position
            print("yellow")
        if guess[i] not in secret:
            black += 1 #Wrong digit, not in number
            print("black")
    print("Black "* black + "Green " * green + "Yellow " * yellow )
    if green == 0 and yellow == 0:
        print("try again")