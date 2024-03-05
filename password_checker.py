#Let's make a simple password checker
#First we import the string library
import string

#let's assume the password is so...
password = input("Enter a password: ")

#What are the things we consider a secure password to have.
#Length, uppercase letters, lowercase letters, numbers and special characters.
#Let's see what it could possibly look like.
#Score one point for each character the password possesses
upper_case = [1 if c in string.ascii_uppercase else 0 for c in password]
lower_case = [1 if c in string.ascii_lowercase else 0 for c in password]
punctuations = [1 if c in string.punctuation else 0 for c in password]
digits = [1 if c in string.digits else 0 for c in password]

#Generate a list of characters found in the password. 
#Assign a value of 1 to each character present in the password, and 0 to those that are not.
characters = [upper_case, lower_case, punctuations, digits]
print (characters)
score = 0

#Add a point to your score for each character present in your password
if sum(upper_case) > 0:
    score += 1
if sum(lower_case) > 0:
    score += 1
if sum(punctuations) > 0:
    score += 1
if sum(digits) > 0:
    score += 1


#Ideally, the project is a password checker, so it should score or grade your password based on some
#STANDARD parameters

#First we need to rule it out of the most common passwords.
#I got a .txt file with a list of 10,000 most commonly used words from (https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt)
#The code opens the file with open() as a string,
#Then, it splits the string to an array with splitlines() to create a Python list.
#Basically makes every password in a line as a variable in the new list "common_passwords".

#common_passwords = '10k-most-common.txt'
with open('10k-most-common.txt', "r") as file:
  passwordList = file.read().splitlines()

if password in passwordList:
    print("Don't be sleek. Use something else")

#The longer your password, the better. 
#A point for each additional 4 variables you have in your password.
    
length = len(password)
if length < 8:
    print("Weak: Password length should be at least 8 characters.")
if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 16:
    score += 1
if length > 20:
    score += 1

#The highest score you can get is 8
print ("Your score is: " + str(score) + "/8")
