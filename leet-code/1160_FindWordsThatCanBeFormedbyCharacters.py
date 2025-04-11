class Solution:
    def countCharacters(self, words, chars):
        charFrequency = {}
        for index in range(len(chars)):
            if chars[index] in charFrequency:
                charFrequency[chars[index]] += 1
            else:
                charFrequency[chars[index]] = 1
        length = 0
        for word in words:
            temp = {}
            for index in range(len(word)):
                if word[index] in temp:
                    temp[word[index]] += 1
                else:
                    temp[word[index]] = 1

            for key in temp.keys():
                if not key in charFrequency or temp[key] > charFrequency[key]:
                    break
            else:
                length += len(word)
        
        return length

