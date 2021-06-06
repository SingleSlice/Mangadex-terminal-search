from MangaDexPy import manga
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import MangaDexPy

MD = MangaDexPy.MangaDex()

print("search :")
bababooey = input()

for iteration ,manga in enumerate(MD.search("manga",{"title" : bababooey}, 10)):
    
    print(str(iteration) + str(manga.title["en"]))

print("which one?")
mangaOn = int(input())
mangasc = MD.search("manga",{"title" : bababooey}, 100)[mangaOn]

print(mangasc.title["en"])

#print(MD.get_manga("ed996855-70de-449f-bba2-e8e24224c14d").title)