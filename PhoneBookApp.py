# Phone Book App

"""
Using Dictionary & Functions To Create A Phone Book App
That Has The Following Abilities:
1. View The Phone Book
2. Add A Contact
3. Edit A Contact
4. Delete A Contact
5. Search A Contact
6. Exit
Implementing The CRUD Functionality
"""

# Importing The System Module
from sys import *

# Creating Two Empty Dictionaries For Storing Contact Details
phone_book = {}
draft_phone_book = {}

# Checking Whether The Phone Book Is Empty Or Not
def is_empty(phone_book):
    if phone_book:
        return False
    else:
        return True

# Function: View Phone Book
def view(phone_book):
    print("Contact List: ", phone_book)

# Function: Add Contact In Phone Book
def add(phone_book):
    while True:
        name = input("Enter Contact Name: ")
        phone = input("Enter Contact Phone: ")

        # Input Validation Check
        if name.isalpha() and phone.isdecimal():
            phone_book[name] = phone
            print("New Contact Added: ", phone_book)
            break

        print("ERROR: Wrong Input Type. Please Enter Alphabets For Name & Numbers For Phone.")

# Function: Edit An Existing Contact In Phone Book
def edit_name(phone_book):
    while True:
        name = input("Enter The Name Of The Contact You Want To Edit: ")
        new_replacable_name = input("Enter The New Replacable Name: ")

        # Input Validation Check
        if name.isalpha() or new_replacable_name.isalpha():
            if phone_book.get(name) != None:
                phone_book[new_replacable_name] = phone_book.pop(name)
                print("Name Changed From", name, "to", new_replacable_name)
                print("Updated Phone Book: ", phone_book)
                break
            else:
                print("ERROR: Contact Name Not Found! Please Enter The Correct Contact Name.")
        else:
            print("ERROR: Wrong Input Type! Please Enter Alphabets For Both Name & The New Replacable Name.")

# Function: Edit An Existing Contact Phone In Phone Book
def edit_phone(phone_book):
    while True:
        name_search = input("Enter The Name Of The Contact Whose Phone Number You Would Like To Edit In The Phone Book: ")
        phone_edit = input("Enter The New Phone Number: ")

        # Input Validation Check
        if name_search.isalpha() or phone_edit.isdecimal():
            if phone_book.get(name_search) != None:

                # Storing The New Phone Number In A New Empty Draft Contact List
                draft_phone_book[name_search] = phone_edit

                # Updating The Draft Contact List With The Original Contact List
                phone_book.update(draft_phone_book)

                print("Phone Number Successfully Changed!")
                print("Updated Phone Book: ", phone_book)
                break
            else:
                print("ERROR: Contact Name Not Found! Please Enter The Correct Contact Name.")
        else:
            print("ERROR: Wrong Input Type! Please Enter Alphabets For Name & Digits For The New Replacable Phone Number.")

# Function: Delete An Existing Contact
def delete(phone_book):
    while True:
        name = input("Enter The Name Of The Contact You Want To Delete: ")

        # Input Validation Check
        if name.isalpha():
            if phone_book.get(name) != None:

                # Deleting The Contact From The Contact List
                phone_book.pop(name)

                print("Contact", name, "has been deleted successfully!")
                print("New Phone Book: ", phone_book)
                break
            else:
                print("ERROR: Contact Name Not Found! Please Enter The Correct Contact Name.")
        else:
            print("ERROR: Wrong Input Type! Please Enter Alphabets For Contact Name.")

# Function: Search A Contact
def search(phone_book):
    search_name = input("Enter The Name Of The Contact You Want To Search: ")

    # Case 1: If The Entered Name Is In The Contact List
    if search_name in phone_book:
        print("Name: ", search_name)

        # If The Entered Name Is Not Found, Then Use 0 As Default Value
        print("Contact Phone: ", phone_book.get(search_name, 0))
    
    # Case 2: If The Entered Name Is Not In The Contact List
    else:
        print("Contact: ", search_name, "Not Found! No Such Contact Is Available!")

print("--------------")
print("PHONE BOOK APP")
print("--------------")

while True:
    choice = int(input("1. View Phone Book\n2. Add New Contact\n3. Edit Existing Contact\n4. Delete A Contact\n5. Search A Contact\n6. Exit\nPlease Enter Your Choice (1 - 6): "))

    # Main Program
    if __name__ == "__main__":

        # Viewing Phone Book
        if choice == 1:
            if is_empty(phone_book) == False:
                view(phone_book)
            else:
                print("No Contacts Yet!")
                print("Thank You For Using The Phone Book App")

        # Adding New Contact In Phone Book
        elif choice == 2:
            add(phone_book)

        # Editing An Existing Contact In Phone Book
        elif choice == 3:
            edit_choice = input("Do you want to edit the name of the contact or phone number of the contact? Press (n/N) for editing the name of the contact OR Press (p/P) for editing the phone number of the contact: ")
            
            # Case 1: Editing The Name Of The Contact
            if edit_choice == 'n' or edit_choice == 'N':
                edit_name(phone_book)

            # Case 2: Editing The Phone Number Of The Contact
            elif edit_choice == 'p' or edit_choice == 'P':
                edit_phone(phone_book)

            # Case 3: Unmatched Entry
            else:
                print("Invalid Entry! Please Enter Either n/N Or p/P.")

        # Deleting An Existing Contact In Phone Book
        elif choice == 4:
            delete(phone_book)

        # Searching A Contact In Phone Book
        elif choice == 5:
            search(phone_book)

        # Exiting The Phone Book Application
        elif choice == 6:
            print("Thank You For Using The Phone Book Application.")
            exit()
