from validator_collection import validators, errors
import sys

email = input("What's your email address? ")

try:
    email_val = validators.email(email)
except errors.InvalidEmailError:
    print("Invalid")
else:
    print("Valid")