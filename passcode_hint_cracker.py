from itertools import permutations

# Function to get hint from user
def get_hint_from_user(hint_number, passcode_length):
    # Prompt user to enter hint and parse it into a list of integers
    hint_str = input(f"Enter Hint {hint_number} (comma-separated): ")
    hint_list = list(map(int, hint_str.split(',')))
    
    # Ask user for the number of correct digits and correct positions
    correct_digits = int(input(f"How many of those numbers are correct for Hint {hint_number}? "))
    correct_positions = int(input(f"How many are in the correct place for Hint {hint_number}? "))
    
    # Check if length of hint matches passcode length
    if len(hint_list) != passcode_length:
        print(f"Hint {hint_number} length does not match passcode length ({passcode_length}).")
        # If length does not match, recursively call get_hint_from_user until it does
        return get_hint_from_user(hint_number, passcode_length)
    
    return (hint_list, correct_digits, correct_positions)

# Function to find the passcode
def find_passcode(passcode_length, num_hints):
    hints = []
    # Iterate over the range of hint numbers
    for i in range(1, num_hints + 1):
        # Get hint from user
        hints.append(get_hint_from_user(i, passcode_length))
        
    # Iterate over permutations of digits
    for guess in permutations(range(10), passcode_length):
        # Check if guess satisfies all hints
        if all(check_guess(guess, hint) for hint in hints):
            return guess

# Function to check if guess satisfies hint
def check_guess(guess, hint):
    # Count correct digits and correct positions
    correct_digits = sum(1 for digit in guess if digit in hint[0])
    correct_positions = sum(1 for i in range(len(guess)) if guess[i] == hint[0][i])
    # Return True if guess satisfies hint, False otherwise
    return correct_digits == hint[1] and correct_positions == hint[2]

# Ask user for passcode length and number of hints
passcode_length = int(input("Enter the length of the passcode: "))
num_hints = int(input("Enter the number of hints: "))

# Find the correct passcode
passcode = find_passcode(passcode_length, num_hints)
# Print the correct passcode
print("The correct passcode is:", ''.join(map(str, passcode)))