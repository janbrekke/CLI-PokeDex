#####################################################################
#                                                                   #
# date: 2019/02/11                                                  #
# name: Jan Brekke                                                  #
# description: PokeDex - Pokemon Database Search..                  #
#                                                                   #
#####################################################################
#                                                                   #
# Search for a specific Pokemon Character, and get details          #
# back from the PokeDex database.                                   #
# This project uses UniCurse to be able to work on Win32            #
# Have had some issues making this work on linux due to             #
# Unicurse, and too lazy right now to solve it..                    #
# Should work fine on Windows.                                      #
#                                                                   #
# pdcurses.dll should follow the project and/or be placed into      #
# the Python interpreter folder                                     #
# Ex: C:\Users\USERname\AppData\Local\Programs\Python\Python37-32   #
#                                                                   #
# Also this should be installed should it still not work (Sorry)    #
# https://sourceforge.net/projects/pyunicurses/                     #                                                        
#                                                                   #
#####################################################################

import requests
import json
import sys
import time
import argparse
from unicurses import *


#Argparser function to trigger on arguments
parser = argparse.ArgumentParser(description="*** The Pokemon POKEDEX ***", epilog="*** -Gotta Catch em ALL!!- ***")
parser.add_argument('-p', '--pokemon', type=str, help='Enter the name or ID of a Pokemon..')

args = parser.parse_args()

#The PokeAPI database
pokemon_url = 'https://pokeapi.co/api/v2/pokemon/'+args.pokemon.lower()+'/'
pokemon_response = requests.get(pokemon_url)

#Two empty list used by the FOR loops to append their findings
categoryList = []
abilityList = []

#Makes a custom print function.
#Used here to make the scroll effect in the end. Modify time.sleep(X) to change speed.
def consoleprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.3) #time is in seconds

def consoleprint2(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05) #time is in seconds

def consoleprint3(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1) #time is in seconds


#If the Pokemon exist in the API, data is scraped
while True:
    if pokemon_response.status_code == 200:
        data = json.loads(pokemon_response.text)
        name = 'Name: '
        namedata = data['name'].capitalize() + ' (id:'+ str(data['id']) + ')' 
        weight = 'Weight: '
        weightdata = str(data['weight']/10)+' kg'
        height = 'Height: '
        heightdata = str(data['height']/10)+' Meters'
        category = 'Category:'

        #FOR loops used to make sure all data under this category is scraped since the Pokemon's have different numbers of ex: abilities 
        for i in data['types']:
            categoryList.append('-> '+i['type']['name'].capitalize())
        ability = 'Abilities:'

        for i in data['abilities']:
           abilityList.append('-> '+i['ability']['name'].capitalize())

        break
    else:
        print("\n"*100)
        print("          ----------------------------------------------")
        print("         |")
        print("---------|Can't find any Pokemon called "+args.pokemon.capitalize())
        print("---------|Try these out; \"Kakuna\" or \"Ninetales\"")
        print("         |")
        print("          ----------------------------------------------\n\n\n")
        exit()



#Visual loading screen at the begining
print("\n"*100)
print("----------------------------------------------------------------\n")
print("\t\tInitializing - Please wait::")
print("\nLoading CGA Graphics")
consoleprint2("|########25%###########50%#############75%##########|")
print("\n\nGathering information about --> "+data['name'].capitalize()+" <-- ")
consoleprint2("|########25%######")
consoleprint("#####50%#############75%###")
consoleprint3("#######|")
print("\n\nLoading text formater")
consoleprint2("|########25%###########50%#############75%##########|")
print("\n\n\nLoading Complete..\nStarting up Interface..\n\n      -Enjoy!-")
time.sleep(5)

#Formats both FOR loops for "Category" and "Ability"
categoryPrint = "\n  ".join(categoryList)
abilityPrint = "\n  ".join(abilityList)

#Starts the main unicurses screen
stdscr = initscr()  
start_color()

