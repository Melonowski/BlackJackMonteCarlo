
import numpy as np

def stop():
    pass
    #m.gettingWinner()

def hit(playerCards,newDeck):
    index = np.random.randint(len(newDeck))
    playerCards.append(newDeck[index])
    return np.delete(newDeck, index, axis=0)


def doubleDown():
    pass

def insurance():
    pass

def split():
    pass
