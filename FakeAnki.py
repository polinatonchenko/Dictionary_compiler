import CardSystem
хаха лалка соси бибу 
import DIctionaryCompiler

def main():
    while True:
        tempCommand = input()
        match tempCommand:
            case "stop":
                break
            case "help":
                print("SUCK IT")
            case "cdict"|"create dictionary":
                dictionary = DIctionaryCompiler.DictOfWords()
            case "sdict"|"save dictonary":
                print("print path to file")
                pathToFile = input()
                if pathToFile == "":
                    dictionary.saveDict()
                else:
                    dictionary.saveDict(pathToFile)
            case "ldict"|"load dictionary":
                print("print path to file")
                pathToFile = input()
                if pathToFile == "":
                    dictionary.loadDict()
                else:
                    dictionary.loadDict(pathToFile)
            case "etext"|"eat text":
                print("print the text")
                someText = input()
                dictionary.eatText(someText)
            case "cdeck"|"create deck":
                deck = CardSystem.DeckOfCards()
                print(deck.deck)
            case "sdeck"|"save deck":
                print("print path to file")
                pathToFile = input()
                if pathToFile == "":
                    deck.saveDeck()
                else:
                    deck.saveDeck(pathToFile)
            case "ldeck"|"load deck":
                print("print path to file")
                pathToFile = input()
                if pathToFile == "":
                    deck.loadDeck()
                else:
                    deck.loadDeck(pathToFile)
            case "edict"|"eat dictionary":
                deck.eatDict(dictionary.dictionary)
            case "lr"|"lets reply":
                deck.letsReply()
            case "pd"|"print deck":
                print(deck.deck)
            case _:
                print("try another one command")


if __name__ == "__main__":
    main()
