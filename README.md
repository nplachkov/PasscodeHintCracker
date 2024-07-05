# Passcode Solver

This script is designed to help you solve a passcode based on a series of hints. Each hint consists of a sequence of digits and provides information about how many of those digits are correct and how many are in the correct positions.

### Example passcode:
<img src="https://github.com/nplachkov/passcode-solver/assets/137792060/e13a6961-4939-4b42-b7e0-5ec67634001b" width="400" height="400">

## Features
- **User Interaction:** Prompts the user to input hints about the passcode.
- **Validation:** Ensures that the provided hints match the length of the passcode.
- **Permutation Checking:** Uses permutations to systematically check all possible passcodes.
- **Hint Checking:** Validates each guess against the provided hints to find the correct passcode.

## Requirements
- Python 3.x

## Usage

1. Clone the Repository:

```bash
git clone https://github.com/yourusername/passcode-solver.git
cd passcode-solver
```

2. Run the Script:

```bash
python passcode_solver.py
```

3. Input the Passcode Length:
- The script will prompt you to enter the length of the passcode.

4. Input the Number of Hints:
- The script will prompt you to enter the number of hints.

5. Input the Hints:
- For each hint, the script will prompt you to enter the hint as a string of digits.
- The script will also ask for the number of correct digits and the number of digits in the correct positions for each hint.

6. View the Result:
- The script will attempt to find the correct passcode based on the provided hints.
- If a passcode is found, it will be displayed. If not, a message indicating that the passcode could not be solved will be shown.

## Example
```sh
Enter the length of the passcode: 3
Enter the number of hints: 2
Enter Hint 1 (digits only): 123
How many of those numbers are correct for Hint 1? 1
How many are in the correct place for Hint 1? 1
Enter Hint 2 (digits only): 456
How many of those numbers are correct for Hint 2? 1
How many are in the correct place for Hint 2? 0
The correct passcode is: 178
```

## Support
For any issues or feature requests, please [open an issue](https://github.com/nplachkov/passcode-solver/issues) here on GitHub.

## Contributing
Contributions are welcome! Fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).
