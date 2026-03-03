n = 18
guesses = 0

while guesses < 9:
    guess = int(input("Guess the number: "))
    guesses = guesses + 1

    if guess < n:
        print("Too low! Try a bigger number.")
    elif guess > n:
        print("Too high! Try a smaller number.")
    else:
        print("Correct! You won in", guesses, "tries.")
        break

if guesses == 9:
    print("Game Over! You used all 9 attempts.")