import random

#card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit
#card attributes
suits = ('Spades', 'Diamonds', 'Clubs', 'Hearts')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
cardcounts = {'2':1, '3':1, '4':1, '5':1, '6':1, '7':0, '8':0, '9':0, '10':-1, 'Jack':-1, 'Queen':-1, 'King':-1, 'Ace':-1}

deck = []
#build deck
for suit in suits:
    for rank in ranks:
        deck.append(Card(suit, rank))


#start game
def blackjackgame():
    playerhand = []
    dealerhand = []
    playerscore = 0
    dealerscore = 0
    advantage = 0
    
    global values

#player initial draw
    random.shuffle(deck)
    while len(playerhand) < 2:
        draw = random.choice(deck)
        playerhand.append(draw)
        deck.remove(draw)
        playerscore += draw.value
        advantage += draw.cardcount

        if len(playerhand) == 2:
            if playerhand[0].value == 11 and playerhand[1].value == 11:
                playerhand[0].value = 1
                playerscore -= 10
    print(playerhand)
    print(playerscore)

#dealer initial draw
    while len(dealerhand) < 2:
        draw = random.choice(deck)
        dealerhand.append(draw)
        deck.remove(draw)
        dealerscore += draw.value
        advantage += draw.cardcount

#prevent double ace bust
        if len(dealerhand) == 2:
            if dealerhand[0].value == 11 and dealerhand[1].value == 11:
                dealerhand[1].value = 1
                dealerhand -= 10
    print(dealerhand)
    print(dealerscore)

#check blackjacks
    if playerscore == 21 and dealerscore == 21:
        print("You have Blackjack! But so does the dealer :/")
        quit()
    elif playerscore == 21 and dealerscore != 21:
        print("You have Blackjack! You win!! :)")
        quit()
    elif dealerscore == 21 and playerscore != 21:
        print("Dealer has Blackjack... You lose :(")
        quit()
#action player loop
    while playerscore < 21:
        print('''
        Your Action
        ===========
        1. Hit
        2. Stand
        ''')
        action = input("What would you like to do?")
        while action not in {1, 2}:
            action = input("It's only two choices, try again")
#hit
        if action == 1:
            draw = random.choice(deck)
            playerhand.append(draw)
            deck.remove(draw)
            playerscore += draw.value
            advantage += draw.cardcount
            acecount = 0
            while playerscore > 21 and acecount < len(playerhand):
                if playerhand[acecount].value == 11:
                    playerhand[acecount].value = 1
                    playerscore -= 10
                    acecount += 1
                else:
                    acecount += 1
            print(dealerhand)
            print(dealerscore)
            print(playerhand)
            print(playerscore)
#stand
        if action == 2:
            break
#bust
    if playerscore > 21:
        print("Player Bust! T.T")
        quit()
#dealer loop
    while dealerscore < 17:
        print("Dealer must hit")
        draw = random.choice(deck)
        dealerhand.append(draw)
        deck.remove(draw)
        dealerscore += draw.value
        advantage += draw.cardcount
        acecount = 0
        while dealerscore > 21 and acecount < len(dealerhand):
            if dealerhand[acecount].value == 11:
                dealerhand[acecount].value = 1
                dealerscore -= 10
                acecount += 1
            else:
                acecount += 1
        print(dealerhand)
        print(dealerscore)
        print(playerhand)
        print(playerscore)
    if dealerscore > 21:
        print("Dealer Breaks!! Table Win!")
        quit()
    elif dealerscore == playerscore:
        print("Push")
        quit()
    elif playerscore > dealerscore:
        print("You win!")
        
    else:
        print("Dealer wins")
