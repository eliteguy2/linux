import random
import time

# List of motivational statements
motivational_statements = [
    "You've got this! Keep pushing forward.",
    "Don't give up on your dreams.",
    "Take that first step, no matter how small.",
    "Believe in yourself and you can achieve anything."
]

def main():
    # Choose a random motivational statement
    statement = random.choice(motivational_statements)
    print("\n" + statement)

def run_motivation_program():
    print("Welcome to the Motivation Program!")
    print("You'll receive motivational statements every 5 seconds.")
    print("Press Ctrl+C or type 'exit' at any time to quit.")

    last_statement = None
    try:
        while True:
            # Avoid repeating the last statement
            current_statement = random.choice(motivational_statements)
            while current_statement == last_statement:
                current_statement = random.choice(motivational_statements)
            last_statement = current_statement

            # Display the motivational statement
            print("\n" + current_statement)
            
            # Pause for 5 seconds
            time.sleep(5)
    except KeyboardInterrupt:
        # Handle user exiting with Ctrl+C
        print("\nExiting the program. Stay motivated!")

if __name__ == "__main__":
    run_motivation_program()
