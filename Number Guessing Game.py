import random

def number_guessing_game():
    """
    A number guessing game where the computer picks a random number
    and the user tries to guess it.
    """
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print(f"You have {max_attempts} attempts to guess the number.")
    
    while attempts < max_attempts:
        try:
            # Get user's guess
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess < secret_number:
                print("Too low! 📉 Try a higher number.")
            elif guess > secret_number:
                print("Too high! 📈 Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break
                
            # Give hint when few attempts remain
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"You have {remaining_attempts} attempts remaining.")
            else:
                print(f"❌ Game over! The number was {secret_number}.")
                
        except ValueError:
            print("⚠️ Please enter a valid number!")
    
    # Ask if user wants to play again
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again in ['yes', 'y']:
        number_guessing_game()
    else:
        print("Thanks for playing! 👋")

# Run the game
if __name__ == "__main__":
    number_guessing_game()