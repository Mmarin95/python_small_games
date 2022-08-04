from random import randint
from time import sleep


def printIntroduction():
    print("""You are hungry in the mall parking spot, and you can go to two different shops to buy a snack.
    Suddenly you see your annoying neighbour, Carl, coming inside the mall with the groceries shopping car...""")
    print("You have to choose the shop wisely, one mistake and you'll have to meet your neighbour...")


def choosePath():
    shop = ''
    while shop != '1' and shop != '2':
        print('Which shop will you choose? (1 or 2)')
        shop = input()

    return shop


def checkPath(userPath):
    print('You approach to the chosen shop...')
    sleep(2)
    print('You choose your favorite snack...')
    sleep(2)
    print('Finally you are on the line to pay, happy because you can enjoy your snack...')
    print()
    sleep(2)

    neighbourPath = str(randint(1, 2))

    if neighbourPath == userPath:
        print('And in the last moment Carl appears and invites you to a boring party! :/')
    else:
        print('And you pay and go home without meeting Carl :D')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    printIntroduction()
    userPath = choosePath()
    checkPath(userPath)

    print()
    print('Play again? (yes or no)')
    playAgain = input()
