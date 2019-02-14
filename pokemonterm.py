##############################################################
#                                                            #
# date: 2019/02/11                                           #
# name: Noroff Student                                       #
# description: PokeDex - Pokemon Database Search..           #
#                                                            #
##############################################################
#                                                            #
# Search for a specific Pokemon Character, and get details   #
# back from the PokeDex database.                            #
# This project uses UniCurse to be able to work on Win32     #
#                                                            #
#                                                            #
##############################################################

import requests
import json
import sys
import time
import argparse
from unicurses import *

#Argparser function to trigger on arguments
parser = argparse.ArgumentParser(description="*** The Pokemon POKEDEX ***", epilog="*** -Gotta Catch em ALL!!- ***")
parser.add_argument('-p', '--pokemon', type=str, help='Enter the name of a Pokemon..')

args = parser.parse_args()

#The PokeAPI database
pokemon_url = 'https://pokeapi.co/api/v2/pokemon/'+args.pokemon+'/'
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

#If the Pokemon exist in the API, data is scraped
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

namebox = newwin(1,sizeX -110,4,4)
wbkgd(namebox,COLOR_PAIR(3),A_BOLD)
infoPanel = new_panel(namebox)
noecho()
panel_above(namebox)

weightbox = newwin(1,sizeX -110,6,4)
wbkgd(weightbox,COLOR_PAIR(3),A_BOLD)
infoPanel = new_panel(weightbox)
noecho()
panel_above(weightbox)

heightbox = newwin(1,sizeX -110,8,4)
wbkgd(heightbox,COLOR_PAIR(3),A_BOLD)
infoPanel = new_panel(heightbox)
noecho()
panel_above(heightbox)


#All Text strings on the main window
mvwaddstr(namebox, 0, 0, name)
mvwaddstr(info, 2, 9, namedata)
mvwaddstr(weightbox, 0, 0, weight)
mvwaddstr(info, 4, 10, weightdata)
mvwaddstr(heightbox, 0, 0, height)
mvwaddstr(info, 6, 10, heightdata)
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

print("               -The End-")
consoleprint("\n"*4)
print("           You have been using")
consoleprint("\n")
print("       the Noroff POKEDEX Terminal")
consoleprint("\n"*2)
print("     A CLI-based API database lookup")
consoleprint("\n"*2)
print("               Thank you..")
consoleprint("\n"*2)
print("         - "+data['name'].capitalize()+" I CHOOSE YOU! -")
consoleprint("\n"*75)

    

