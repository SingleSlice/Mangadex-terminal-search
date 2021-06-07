import MangaDexPy, sys

MD = MangaDexPy.MangaDex()

print("search :")
Userinput = sys.argv#input()

if len(Userinput) < 2:

    print("sus")
else:

    print("you searched : " + str(Userinput[1]) + "\n")
    for iteration ,manga in enumerate(MD.search("manga",{"title" : Userinput[1]}, 10)):

        print(str(iteration) + str(manga.title["en"]))

    print("which one?")
    mangaOn = int(input())
    mangasc = MD.search("manga",{"title" : Userinput[1]}, 100)[mangaOn]

    print(mangasc.title["en"])

#print(MD.get_manga("ed996855-70de-449f-bba2-e8e24224c14d").title)