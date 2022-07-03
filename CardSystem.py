import os
import json

class DeckOfCards:

    def __init__(self):
        self.deck = []
    
    def eatDict(self, dictionary):
        '''a'''
        for key, value in dictionary.items():
            self.deck.append(self.Card(key, value))

    def loadDeck():
        '''a'''
    
    def __bubbleSort(self, varList=[]):
        '''implements list sort by bubble method'''

        for i in range(len(varList)-1, -1, 1):
            for j in range(len(varList)-1, len(varList)-i-1, 1 ):

                if varList[j] > varList[j-1]:
                    varList[j], varList[j-1] = varList[j-1], varList[j]
        return varList

    class Card:

        def __init__(self, word, priority):
            self.word = word
            self.priority = priority
        
        def __repr__(self):
            return repr([self.word, self.priority])

def bubbleSort(varList):
    for i in range(len(varList)-1, 0, 1):
        for j in range(len(varList)-1, len(varList)-i-1, 1):
            if varList[j] > varList[j-1]:
                varList[j], varList[j-1] = varList[j-1], varList[j]
    return varList

def main():
    print(bubbleSort([1, 3, 2, 4, 10]))
    Deck = DeckOfCards()
    Deck
    Deck.eatDict({'hello': 1, 'my': 2, 'dear': 1, 'pleasent': 1, 'dnd': 1, 'world': 1})
    print(Deck.deck)

if __name__ == "__main__":
    main()
        
