import json


def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt user for a new username"""
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet user by name"""
    username = get_stored_username()
    if username:
        answer = input("Hello, are you {}? (yes/no) ".format(username))
        if answer.lower() == 'yes':
            print("Welcome back, {}".format(username))
        else:
            username = get_new_username()
    else:
        username = get_new_username()
        print("We'll remember you when you come back, {}".format(username))

greet_user()
