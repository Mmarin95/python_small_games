import random
from random import randint

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''', '''
    +---+
  [O   |
  /|\  |
  / \  |
      ===''', '''
   +---+
  [O]  |
  /|\  |
  / \  |
      ===''']
WORDS = {'Colors': 'red orange yellow green blue indigo violet white black brown'.split(),
         'Shapes': 'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon '
                   'octagon'.split(),
         'Fruits': 'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango '
                   'strawberry tomato'.split(),
         'Animals': 'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard '
                    'monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle '
                    'weasel whale wolf wombat zebra'.split()
         }


# return a random word to play
def getRandomWord():
    wordsKey = random.choice(list(WORDS.keys()))
    wordIndex = randint(0, len(WORDS[wordsKey]) - 1)

    return [WORDS[wordsKey][wordIndex], wordsKey]


# get and return user letter
def getUserLetter():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print("Give me a letter... ", end="")
    while True:
        userLetter = input()
        if len(userLetter) != 1:
            print("Please only one letter")
        elif userLetter not in letters:
            print("Please introduce an actual letter")
        else:
            return userLetter.lower()


# print board
def printBoard():
    print(HANGMAN_PICS[len(missedLetters)])

    for letter in word:
        if letter in correctLetters:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print()
    print()
    print(f"Correct Letters: {correctLetters}")
    print(f"Missed Letters: {missedLetters}")
    print()


def getPlayAgain():
    print()
    print("Play again? (yes or no)", end=" ")
    userInput = input()
    if userInput == "yes" or userInput == "y":
        return True
    else:
        return False



# Main Flow
print("=== THE HANGMAN GAME ===")

difficulty = "X"
while difficulty not in "EMH":
    print('Enter difficulty: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()

if difficulty == "M":
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]

if difficulty == "H":
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

word, wordSet = getRandomWord()
missedLetters = ""
correctLetters = ""
gameDone = False

while True:
    print('The secret word is in the set: ' + wordSet)
    printBoard()

    userLetter = getUserLetter()

    if userLetter in word:

        if userLetter in correctLetters:
            print("Letter already guessed!")
            continue

        correctLetters += userLetter

        foundAllLetters = True
        for i in word:
            if i not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            gameDone = True
            print("You found all the letters!!")
            printBoard()

    else:
        missedLetters += userLetter

        if len(missedLetters) == len(HANGMAN_PICS):
            gameDone = True
            print(f"You lose, the word was {word}")

    if gameDone:
        if getPlayAgain():
            word, wordSet = getRandomWord()
            missedLetters = ""
            correctLetters = ""
            gameDone = False
        else:
            break
