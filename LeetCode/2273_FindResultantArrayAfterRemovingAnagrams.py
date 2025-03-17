class Solution:
    def createDict(self, word):
        temp = {}
        for index in range(len(word)):
            if word[index] in temp:
                temp[word[index]] += 1
            else:
                temp[word[index]] = 1
        return temp

    def removeAnagrams(self, words):
        if not words:
            return []
        index = 1
        while index < len(words) and len(words) > 1:
            prev = self.createDict(words[index - 1])
            cur = self.createDict(words[index])
            if prev == cur:
                words.pop(index)
            else:
                index += 1
        return words
                            
