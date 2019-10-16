import random

print("Welcome to simple boss fight")
print("You can choose to melee (always does 1 damage)")
print("You may use magic (deals 1 or 2 damage and costs equivalent mana)")
print("You may access your items (health potions heal 2, mana potions restore 1)")
print("You may choose to run (exit the fight)\n")

mon_health = 10
user_health = 10
user_mana = 5
items = ["Heath Potion", "Mana Potion"]

while mon_health > 0 or user_health > 0:
    print("Monster Health: ")
    print("[-]"*mon_health)
    print('\n\n')
    print("Your Health: ")
    print("[+]"*user_health)
    print("Your Mana: ")
    print("[~]"*user_mana)
    print("Options: [Melee]\t[Magic]")
    print("         [Items]\t[Run]")
    choice = input("What would you like to do?: ")
    if choice == "Melee":
        is_crit = random.randint(1,6)
        if (is_crit==6):
            mon_health-=3
            print("You dealt a CRIT of 3 damage to the monster!")
        else:
            mon_health-=1
            print("You deal 1 damage to the monster!")
    elif choice == "Magic":
        magic = random.randint(1,2)
        is_crit = random.randint(1,6)
        if user_mana>=magic:
            if (is_crit==6):
                mon_health-=(magic+2)
                print("You have dealt a CRIT of {} to the monster!".format(magic+2))
            else:
                mon_health-=magic
                print("You deal {} damage to the monster!".format(magic))
            user_mana-=magic
        else:
            print("You don't have enough Mana to perform that!")
            continue
    elif choice == "Items":
        print(items)
        item_choice = input("What item would you like to use: ")
        if item_choice == "Health Potion":
            if (10-user_health)<2:
                user_health+=(10-user_health)
                print("You have restored {} Health.".format(10-user_health))
            else:
                user_health+=2
                print("You have restored 2 Health.")
        if item_choice == "Mana Potion":
            if user_mana<5:
                user_mana+=1
            print("You have restored 1 Mana.")
    elif choice == "Run":
        break
    else:
        print("Please pick a choice from the available options (case sensitive)")
        continue
    if mon_health<=0:
        break
    print('\n')
    print("The monster is attacking!")
    mon_damage = random.randint(1,2)
    crit_bonus = random.randint(1,6)
    if crit_bonus == 6:
        mon_damage+=2
        print("The monster has dealt a CRIT of {} to you".format(mon_damage))
    else:
        print("The monster deals {} damage to you".format(mon_damage))

    user_health-=mon_damage
    if user_health<=0:
        break
    print('\n')

if (user_health<=0):
    print("You have died!")
elif (mon_health<=0):
    print("You have won!")
else:
    print("You have fled!")