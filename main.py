import matplotlib.pyplot as plt

class TextAnalyzer:
    def __init__(self, text):
        # for removing punctuations and all of that stuff
        formattedText = text.replace('?','').replace('!','').replace(',','').replace('.','').replace('\'','')
        # to convert the whole sentence or para in lowercase to standerise all of the cases to lower
        formattedText = formattedText.lower()
        self.frmtText = formattedText
   
    # creating a dictionary for the kjkey value pairs
    
    def freqAll(self):
        # splitting the words from whole string and then storing them in a list
        # Step 1: Split into words and then stores in wordList
        wordList = self.frmtText.split()
        # Step 2: Create empty dictionary
        freqMap = {}
        # Step 3 & 4: Loop and count occurrences
        for word in set(wordList):
            freqMap[word] = wordList.count(word)
        # Step 5: Return the frequency dictionary
        return freqMap


    # freqOf(word) → relies on freqAll() → gets full frequency dictionary → returns only the count for `word`
    def freqOf(self, word):
        freqDict = self.freqAll()
        if word in freqDict:
            
            return freqDict[word]
        else:
            return 0
            
    def showGraph(self):
        freqMap = self.freqAll()
        
        # Plotting bar graph
        plt.figure(figsize=(7, 4))
        plt.bar(freqMap.keys(), freqMap.values(), color='yellow')
        plt.title("Word Frequency Visualization")
        plt.xlabel("Words")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()
