import random as r
def test_rps(p1):
    one = 0
    two = 0
    tie = 0
    while one < 3 or two < 3:
        if one == 3:
            print ("p1 wins")
            break
        if two == 3:
            print("p2 wins")
            break
        score = one , two , tie
        value = ["rock" , "paper" , "scissors"]
        r.shuffle(value)
        p2 = value[:1]
        print(p2)
        if p1 == "rock":
            if p2 == "rock":
                tie += 1
                return "tie"
        if p1 == "paper":
            if p2 == "paper":
                tie += 1
                return "tie"
        if p1 == "scissors" :
            if p2 == "scissors":
                tie += 1
                return "tie"
        if p1 == "rock": 
            if  p2 == "paper":
                two += 1
                return "p2"
        if p1 == "scissors": 
            if p2 == "paper":
                one += 1
                return "p1"
        if p1 == "paper":
            if p2 == "rock":
                one += 1
                return "p1"
        if p1 == "paper":
            if p2 == "scissors":
                two += 1
                return "p2"
        if p1 == "scissors": 
            if p2 == "rock":
                two += 1
                return "p2"
        if p1 == "rock":
            if p2 == "scissors":
                one += 1
                return "p1"
    else:
        return "not valid id"
print(test_rps("rock"))
