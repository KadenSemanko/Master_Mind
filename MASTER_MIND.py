#Kaden Semanko
#Computer makes random 4 digit number without repeats
#user gets 10 tries
#correct display as green for the charater
#yellow if correct but in the wrong spot
#sort 1,2,3,4 if one is right in the right spot displaying green
import random as r
value = list("1234567890")
r.shuffle(value)
secret = value[0:4]
print(secret)
guess = input("enter 4 digit value: ")
for l in range(10):
    for i in range(0,3):
        if guess[i] in secret[i]:
            print("yellow", i)
        if guess[i] == secret[i]:
            print("green", i)
        if guess[0,3] == secret[0,3]:
            print(guess,"is right")
            exit(0)
