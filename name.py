import random

game_number = random.randint(1,10)
#print(game_number)
guess_count = 0
while (True): 
    guess = int(input("Guess a number between 1 and 10: "))
    guess_count += 1

    if guess > game_number:
        print("Too high! Try again.")
    elif guess < game_number:
        print("Too low! Try again.")
    else:
        print(f"Congratulations! You guessed the correct number in {guess_count} guesses.")
        if guess_count < 4:
            print("Good job!")
        else:
            print("You can do better!")
        break