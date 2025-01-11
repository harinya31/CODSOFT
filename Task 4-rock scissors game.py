
import random  # Import the 'random' module for generating random choices

print("\nLet's play Rock-Paper-Scissors!")  # Display an introduction message
choices = ["rock", "paper", "scissors"]  # Define the available choices

while True:  # Start an infinite loop
    user_choice = input("Choose Rock, Paper, or Scissors (or type 'quit' to exit): ").strip().lower()  # Get user input

    if user_choice == "quit" or user_choice == "exit":  # Check if user wants to quit
        print("Thanks for playing! Goodbye!")  # Display a farewell message
        break  # Exit the loop if user wants to quit

    if user_choice in choices:  # Check if user choice is valid
        computer_choice = random.choice(choices)  # Generate a random computer choice

        # Display user and computer choices
        print(f"Your choice: {user_choice.capitalize()}")
        print(f"Computer's choice: {computer_choice.capitalize()}")

        # Determine the winner based on the choices
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")
        else:
            print("Computer wins!")
    else:
        print("Invalid choice. Please choose Rock, Paper, or Scissors or type 'quit' to exit.")
