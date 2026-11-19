import numpy as np
import pandas as pd
import random
import possibleMoves as pm
import strategies as strat
import matplotlib.pyplot as plt

colors = ["diamonds","spades","hearts","clubs"]
values = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

games = 100000
num_decks = 6
betAmount = 100
startingChips = 100000
chips = startingChips

deck = np.array([
    (color,value)
    for i in range(num_decks)
    for color in colors
    for value in values
])

newDeck = deck.copy()

playerCards = []
dealerCards = []

EV = 0

fura = 0
blackjacks = 0
wins = 0
draws = 0
loses = 0
currentChips = []
outputsY = [blackjacks,wins,draws,loses,fura,loses+fura,wins+blackjacks]
outputsX = ["BlackJacks","Wins","Draws","Loses","Fura","Loses + Fura","Wins + BlackJacks"]

def firstCards():
    global newDeck
    index = np.random.randint(len(newDeck))
    playerCards.append(newDeck[index])
    newDeck = np.delete(newDeck,index,axis=0)

    index = np.random.randint(len(newDeck))
    playerCards.append(newDeck[index])
    newDeck = np.delete(newDeck, index, axis=0)

    index = np.random.randint(len(newDeck))
    dealerCards.append(newDeck[index])
    newDeck = np.delete(newDeck, index, axis=0)

    index = np.random.randint(len(newDeck))
    dealerCards.append(newDeck[index])
    newDeck = np.delete(newDeck, index, axis=0)

    if strategy(1):
        gettingWinner()

def strategy(choice):
    if choice == 1:
        while strat.stopAtSeventeen(playerCards,handValue(playerCards),newDeck) is False:
            strat.stopAtSeventeen(playerCards, handValue(playerCards), newDeck)
        else:
            return True


def handValue(cards):
    hv = 0
    aces = 0
    for card in cards:
        if card[1] == "J" or card[1] == "Q" or card[1] == "K":
            hv += 10
        elif card[1] == "A":
            aces += 1
        else:
            hv += int(card[1])

    hv += 11 * aces
    for A in range(aces):
        if hv > 21:
            hv -= 10

    return hv


def gettingWinner():
    global chips
    global newDeck
    global wins,draws,loses,blackjacks,fura
    if handValue(playerCards) == 21 and len(playerCards) == 2:
        chips += betAmount * (3/2)
        blackjacks += 1
        return

    if handValue(playerCards) > 21:
        chips -= betAmount
        fura += 1
        return

    while handValue(dealerCards) < 17 :
        index = np.random.randint(len(newDeck))
        dealerCards.append(newDeck[index])
        newDeck = np.delete(newDeck, index, axis=0)

    if handValue(playerCards) > handValue(dealerCards) or handValue(dealerCards) > 21:
        chips += betAmount
        wins += 1
    elif handValue(playerCards) < handValue(dealerCards):
        chips -= betAmount
        loses += 1
    else:
        draws += 1

def playGame():
    global playerCards
    global dealerCards
    global newDeck

    currentChips.append(chips)
    playerCards = []
    dealerCards = []

    firstCards()

    if len(newDeck) < 0.2 * len(deck):
        newDeck = deck.copy()



if __name__ == "__main__":
    x0 = 0
    for i in range(games):
        playGame()
        if chips == 0 and x0 == 0:
            x0 = i

    EV = (chips-startingChips)/(games * betAmount)


    plt.figure(1)
    plt.plot(range(games),currentChips,label = f"House Edge is {EV}")
    plt.xlabel("Number of Games")
    plt.ylabel("Current Chips")
    plt.title("Stop At 17 Strategy")
    plt.axhline(y = 0, linestyle = "--",color = "red",label = "0 chips mark")
    if x0 > 0:
        plt.axvline(x = x0, linestyle = "--",color = "blue",label = f"Bankruptcy Point reached after {x0} games")
    plt.legend()

    plt.figure(2)
    outputsY = [blackjacks,wins,draws,loses,fura,loses+fura,wins+blackjacks]
    plt.bar_label(plt.bar(outputsX, outputsY, color = ["gold","green","gray","red","black","#5f0202","blue"]),fmt='%.0f', padding=3)

    plt.show()



