n = "gexton"
max_num = 0

while max_num < 9:
    word = input("Enter the secret word: ")
    max_num += 1

    if word == n:
        print("Correct! You found the secret word!")
        break
    else:
        print("Wrong word, try again!")

else:
    print("Game Over")