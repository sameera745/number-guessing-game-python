import random

print("🎲 Welcome to the Number Guessing Game!")

play_again = "yes"
while play_again.lower() in ["yes", "y"]:
    number = random.randint(1, 10)
    guess = 0
    tries = 0

    print("\nI have chosen a number between 1 and 10. Can you guess it?")

    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        tries += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"✅ Correct! You guessed the number in {tries} tries.")

        if guess != number and abs(guess - number) <= 2:
            print("💡 Hint: You're very close!")

    play_again = input("Do you want to play again? (yes/no): ")

print("🎉 Thanks for playing! Goodbye!")
