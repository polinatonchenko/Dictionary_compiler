import os
import json

class DictOfWords:

    def __init__(self):
        self.dictionary = {}
        # self.amountOfWords = 0
    
    def saveDict(self, pathToFile="dict.json"):
        '''saves dictionary to json file in specified directory'''
        with open(pathToFile, "w") as wf:
            json.dump(self.dictionary, wf)
    
    def loadDict(self, pathToFile="dict.json"):
        '''loads json dictionary from specified directory'''
        try:
            with open(pathToFile) as rf:
                stepDictionary = json.load(rf)
                self.dictionary = self.__combineDict(self.dictionary, stepDictionary)
                # self.amountOfWords = sum(self.dictionary.values())
        except: 
            print("No such file or directory")

    def eatText(self, someText:str):
        '''collects statistics from semeText'''
        someText = someText.lower()
        someText = "".join(c for c in someText if c.isalpha() or c==" ")
        wordsList = someText.split()
        stepDictionary = dict.fromkeys(wordsList, 0)
        for word in wordsList:
            stepDictionary[word] += 1
        self.dictionary = self.__combineDict(self.dictionary, stepDictionary)
        # self.amountOfWords = sum(self.dictionary.values())

    def eatFileTXT(self, pathToFile):
        '''collects statistics from .txt file in the specified directory'''
        try:
            with open(pathToFile) as file:
                someText = file.read().replace('\n', ' ')
            self.eatText(someText)
        except:
            print("No such file or directory")

    def eatDir(self, pathToDir=""):
        '''collects statistics from all .txt files in the specified directory'''
        if pathToDir != "":
            pathToDir += "/"
        listOfNames = self.__listFiles(pathToDir)
        for name in listOfNames:
            self.eatFileTXT(f"{pathToDir}{name}")
    
    def __listFiles(self, pathToDir):
        '''creates a list of all file names in a directory with a .txt extension'''
        listOfNames = []
        for file in os.listdir(pathToDir):
            if file.endswith(".txt"):
                listOfNames.append(file)
        return listOfNames

    def __combineDict(self, dict1, dict2):
        '''creates a dictionary with keys from dict1 and dict2 and sum their values'''
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
    dict1.eatText("hello my dear, my pleasent DND - WORLD!")
    print(dict1.dictionary)
    # print(max(dict1.dictionary, key=dict1.dictionary.get))

if __name__ == "__main__":
    main()
