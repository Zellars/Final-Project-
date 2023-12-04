def get_user_info():
    print("Hello Player 1! What is your name?")
    while True:
        user_name = input()
        confirm = input(f"You entered {user_name}. Is this correct? (yes/no) ")
        if confirm.lower() != 'yes':
            continue
        break

    print("Hello, {}!".format(user_name))

    print("Are you a boy or girl?")
    while True:
        user_gender = input()
        confirm = input(f"You entered {user_gender}. Is this correct? (yes/no) ")
        if confirm.lower().startswith('y'):
            break
        else:
            print("Please re-enter your gender.")

    print("Is this correct?")
    print("You are {} and you are a {}?".format(user_name, user_gender))
    print("(yes/no)")

    while True:
        correct = input()
        if not correct.lower().startswith('y'):
            print("Please re-enter your information")
        else:
            break

    print("Welcome to your new adventure, {}!".format(user_name))
    print("Let's get started.")

# Call the function to start the process
get_user_info()

# Ask if the user wants to start over
while True:
    restart = input("Do you want to start over? (yes/no) ")
    if restart.lower().startswith('y'):
        get_user_info()
    else:
        print("Goodbye!")
        break
