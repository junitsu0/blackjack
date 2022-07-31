import random

suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
symbols = {'Spades':'\u2664', 'Diamonds':'\u2661', 'Clubs':'\u2667', 'Hearts':'\u2662'}
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
cardcounts = {'2':+1, '3':+1, '4':+1, '5':+1, '6':+1, '7':0, '8':0, '9':0, '10':-1, 'Jack':-1, 'Queen':-1, 'King':-1, 'Ace':-1}

shoe = []
hand = []
score = 0

def int_input(prompt):#check for invalid string inputs
    while True:
        try:
            edgecase = int(input(prompt))
            return edgecase
        except ValueError as x:
            print("Please enter a valid number.")

class Cards:
    def __init__(self, symbols, ranks, values, suits, cardcounts):
        self.ranks = ranks
        self.symbols = symbols
        self.values = values
        self.suits = suits
        self.cardcounts = cardcounts

class Deck:
    def __init__(self):
        for suit in suits:
            for rank in ranks:
                shoe.append(Cards(symbols[suit], rank, values[rank], cardcounts[rank]))
                random.shuffle(shoe)

    def shuffle(self):
        random.shuffle(shoe)

    def __str__(self):
        pass

class Participant:
    def __init__(self, name, hand, score):
        self.name = name
        self.hand = hand
        self.score = score
    
    def stand(self):
        pass

    def hit(self):
        card = random.choice(shoe)
        shoe.pop(card)
        hand.append(card)

    def bust(self):
        for card in hand:
            hand.pop(card)

class Dealer(Participant):
    def __init__(self):
        super().__init__('Dealer', hand, score)
        self.name = "Dealer"

class Player(Participant):
    def __init__(self, name, hand, score):
        super().__init__(name, hand, score, bankroll=0, bet=0)
        1

    def bet(self, amount):
        self.bankroll -= amount
        self.bet += amount

    def pay(self):
        self.bankroll += (self.bet * 2)
        self.bet = 0

    def split(self):
        pass

    def double(self):
        self.bet = (self.bet * 2)
        self.hit

        self.stand

    def surrender(self):
        hand.pop([hand]) #discard hand
        self.bankroll += (self.bet // 2)
        self.bet = 0

class Table: #is this needed?
    def __init__(self, shoe, Dealer, *Player):
        self.participant = Participant()
        self.shoe = Deck()



def setup():
    #create number of player instances -max6- from input value
    while len(hand) < 2:
        card = random.choice(shoe) #card from shoe
        shoe.pop(card)
        hand.append(card)
        Player.score += {values}[1]

        #multiple aces in hand
        #if the [count of Ace] in playerhand is > 1, then playerscore == 10 + [count of Ace] + other card values

print('''
1. Hit
2. Stand
3. Split
4. Double
5. Surrender
6. Flip the Table 
''')
#action loop
option = int(int_input("What would you like to do?"))
while option != 6:
    print(hand)
    if len(hand) == 2:
        int_input(option)
        if option == 1:
            print("You hit")
            Participant.hit()
            score += value
            if score > 21:
                print("You bust")
                Participant.bust()
                break
            elif score == 21:
                print("You have 21")
                break
            else:
                if score < 21:
                    score += value
                    print(f"[hand], score")

        elif option == 2:
            print("You stand")
            Participant.stand()

        elif option == 3:
            print("You split")
            Player.split()

        elif option == 4:
            print("You double down")
            Player.double()

        elif option == 5:
            print("You surrender")
            Player.surrender()

        elif option != 6:
            print("Enter a valid number please")

    print('''
What would you like to do?
1. Hit
2. Stand
3. Split
4. Double
5. Surrender
6. Flip the Table 
''')
    option = int(int_input("What would you like to do?"))







#deck - 52 cards - 6 decks - 312 cards in shoe

#dictionary tuples {card id: value, suit}
#===========
#card id A-K
#card value 1-11
#card suits D-S-H-C

#game start
#==========
#determine player count and hand count, add to active list and $bets$
#deal cards (1 each until) 2 per hand and 2 for dealer- random draw from deck list/dictionary
#hand totals


#dealing opening hands

        
        


#pre-action
#==========
#check dealer blackjack
#check player blackjack
#even money options if pbj w/dealer ace   y/n
#insurance options if dealer ace   y/n $amount

#go to player 1 - action




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