curs_set(0) #Disables the terminal character cursor
noecho()
cbreak()

#Color Pairs
init_pair(1, COLOR_YELLOW, COLOR_CYAN)
init_pair(2, COLOR_MAGENTA, COLOR_BLACK)
init_pair(3, COLOR_YELLOW, COLOR_BLACK)

size = getmaxyx(stdscr)

sizeX = size[1]
sizeY = size[0] 
    
#All graphics and it's location on the main screen
bg = newwin(sizeY, sizeX, 0, 0)
box(bg) 
wbkgd(bg,COLOR_PAIR(1)+A_BOLD)
bgPanel = new_panel(bg)
noecho()
panel_below(bg)

info = newwin(20,sizeX -40,2,2)
box(info)
wbkgd(info,COLOR_PAIR(2),A_BOLD)
infoPanel = new_panel(info)
noecho()

categorybox = newwin(1,sizeX -105,10,4)
wbkgd(categorybox,COLOR_PAIR(3),A_BOLD)
infoPanel = new_panel(categorybox)
noecho()
panel_above(categorybox)

categorybox2 = newwin(10,sizeX -90,11,4)
wbkgd(categorybox2,COLOR_PAIR(2),A_BOLD)
infoPanel = new_panel(categorybox2)
noecho()
panel_above(category)

abilitybox = newwin(1,sizeX -105,10,33)
wbkgd(abilitybox,COLOR_PAIR(3),A_BOLD)
infoPanel = new_panel(abilitybox)
noecho()
panel_above(abilitybox)

abilitybox2 = newwin(10,sizeX -90,11,35)
wbkgd(abilitybox2,COLOR_PAIR(2),A_BOLD)
infoPanel = new_panel(abilitybox2)
noecho()
panel_above(abilitybox2)

namebox = newwin(1,sizeX -112,4,4)
wbkgd(namebox,COLOR_PAIR(3),A_BOLD)
infoPanel = new_panel(namebox)
noecho()
panel_above(namebox)

weightbox = newwin(1,sizeX -112,6,4)
wbkgd(weightbox,COLOR_PAIR(3),A_BOLD)
infoPanel = new_panel(weightbox)
noecho()
panel_above(weightbox)

heightbox = newwin(1,sizeX -112,8,4)
wbkgd(heightbox,COLOR_PAIR(3),A_BOLD)
infoPanel = new_panel(heightbox)
noecho()
panel_above(heightbox)


#All Text strings on the main window
mvwaddstr(namebox, 0, 0, name)
mvwaddstr(info, 2, 15, namedata)
mvwaddstr(weightbox, 0, 0, weight)
mvwaddstr(info, 4, 15, weightdata)
mvwaddstr(heightbox, 0, 0, height)
mvwaddstr(info, 6, 15, heightdata)
mvwaddstr(categorybox, 0, 0, category)
mvwaddstr(categorybox2, 1, 1, categoryPrint)
mvwaddstr(abilitybox, 0, 0, ability)
mvwaddstr(abilitybox2, 1, 1, abilityPrint)

mvwaddstr(bg, 0, 25, "*** The Pokemon POKEDEX ***")
mvwaddstr(bg, sizeY - 2, 1, "Hit Escape to EXIT..")

update_panels()
doupdate()

size = getmaxyx(stdscr)

#Hitting the escape key will quit the software
running = True
while (running):
    key = getch( )
    if (key == 27):
        running = False
        break

wclear(bg)
wrefresh(bg)
endwin()


#End Screen roll
print("\n"*100)
print("               -The End-")
consoleprint("\n"*4)
print("           You have been using")
consoleprint("\n")
print("       the DigitalBrekke POKEDEX Terminal")
consoleprint("\n"*2)
print("     A CLI-based API database lookup")
consoleprint("\n"*2)
print("               Thank you..")
consoleprint("\n"*2)
print("         - "+data['name'].capitalize()+" I CHOOSE YOU! -")
consoleprint("\n"*75)

    
