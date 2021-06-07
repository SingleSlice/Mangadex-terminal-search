#!/usr/bin/env python3
import MangaDexPy, sys
from _Getch import _Getch

MD = MangaDexPy.MangaDex()
Userinput = sys.argv#input()
getch = _Getch()

if len(Userinput) < 2:
    print("Please input a Manga name as an argument")

else:
    for iteration ,manga in enumerate(MD.search("manga",{"title" : Userinput[1]}, 10)): # searches the manga
        print("["+str(iteration+1)+"]" + str(manga.title["en"])) #prints the manga list

    mangaOn = int(getch())-1
    mangasc = MD.search("manga",{"title" : Userinput[1]}, 100)[mangaOn]

    print("\nenglish title : " + str(mangasc.title["en"]))
    print("\n-- tags --")

    for tags in mangasc.tags:
        print(tags.name["en"])
    
    print("\n""-- description --")
    print(mangasc.desc["en"])
        
        

#print(MD.get_manga("ed996855-70de-449f-bba2-e8e24224c14d").title)