print("Hello Player 1! What is your name?")
while True:
    user_name = input()
    confirm = input(f"You entered {user_name}. Is this correct? (yes/no) ")
    if confirm.lower() != 'yes':
        continue
    break
# allows for user to change answer of name if mistakes are made or if they simply want to change it confirm.lower()
# makes it so that if the user types "Yes" the code will still be recognized even if the options are given in lowercase


print("Hello, {}!".format(user_name))
# gets username and stores it under user_name

print("Are you a boy or girl?")
while True:
    user_gender = input()
    confirm = input(f"You entered {user_gender}. Is this correct? (yes/no) ")
    if confirm.lower().startswith('y'): #did the player say yes?
        break
    else:
        print("Please re-enter your gender.")

#final preparations before adventure
print("Is this correct?")
print("You are " + user_name + " and you are a " + user_gender + "?")
print("(yes/no)")
#checks if player says yes or no
while True:
    correct = input()
    if not correct.lower().startswith('y'):
        return "please re-enter your information"
    else:
        break
#returns player for redoing of information
#final message
print(f'Welcome to your new adventure, {user_name}!')
print('Let\'s get started.')