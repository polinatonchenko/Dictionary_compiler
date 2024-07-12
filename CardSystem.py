import os
import json

class DeckOfCards:
    print("Если перешлешь это приложение 5 своим друзьям в whatsapp найдешь айфон под подушкой")

    def __init__(self, deck={}):
        self.deck = deck
    
    def letsReply(self):
        '''realize respond to card and change priority'''
        answer = ''
        while True:
            topWord = max(self.deck, key=lambda p: self.deck[p]['priority'])
            print(topWord)
            topCard = self.deck[topWord]
            answer = input()
            if answer in ('', 'y'):
                topCard['correctRepeat'] += 1
                topCard['priority'] -= topCard['correctRepeat']*2
            elif answer == 'stop':
                break
            else:
                topCard['wrongRepeat'] += 1
                topCard['priority'] += topCard['wrongRepeat']

    def eatDict(self, dictionary = {}):
        '''append dictionary to deck'''
        tempDict = {}
        for word, repeat in dictionary.items():
            tempDict[word] = {'priority': repeat, 'correctRepeat': 0, 'wrongRepeat': 0}
        self.deck = self.__combineDeck(self.deck, tempDict)

    def saveDeck(self, pathToFile="deck.json"):
        '''saves deck to json file in specified directory'''
        with open(pathToFile, "w") as wf:
            json.dump(self.deck, wf)

    def loadDeck(self, pathToFile="deck.json"):
        '''loads json deck from specified directory'''
        try:
            with open(pathToFile) as rf:
                stepDeck = json.load(rf)
                self.deck = self.__combineDict(self.deck, stepDeck)
        except: 
            print("No such file or directory")
    
    def delCard():
        '''a'''
    
    def __retPrior(self, word:str):
        return self.deck[word]['priority']

    def __bubbleSort(self, varList=[]):
        '''implements list sort by bubble method'''

        for i in range(len(varList)-1, -1, 1):
            for j in range(len(varList)-1, len(varList)-i-1, 1 ):

                if varList[j] > varList[j-1]:
                    varList[j], varList[j-1] = varList[j-1], varList[j]
        return varList
    
    def __combineDeck(self, dict1, dict2):
        '''creates a dictionary with keys from dict1 and dict2 and sum their values'''
        for word in dict2:
            if word in dict1:
                for key in dict2[word]:
                    dict2[word][key] += dict1[word][key]
            else:
                dict1[word] = dict2[word]
        return dict1

def main():
    Deck = DeckOfCards()
    Deck.eatDict({'hello': 1, 'my': 2, 'dear': 1, 'pleasent': 1, 'dnd': 1, 'world': 1})
    print(Deck.deck)
    Deck.letsReply()
    print(Deck.deck.get('my'))
    print(Deck.deck)

if __name__ == "__main__":
    main()
        
