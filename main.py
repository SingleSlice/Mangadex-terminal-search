#!/usr/bin/env python3
import MangaDexPy, sys

MD = MangaDexPy.MangaDex()
Userinput = sys.argv#input()

getch = _Getch()



if len(Userinput) < 2:

    print("Please input a Manga name as an argument")
else:

    print("you searched : " + str(Userinput[1]) + "\n")

    for iteration ,manga in enumerate(MD.search("manga",{"title" : Userinput[1]}, 10)): # searches the manga
        print("["+str(iteration+1)+"]" + str(manga.title["en"])) #prints the manga list

    print("\nwhich one?")
    mangaOn = int(getch())-1
    mangasc = MD.search("manga",{"title" : Userinput[1]}, 100)[mangaOn]

    print("english title : " + str(mangasc.title["en"]))
    print("tags : ", end="")
    for tags in mangasc.tags:

        print(tags.name["en"], end= "; ")
    
    print("\n\n""description")
    print("\n" + mangasc.desc["en"])

#print(MD.get_manga("ed996855-70de-449f-bba2-e8e24224c14d").title)