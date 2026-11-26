import random

while True:
    level = input("Level: ")
    try:
        level = int(level)
    except ValueError:
        continue
    if level <= 0:
        continue
    else:
        break

answer = random.randint(1,level)

while True:
    guess = input("Guess: ")
    try:
        guess = int(guess)
    except ValueError:
        continue
    if guess <= 0:
        continue

    if guess < answer:
        print("Too small!")

    elif guess > answer:
        print("Too large!")

    else:
        print("Just right!")
        break