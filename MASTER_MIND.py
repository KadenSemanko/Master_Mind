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
print("Secret code (for testing):", (secret))
for _ in range(10):
    guess = input("Enter a 4-digit code: ")

    if guess == ''.join(secret):
        print(guess, "is correct!")
        break
    for i in range(4):
        if guess[i] == secret[i]:
            print("green", i)  # Correct digit and position
        elif guess[i] in secret:
            print("yellow", i)  # Correct digit, wrong position
    else:
        print("Try again.")
