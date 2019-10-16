import random

shake = input("Type 'SHAKE' to shake the magic 8 ball and get a fortune! ")

while shake == "SHAKE":
    num = random.randint(1,8)
    if num == 1:
        print("Try again")
    elif num == 2:
        print("Bad luck today")
    elif num == 3:
        print("Good luck today")
    elif num == 4:
        print("You fucked boi")
    elif num == 5:
        print("You will have a great day")
    elif num == 6:
        print("Very bad luck today")
    elif num == 7:
        print("Invest in gold")
    elif num == 8:
        print("Invest in life insurance")
    shake = input("\nType 'SHAKE' to try again!, or 'quit' to stop ")