#Kaden Semanko
#11/21/24
#MAZE_skeleton.py
rooms = {"room1":["S","room2"],
         "room2":[("N","room1"),("E","room3")],
         "room3":[("W","room2"),("N","room5"),("E","room4")],
         "room4":[("W","room3")],
         "room5":[("S","room3"),("E","room6")],
         "room6":[("W","room5"),("N","exit")]} # Giving the commands and where it leads
def choose_direction(room):
    print("You are in a room. There are doors in the following directions")
    for direction in rooms[room]:
        return direction[0]
    value = input("Enter direction: ")
print(choose_direction("room1"))

#print(rooms.keys())
#print(rooms.values())
items = {"knife", "health spray","value boy figure"}

def hello_name(name):
  greeting = "Hello" , name , "!"
  return greeting
print(hello_name("Alice"))