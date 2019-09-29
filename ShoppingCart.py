# Adding Items To Your Shopping Cart

"""
Creating A List Of Grocery Items From The User & Add It In The Shooping Cart.
It Will Also Take The Size Of The List From The User.
It Will Also Validate The Input From The User. No Numbers. Only Texts.
"""

# Importing The System Module
from sys import *

# Creating A Empty Grocery List
groceries = []

# Checking Whether The Shopping Cart Is Empty Or Not
def is_empty(groceries):
    if groceries:
        return False
    else:
        return True

# Function: Viewing Shopping Cart
def list_item(groceries):
    if is_empty(groceries) == True:
        print("No Items In Your Shopping Cart Yet!")
    elif len(groceries) == 1:
        print("Your Shopping Cart: ", groceries[0])
    else:
        # String Manipulation
        print("Your Shopping Cart: ", '{} And {}'.format(', '.join(groceries[:-1]), groceries[-1]))

# Function: Adding Grocery Items
def add_items():
    while True:
        size = input("Enter The Size Of Your Shopping Cart: ")

        try:
            int_size = int(size)

            while int_size != 0:
                try:
                    for item in range(int_size):
                        food = input("Enter A Food Item: ")

                        # Input Validation: Only Alphabets
                        if food.isalpha():
                            groceries.append(food)
                            int_size -= 1
                        else:
                            raise TypeError
                except TypeError:
                    print("ERROR: Wrong Input! Please Enter Letters Only.")
                    continue
            
            list_item(groceries)
            break

        except ValueError:
            print("ERROR: Wrong Input! Please Enter Numbers Only.")

# Main Function
if __name__ == "__main__":
    print("-----------------")
    print("SHOPPING CART APP")
    print("-----------------")

    while True:
        choice = input("1. View Your Orders\n2. Add to Cart\n3. Exit\nEnter Your Choice (Please enter numbers between 1 to 3: ")

        try:
            int_choice = int(choice)
            
            # Viewing Orders
            if int_choice == 1:
                list_item(groceries)
            
            # Adding Items To Cart
            elif int_choice == 2:
                add_items()

            # Exiting The Shopping Cart Application
            elif int_choice == 3:
                print("Thank You For Using The Shopping Cart Application.")
                exit()

            # Exception Entry
            else:
                print("ERROR: Wrong Choice Input! Please Enter Numbers Between 1 To 3.")
        
        except ValueError:
            print("ERROR: Wrong Input! Please Enter Numbers For Choices.")