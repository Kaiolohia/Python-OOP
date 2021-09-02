from random import randint
class WordFinder:
    def __init__(self, dictionaryPath):
        self.raw_words = open(dictionaryPath, 'r')
        self.raw_words = self.raw_words.readlines()
        self.words = []
        for word in self.raw_words:
            self.words.append(word.rstrip()) 
        print(f"{len(self.words)} words read")
    def random(self):
        return self.words[randint(0, len(self.words))]

class SpecialWordFinder(WordFinder):
    def __init__(self, dictionaryPath):
        super().__init__(dictionaryPath)
        self.catagories = {}
        self.currentCatagory = ''
        print(self.words)
        for line in self.words:
            if "#" in line:
                self.catagories[line] = []
                self.currentCatagory = line
            else:
                self.catagories[self.currentCatagory].append(line)
            print(self.catagories)