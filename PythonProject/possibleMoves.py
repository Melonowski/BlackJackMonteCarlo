import main as m
import numpy as np

def stop():
    m.gettingWinner()

def hit():
    index = np.random.randint(len(m.newDeck))
    m.playerCards.append(m.newDeck[index])
    m.newDeck = np.delete(m.newDeck, index, axis=0)
    m.strategy()


def doubleDown():
    pass

def insurance():
    pass

def split():
    pass
