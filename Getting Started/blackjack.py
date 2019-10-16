from random import shuffle


class Cards:
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace"]

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            return False
        return False

    def __add__(self, other):
        return self.value + other.value

    def __repr__(self):
        return self.values[self.value]


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Cards(i))
        shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Game:
    def __init__(self):
        self.deck = Deck()

    def playGame(self):
        face_cards = ["Jack", "Queen", "King"]
        print("Let's go")
        player_total = 0
        dealer_total = 0
        hit_stay = "hit"
        while hit_stay == "hit":
            player_card = self.deck.remove_card()
            print(player_card)
            if player_card in face_cards:
                player_total += 10
            elif player_card == "Ace":
                player_total += input("You've have an Ace, enter the value you want (11 or 1): ")
            else:
                player_total += player_card
            if player_total > 21:
                print("You've busted!")
                break
            hit_stay = input("Your total is {}, would you like to hit or stay? ".format(player_total))
        hit_stay = "hit"
        while hit_stay == "hit":
            dealer_card = self.deck.remove_card()
            if dealer_card == "Jack" or "Queen" or "King":
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
            if dealer_total < 16:
                print("The dealer hits")
                hit_stay = "hit"
            else:
                print("The dealer stays")
                hit_stay = "stay"

        if player_total > dealer_total or player_total == 21:
            print("You had a total of {} and the dealer had a total of {}. You won!".format(player_total, dealer_total))
        elif dealer_total > player_total or player_total > 21 or dealer_total == player_total:
            print("You had a total of {} and the dealer had a total of {}. You lost!".format(player_total, dealer_total))


game = Game()
game.playGame()