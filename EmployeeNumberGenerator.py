# Employee Number Random Generator

"""
Format: XXX-JK-1234
XXX: Random Characters Of Length 3 In UPPER CASE Letters
JK: First Letter Of First Name & First Letter Of Last Name
1234: Random Integers Of Length 4
"""

# Importing Random & String Modules
from random import *
from string import *

# Taking User Input: Name (First Name & Last Name)
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

# Function: Generating The First Part Of The Input (XXX)
def generate_first_part():
    return "{}{}{}".format((choice(ascii_letters)).upper(), (choice(ascii_letters)).upper(), (choice(ascii_letters)).upper())

# Function: Generating The Middle Part Of The Input (JK)
def generate_middle_part(first_name, last_name):
    
    # Taking First Character Of First Name & First Character Of Last Name
    initials = first_name[0] + last_name[0]

    return initials

# Function: Generating The Last Part Of The Input (1234)
def generate_last_part():
    return ("".join(str(randint(0, 0)) for _ in range(4)))

# Function: Generate ID Number Based On The Format XXX-JK-1234
def generate_ID():
    print("Your Employee ID: ", generate_first_part() + '-' + generate_middle_part(first_name, last_name) + '-' + generate_last_part())

# Main Program
if __name__ == "__main__":
    generate_ID()