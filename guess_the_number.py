import random

def guess_the_number():
    low = 0
    high = int(input("Enter your number : "))

    guess = random.randint(low, high)
    while True:
        user_guess = int(input("Enter your guess : "))
        if user_guess < guess:
            print("You are too low !!! . Try again")
            continue
        elif user_guess > guess:
            print("You are too high !!! . Try again")
            continue
        elif user_guess == guess:
            print(f"You got the number {guess} right. Yay!!!")
            break
        else:
            print("Invalid input")

    print("Thank you for playing")

guess_the_number()