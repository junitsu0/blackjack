import random
#attributes
suits = ('Spades', 'Diamonds', 'Clubs', 'Hearts')
symbols = {'Spades':'\u2664', 'Diamonds':'\u2661', 'Clubs':'\u2667', 'Hearts':'\u2662'}
ranks = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
cardcounts = {'2':+1, '3':+1, '4':+1, '5':+1, '6':+1, '7':0, '8':0, '9':0, '10':-1, 'Jack':-1, 'Queen':-1, 'King':-1, 'Ace':-1}
#use for down below
playing = True
#cards have a rank and suit
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit
#build the deck
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()      

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def draw(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
#checks for aces in hand to reduce if over 21
    def acecheck(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 500
        self.bet = 0

    def win(self):
        self.total += self.bet

    def lose(self):
        self.total -= self.bet

def placebet(chips):

    while True:
        try:
            chips.bet = int(input("Place your bet "))
        except ValueError:
            print("Seriously, it's not hard. Try again.")
        else:
            if chips.bet > chips.total:
                print("Oh... you again... you think you are rich, huh?")
            else:
                break

def hit(deck, hand):
    hand.draw(deck.deal())
    hand.acecheck()

def action(deck, hand):
    global playing

    while True:
        option = input("Hit or Stand? (h or s)")

        if option[0].lower() == 'h':
            hit(deck, hand)
        elif option[0].lower() == 's':
            print("Player stands")
            playing = False
        else:
            print("Try again")
            continue
        break

def holecard(player, dealer):
    print("\nDealer's Hand:")
    print(" ????????????")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def holereaveled(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def playbust(player, dealer, chips):
    print("Player busts")
    chips.lose()

def playwin(player, dealer, chips):
    print("Player wins")
    chips.win()

def dealbust(player, dealer, chips):
    print("Dealer busts")
    chips.win()

def dealwin(player, dealer, chips):
    print("Dealer wins")
    chips.lose()

def push(player, dealer):
    print("Push")


print("Welcome")
deck = Deck()
deck.shuffle()
playchips = Chips()

while True:
    playhand = Hand()
    playhand.draw(deck.deal())
    playhand.draw(deck.deal())

    dealhand = Hand()
    dealhand.draw(deck.deal())
    dealhand.draw(deck.deal())

    placebet(playchips)
    holecard(playhand, dealhand)

    if playhand.value == 21 and dealhand.value ==21:
        push(playhand, dealhand)

    if playhand.value == 21 and dealhand.value != 21:
        print("Blackjack!! You win")
    

    while playing:
        action(deck, playhand)
        holecard(playhand, dealhand)

        if playhand.value > 21:
            playbust(playhand, dealhand, playchips)
            break

    if playhand.value <= 21:

        while dealhand.value < 17:
            hit(deck, dealhand)

        holereaveled(playhand, dealhand)

        if dealhand.value > 21:
            dealbust(playhand, dealhand, playchips)
        elif dealhand.value > playhand.value:
            dealwin(playhand, dealhand, playchips)
        elif dealhand.value < playhand.value:
            playwin(playhand, dealhand, playchips)
        else:
            push(playhand, dealhand)

    print("\nPlayer's winnings stand at", playchips.total)

    new_game = input("Continue? y or n ")

    if new_game[0].lower()=='y':
        playing = True
        continue
    else:
        print("Come back soon")
        break