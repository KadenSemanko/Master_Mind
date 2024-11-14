#Kaden Semanko
#November_8.py
#11/8/24
import random as r
songs = ["snowfall", "swing lynn" , "synthwave goose", "perfect girl", "it's been a long time"] #song list
value = str(input("Enter number to shuffle, swap, and play songs(value between 1 and 5): "))# how you change song list
while value != '5':
    #swap 1st song to last
    if value == '1':
        songs.pop(0)
        print(songs, "snowfall")
    #last to first
    elif value == '2':
        songs.pop(4)
        print("It's been a long time", songs)
    #swap 1 and 2 songs
    elif value == '3':
        num = songs[0]
        songs[0] = songs[1]
        songs[1] = num
        print(songs)
    #shuffle playlist
    elif value == '4':
        r.shuffle(songs)
        print(songs)
    #plays
    elif value == '5':
        print(songs)
    else:
        print("invalid value try again")