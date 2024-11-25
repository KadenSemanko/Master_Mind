#Kaden Semanko
#11/21/24
#MAZE_skeleton.py
rooms = {"room1":["S","room2"],
         "room2":[("N","room1"),("E","room3")],
         "room3":[("W","room2"),("N","room5"),("E","room4")],
         "room4":[("W","room3")],
         "room5":[("S","room3"),("E","room6")],
         "room6":["W","room5"]} # Giving the commands and where it leads
def choose_direction(room):
    print("You are in a room. There are doors in the following directions")
    for direction in rooms[room]:
        print(direction[0])
    value = input("Enter direction: ")
    if value == "S":
        room == "room2"
        print(direction)
        for direction in rooms[room]:
            print(direction[0])
choose_direction("room1")