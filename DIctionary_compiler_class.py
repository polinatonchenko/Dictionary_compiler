import os
import json

class DictOfWords:

    def __init__(self):
        self.pathToFile = None
        self.dictionary = {}
    
    def dumpDict(self, pathToFile="dict.json"):
        "biba boba"
        with open(pathToFile, "w") as wf:
            json.dump(self.dictionary, wf)
    
    def loadDict(self, pathToFile="dict.json"):
        try:
            with open(pathToFile) as rf:
                self.dictionary = json.load(rf)
        except: 
            print("No such file or directory")

    def eatText(self, someText:str):
        someText = someText.lower()
        someText = "".join(c for c in someText if c.isalpha() or c==" ")
        wordsList = someText.split()
        stepDictionary = dict.fromkeys(wordsList, 0)
        for word in wordsList:
            stepDictionary[word] += 1
        self.dictionary = self.__combineDict(self.dictionary, stepDictionary)

    def __combineDict(dict1, dict2):
        for key in dict1:
            if key in dict2:
                dict1[key] += dict2[key]
                dict2.pop(key)
        dict1.update(dict2)
        return dict1

    def __repr__(self):
        return repr(self.dictionary)

     

def main():
    dict1 = DictOfWords()
    dict1.loadDict()
    print(dict1)

if __name__ == "__main__":
    main()