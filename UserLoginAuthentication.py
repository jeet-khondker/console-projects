# Implementing The User Login Authentication Mechanism

# Importing The GetPass Module To Hide The Password While Typed
import getpass

import os

# User Class
class User:

    # Initializing Admin Credentials Stored In A Tuple Which Will Never Change
    # Instance Variable
    # Mimicing Database
    passwordFile = open(r'C:¥¥Users¥jeetkhondker¥Projects¥console-projects¥UserLoginAuthentication¥password_db.txt')
    secretPassword = passwordFile.read()
    admin_credentials = [("admin", secretPassword)]

    # User Initialization
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Function: Login
    def login(self, username, password):
        print("-------- SIGN IN TO ACCESS --------")

        # Taking Username & Password As Input For Login
        un = input("Enter Username To Login: ")

        # Hiding The Password While Typed
        pw = getpass.getpass("Enter Password To Login: ")

        # Username & Password Verification
        if un == administrator.admin_credentials[0][0] and pw == administrator.admin_credentials[0][1]:
            print("Login Successful.")
        else:
            print("User Access Denied!")

# Creating Administrator Object With Empty Username & Password
administrator = User("", "")

# Main Function
if __name__ == "__main__":
    administrator.login("", "")