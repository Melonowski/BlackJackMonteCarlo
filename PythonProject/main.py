import numpy as np
import pandas as pd
import random
import possibleMoves as pm

colors = ["diamonds","spades","hearts","clubs"]
values = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

num_decks = 6
betAmount = 100
chips = 1000

deck = np.array([
    (color,value)
    for i in range(num_decks)
    for color in colors
    for value in values
])

newDeck = deck

playerCards = []
dealerCards = []


def firstCards():
    global newDeck
    index = np.random.randint(len(newDeck))
    playerCards.append(deck[index])
    newDeck = np.delete(deck,index,axis=0)

    index = np.random.randint(len(newDeck))
    playerCards.append(newDeck[index])
    newDeck = np.delete(newDeck, index, axis=0)

    index = np.random.randint(len(newDeck))
    dealerCards.append(newDeck[index])
    newDeck = np.delete(newDeck, index, axis=0)

    index = np.random.randint(len(newDeck))
    dealerCards.append(newDeck[index])
    newDeck = np.delete(newDeck, index, axis=0)

    strategy()

def stopAtSeventeen():
    if handValue(playerCards) > 17:
        pm.stop()
    elif handValue(playerCards) < 17:
        pm.hit()

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

    for A in range(aces):
        if hv + 11 > 21:
            hv += 1
        else:
            hv += 11

    return hv

def strategy():
    stopAtSeventeen()

def gettingWinner():
    global chips
    global newDeck
    if handValue(playerCards) == 21 and len(playerCards) == 2:
        print("BLACKJACK!!!")
        chips += betAmount * (3/2)
    else:
        if handValue(dealerCards) < 17 :
            index = np.random.randint(len(newDeck))
            dealerCards.append(newDeck[index])
            newDeck = np.delete(newDeck, index, axis=0)
        else:
            if handValue(playerCards) > handValue(dealerCards):
                chips += betAmount
            elif handValue(playerCards) == handValue(dealerCards):
                pass
                #for now nothing

if __name__ == "__main__":
    firstCards()


