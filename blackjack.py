import random

table = [dealer, *player]

playerhand = []
dealerhand = []

runningcount = 0
truecount = runningcount / (Cards in shoe / 52)
playerscore = 0
dealerscore = 0

#deck - 52 cards - 6 decks - 312 cards in shoe
class Deck:
    shoe = []
    for suit in suits:
        for face in faces:
            shoe.append(Card(suits_symbols[suit], face, values[face]))


    def __init__(self, cards):
        self.cards = cards


class Card:
    suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
    suits_symbols = {'Spades':'\u2664', 'Diamonds':'\u2661', 'Clubs':'\u2667', 'Hearts':'\u2662'}
    faces = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
    cardcount = {'2':+1, '3':+1, '4':+1, '5':+1, '6':+1, '7':0, '8':0, '9':0, '10':-1, 'Jack':-1, 'Queen':-1, 'King':-1, 'Ace':-1}

    def __init__(self, faces, values, suits, cardcount):
        self.faces = faces
        self.values = values
        self.suits = suits
        self.cardcount = cardcount


#dictionary tuples {card id: value, suit}
#===========
#card id A-K
#card value 1-11
#card suits D-S-H-C

#game start
#==========
#determine player count and hand count, add to active list and $bets$
#deal cards (1 each until) 2 per hand and 2 for dealer- random draw from deck list/dictionary
def gamestart():
    input("Welcome to the table folks. How many players today?")
    while player in game:
        for each player and dealer in table:
            random.choice(shoe) * 2
        if 'Ace' in dealer[0] and (self.playerscore) == 21:
            input("Would you like even money? y/n ")
                if "y":
                    (self.player)stack = ((self.player)bet * 1.5) + (self.player)stack
                else:    

        


#pre-action
#==========
#check dealer blackjack
#check player blackjack
#even money options if pbj w/dealer ace   y/n
#insurance options if dealer ace   y/n $amount

#go to player 1 - action

class Action:
    def __init__(self):

    def hit(Action):
        def __init__(self):

    def stay(Action):
        def __init__(self):

    def split(Action):
        def __init__(self):

    def double(Action):
        def __init__(self):

    def surrender(Action):
        def __init__(self):


#actions - input menu
#========
#hit (draw random card, add to hand)
#stay (end turn)
#split (only 1st action on hand, generate new hand same player)
#surrender (only 1st action on hand, then lose hand with half bet loss)
#doubledown (only 1st action on hand, double bet, +1 card, end turn)

#go to next player - for loop each player in list, repeat action list

#go to dealer
#dealer rules
#dealer is automated by ruleset
# while < 17 == hit
# hand >= 17 == stay

#compare dealer total vs player total for each player in active list
# player > dealer == pay bet 1:1
# player == dealer return bet
# player < dealer == lose bet

#discard all in play cards to the discard

#round end

#check for cut card (if deck < X card count, game ends)(ask for new shoe y/n) y-restart and retain $$ n-game end
#otherwise start new round at game start



#====extra spicy stuff=====
# player names random list (community)
# AI players that follow random rulesets
# random comments based on results and/or draws
# betting
# continuing bankroll
# side bets
# card count / true count