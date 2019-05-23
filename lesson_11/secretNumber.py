import random
import json
import datetime


secret = random.randint(1, 30)
attempts = 0
username = input("what is your name? ")
list_guesses = []

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print(str(score_list))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_date = {"attempts": attempts, "date": str(datetime.datetime.now()), "name": username, "wrong_guesses": list_guesses }
        score_list.append(score_date)

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
        list_guesses.append(guess)
    elif guess < secret:
        list_guesses.append(guess)
        print("Your guess is not correct... try something bigger")