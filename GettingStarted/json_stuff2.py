import json

def ask_for_num():
    fav_num = input("What's your favorite number? ")
    filename = 'user_fav_num.json'
    with open(filename, 'w') as f_obj:
        json.dump(fav_num, f_obj)
    return fav_num

def read_num():
    filename = 'user_fav_num.json'
    try:
        with open(filename) as f_obj:
            fav_num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return fav_num

def users_fav_num():
    fav_num = read_num()
    if fav_num:
        print("Your favorite number is: {}".format(fav_num))
    else:
        ask_for_num()


users_fav_num()