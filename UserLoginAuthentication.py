# Implementing The User Login Authentication Mechanism
# Can Be Used In Any Login System

# Importing The GetPass Module To Hide The Password While Typed
import getpass

# User Class
class User:

    # Initializing Admin Credentials Stored In A Tuple Which Will Never Change
    # Instance Variable
    # Mimicing Database
    admin_credentials = [("admin", "pass123")]

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