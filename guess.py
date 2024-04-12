# #Guess the number game
import random

guessesTaken = 0

print('Hello! My name is guessAI and what is your name?')
myName = input()

number = random.randint(1, 100)
print('Alrighty,' + myName + 
      ', Want to guess number i am thinkig?, its between 1 and 100. And yeah you have 10 attempts')

for guessesTaken in range(10):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Ammmmm too low.')
    
    if guess > number:
        print('Hold your horses, its too high!')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Guessantastic job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess !=number:
    number = str(number)
    print('Ahhhh  nop. The number i was thinking of was' + number + '.')
