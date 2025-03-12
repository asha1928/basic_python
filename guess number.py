import random
random_number = random.randint(1, 20)
attempts = 0
max_attempts = 5

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 20. Can you guess it?")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess < 1 or guess > 20:
            print("Please enter a number between 1 and 20.")
            continue
        
        attempts += 1
        
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if attempts == max_attempts and guess != random_number:
    print(f"Game over! The correct number was {random_number}. Better luck next time.")