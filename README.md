# Password-Integrity-Checker
This Python script is a simple password checker that assesses the strength of a password based on various criteria including length, presence of uppercase letters, lowercase letters, numbers, and special characters.

## Features
The user is prompted to enter a password.
The script evaluates the password based on the following criteria:
Length of the password
Presence of uppercase letters
Presence of lowercase letters
Presence of numbers
Presence of special characters

## Criteria for a Secure Password
1. Length: Password length should be at least 8 characters.
2. The presence of different character types: Uppercase letters, lowercase letters, numbers, and special characters contribute to the password's strength.
3. The script checks if the entered password is among the most common passwords and advises the user to choose a different one if it is.

## Usage
Clone or download the Python script password_checker.py.
Run the script in your Python environment.
Enter a password when prompted.
The script evaluates the password and provides a score out of 8, indicating its strength.

## Additional Notes
This script utilizes the string module to check for character types in the password.
It reads a list of 10,000 most commonly used passwords from a text file to compare against the entered password.

## License
This project is licensed under the MIT license.

