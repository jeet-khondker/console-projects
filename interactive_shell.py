import sys

print("Python {}".format(sys.version))
print("Copyright By Self-Taught Programmer")

while True:
    user_input = input(">>> ")

    if user_input == "exit()":
        print("Console Closed.")
        break

    try:
        result = eval(user_input)

        if result:
            print(result)

    except:

        try:
            exec(user_input)

        except Exception as e:
            print("Error: ", e)
