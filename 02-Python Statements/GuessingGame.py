import random


# Introduction to the game and ask if the player is ready and want to start the game
intro = ['\nWelcome to the Guessing Game\n', "In this game you'll need to guess a random number between 1 and 100!" ]
for line in intro:
    print(line)

start = input("Are you ready to play? ('y' for yes / 'n' for no) ")
while start.lower() == 'y':
    number = random.randint(1,100)
    guessed = False
    guesses = []
        
    while guessed == False:
        guess = int(input("What's your guess? "))


        guess = int(guess)
        guesses.append(guess)
        
        if guess == number:
            guessed = True
            break

        elif guess > 100 or guess < 1:
            print("OUT OF BOUNDS")
            continue

        elif len(guesses) == 1:
            if guess in range(number-10, number+10):
                print('WARM!')
                continue
            else:
                print('COLD!')
                continue
        
        else:
            if abs(number - guesses[-2]) > abs(number - guess):
                print('WARMER!')
            else:
                print('COLDER!')

    if guessed == True:
        print(f"CONGRATILATION YOU'VE GUESSED THE RANDOM NUMBER {number} IN {len(guesses)} GUESSES!\n")
        start = input("Are you ready to play again? ('y' for yes / 'n' for no) ")

print('\nThank you! See you next time')