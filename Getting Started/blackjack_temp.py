from random import shuffle

values = [None, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]


cards = []
for i in range(2, 15):
    for j in range(4):
        cards.append(values[i])
shuffle(cards)


face_cards = ["Jack", "Queen", "King"]
print("Let's go")
player_total = 0
dealer_total = 0
hit_stay = "hit"
player_bust = False
while hit_stay == "hit":
    player_card = cards.pop()
    print(player_card)
    if player_card in face_cards:
        player_total += 10
    elif player_card == "Ace":
        player_total += int(input("You have an Ace, enter the value you want (11 or 1): "))
    else:
        player_total += player_card
    if player_total > 21:
        print("You've busted!")
        player_bust = True
        break
    hit_stay = input("Your total is {}, would you like to hit or stay? ".format(player_total))
print('\n')
hit_stay = "hit"
while hit_stay == "hit" and not player_bust:
    dealer_card = cards.pop()
    if dealer_card in face_cards:
        dealer_total += 10
    elif dealer_card == "Ace":
        if dealer_total <= 10:
            dealer_total += 11
        else:
            dealer_total += 1
    else:
        dealer_total += dealer_card
    if dealer_total > 21:
        print("The dealer busts!")
        break
    if dealer_total < 15:
        print("The dealer hits")
        hit_stay = "hit"
    else:
        print("The dealer stays")
        hit_stay = "stay"

print('\n')
if player_total > 21:
    print("You lost! Your total was {} and the dealer's was {}".format(player_total, dealer_total))
elif dealer_total > 21:
    print("You won! Your total was {} and the dealer's was {}".format(player_total, dealer_total))
elif dealer_total < player_total <= 21:
    print("You had a total of {} and the dealer had a total of {}. You won!".format(player_total, dealer_total))
elif player_total < dealer_total <= 21 or dealer_total == player_total:
    print("You had a total of {} and the dealer had a total of {}. You lost!".format(player_total, dealer_total))