'''Implement a Python function print_numbers(n) that uses a while loop to print numbers from 1 to n (inclusive), where n is a positive integer provided as input to the function.'''
def print_numbers(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    i = 1
    while i <= n:
        print(i)
        i += 1

# Example usage:
print_numbers(5)
'''Write a Python program that simulates a simple bank account system. The system should use a while loop to continuously prompt the user for actions (deposit, withdraw, check balance) until the user decides to exit. The initial balance should be $1000'''
def bank_system():
    balance = 1000
    while True:
        print("\n--- Bank Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print(f"${amount} deposited successfully.")
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            if amount > balance:
                print("Insufficient funds!")
            else:
                balance -= amount
                print(f"${amount} withdrawn successfully.")
        elif choice == "3":
            print(f"Your current balance is: ${balance}")
        elif choice == "4":
            print("Exiting... Thank you for using our bank system!")
            break
        else:
            print("Invalid choice. Please try again.")
bank_system()
'''Create a function find_factorial(n) that calculates the factorial of a given number n using a while loop. The function should handle cases where n is less than 0 by raising a ValueError'''
def find_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result
print(find_factorial(5)) 
# Develop a simple number guessing game where the computer thinks of a number between 1 and 100, and the user has to guess it. After each guess, the computer should give a hint (higher or lower) using a while loop to repeatedly ask for guesses until the correct number is guessed
import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Guess the number between 1 and 100!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        # Count attempts
        attempts += 1

        # Check if guess is out of range
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        if guess < number_to_guess:
            print("Higher!")
        elif guess > number_to_guess:
            print("Lower!")
        else:
            print(f"🎉 Congratulations! You guessed it right in {attempts} attempts.")
            break
guessing_game()
