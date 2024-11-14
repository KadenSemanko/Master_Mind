#Kaden Semanko
#Mastermind with functions
#New_Master_mind.py

##import
import random as r
##variables
attempt = 0
results = []
##function definitions
def make_secret():
    digits = [str(i) for i in range(10)]
    r.shuffle(digits)
    secret_num = digits[:4]
    return secret_num

def check_guess(user_guess, secret_num):
    results = []
    if user_guess[0] == secret_num[0]:
        results.append("green")
    elif guess in secret_num:
        results.append("yellow")
    if user_guess[1] == secret_num[1]:
        results.append("green")
    elif guess in secret_num:
        results.append("yellow")
    if user_guess[2] == secret_num[2]:
        results.append("green")
    elif user_guess in secret_num:
        results.append("yellow")
    if user_guess[3] == secret_num[3]:
        results.append("green")
    elif user_guess in secret_num:
        results.append("yellow")
    results.sort()
    return results
def check_guess_2(user_guess, secret_num):
        for i in range(3): #sequence list 
            if [i] == secret[i]:
                return "green" # Correct digit and position
                
            elif guess[i] in secret:
                return "yellow" # Correct digit, wrong position
                
            if guess[i] not in secret:
                return "black" #Wrong digit
                
#code
#I need the computer to generate a random 4 digit number with no repeats
secret = make_secret()
#I want to create a loop that continues until guess or run out
while attempt < 10 and results != ["green","green","green","green"]:
    #inside loop 
    #get input
    guess = list(input("Enter your guess(a 4 digit number with no repeat): "))
    #check against secret
    results = check_guess(guess, secret)
    #output result
    print(results)