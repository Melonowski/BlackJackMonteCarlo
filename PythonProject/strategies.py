import possibleMoves as pm

def stopAtSeventeen(playerHand,playerHandV,newDeck):
    if playerHandV >= 17:
        return True
    elif playerHandV < 17:
        pm.hit(playerHand,newDeck)
        return False
