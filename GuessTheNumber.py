from random import randint

print("Welcome to GuessTheNumber game!")
print("What is your name?")
playerName = input()
print(f"Welcome, {playerName}! I am thinking about a number between 1 - 20...")
print("You have 5 tries to guess the number")

randomNumber = randint(1, 20)
triesToWin = -1

for t in range(1, 7):
    print("Take a guess...")
    guess = int(input())

    if guess > randomNumber:
        print("Your guess is too high")
    elif guess < randomNumber:
        print("Your guess is too low")
    elif guess == randomNumber:
        triesToWin = t
        break

if triesToWin < 0:
    print(f"Sorry, no more tries, the number I was thinking was {randomNumber}.")
    print(f"Bad Luck {playerName}, try again next time.")
else:
    print(f"Congratulations {playerName}, you guessed the number in {triesToWin} tries!")

