from itertools import permutations

def get_hint_from_user(hint_number, passcode_length):
    # Prompt user to enter hint as a single string of digits
    hint_str = input(f"Enter Hint {hint_number} (digits only): ")
    
    # Ensure the length of the hint matches the passcode length
    if len(hint_str) != passcode_length:
        print(f"Hint {hint_number} length does not match passcode length ({passcode_length}).")
        # If length does not match, recursively call get_hint_from_user until it does
        return get_hint_from_user(hint_number, passcode_length)
    
    # Parse each character of the hint string as an integer and return as a list
    hint_list = [int(digit) for digit in hint_str]
    
    # Ask user for the number of correct digits and correct positions
    correct_digits = int(input(f"How many of those numbers are correct for Hint {hint_number}? "))
    correct_positions = int(input(f"How many are in the correct place for Hint {hint_number}? "))
    return (hint_list, correct_digits, correct_positions)

def find_passcode(passcode_length, num_hints):
    hints = []
    for i in range(1, num_hints + 1):
        hints.append(get_hint_from_user(i, passcode_length))
        
    for guess in permutations(range(10), passcode_length):
        if all(check_guess(guess, hint) for hint in hints):
            return guess
    # If no passcode is found after all permutations, return None
    return None

def check_guess(guess, hint):
    correct_digits = sum(1 for digit in guess if digit in hint[0])
    correct_positions = sum(1 for i in range(len(guess)) if guess[i] == hint[0][i])
    return correct_digits == hint[1] and correct_positions == hint[2]

passcode_length = int(input("Enter the length of the passcode: "))
num_hints = int(input("Enter the number of hints: "))

# Find the correct passcode
passcode = find_passcode(passcode_length, num_hints)

# Check if passcode is found
if passcode is not None:
    print("The correct passcode is:", ''.join(map(str, passcode)))
else:
    print("Unable to solve the passcode.")
