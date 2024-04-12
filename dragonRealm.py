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
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you treasure!')
        return True
    else:
        print('Gobbles you down in one bite!')
        return False

def play():
    correctGuesses = 0  # Counter for correct guesses
    displayIntro()
    while True:
        caveNumber = chooseCave()
        if checkCave(caveNumber):
            correctGuesses += 1
            print("\nYou venture deeper into the dragon land...")
        else:
            break
        
    print(f'Game over! You guessed {correctGuesses} caves correctly.')
    print('Do you want to play again? (yes or no)')
    return input()
    
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    playAgain = play()