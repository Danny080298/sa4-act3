

number = 10

print("I'm thinking of a number...")
while True:
    guess = input("What number am I thinking of? (or type 'q' to quit) ")
    if guess.lower() == "q":
        print(f"The system is closed.\nThe number was {number}.")
        break
    try:
        guess = int(guess)
        if guess == number:
            print("Congratulations, your guess is correct!")
            break
        else:
            print("Invalid, try again.")
    except ValueError:
        print("Invalid. Please try again or type 'q' to quit.")
