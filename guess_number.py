

number = 10
try_guess = 0
limited = 5
print("I'm thinking of a number...")
while try_guess != limited:
    guess = input("What number am I thinking of? (or type 'q' to quit) ")
    if guess.lower() == "q":
        print(f"The system is closed.\nThe number was {number}.")
        break
    try:
        guess = int(guess)
        if guess == number:
            print("Congratulations, your guess is correct!!!")
            break
        elif guess > number:
            print("Your guess is too high, try again!!")
        elif guess < number:
            print("Your guess is too low, try again!!")
        else:
            print(f"Invalid, try again, you have {limited- 1} trials lefts.")  
            limited -= 1
            if limited == 0:
                print("You run out of trials")
                print(f"The system is closed.\nThe number was {number}.")
                break
    except ValueError:
        print("Invalid. Please try again or type 'q' to quit.")

    try_guess += 1
