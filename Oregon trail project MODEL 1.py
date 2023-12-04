# getting the payer's name
print('Hello!, player! before we continue, what is your name?')
user_name = input()
print('great to meet you, ' + user_name + "!")

# choosing gender
# gets gender of user and stores it under user_gender
print('tell me, are you a boy or a girl?')
# user_name gender
user_gender = input()  # will transfer choice to next line

# checking gender
print("Is this correct? (yes/no)")
while True:
    if user_name == 'No':
        break
    else:
        print("You are " + user_name + " and you are a " + user_gender)
