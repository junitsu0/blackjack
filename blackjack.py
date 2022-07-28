import random

#deck - 52 cards - 6 decks - 312 cards in shoe

#dictionary tuples {card id: value, suit}
#===========
#card id A-K
#card value 1-11
#card suits D-S-H-C

#game start
#==========
#deal
#determine player and hand count, add to active list and $bets$
#deal cards (1 each until) 2 per hand and 2 for dealer- random draw from deck list/dictionary

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
# hand > 17 == stay

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