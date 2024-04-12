import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you, you see
          two caves. In one cave, the dragon is friendly and will share his treasures with you.
           The other dragon is greedy and hungry, and will eat you on sight.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    