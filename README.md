# CLI-PokeDex for Windows

A CLI based Pokemon lookup. 

### Prerequisites

You will need some modules to make this work..

```
* requests
* unicurses
* argparse
```
This project uses UniCurses (yes i know it's old) to make it visually fancy for windows users.
Due to this the DLL file needs to follow the project file. I think you could also place it into your interpreter folder.

**Windows:**
Should work fine, but some has reported issues with "panels".
DLL should be placed in the interpreter folder..
Ex: C:\user\<username>\appdata\local\programs\python\<python version>\)

**Linux:**
Won't work due to Unicurse, It's said to be cross platform, but feel free to try. 

### Installing

To install the Prerequisites, simply run the following command:

```
pip install -r requirements.txt
```
# Usage

**Help**
```
pokemonterm.py -h
```
**Pokemon**
```
ex:
pokemonterm.py -p kakuna
```
# Support
Would love to help you, but i'm only an amature developer soooo.. No, sorry!
The code is probably full of BUGS, and there is probably a much better solution to this,
but this was made with love, and passion........
Okay well, it's what i could do at the moment with the current knowledge.
But HEY, i'm still learning :)

# Screenshot
![Alt text](https://www.digitalbrekke.com/res/pokemontermScreenShot.png "Main Screen")
