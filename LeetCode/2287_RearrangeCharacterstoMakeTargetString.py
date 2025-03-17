import sys

class Solution:
    def rearrangeCharacters(self, source, target):
        sourceDict = {}
        for index in range(len(source)):
            if source[index] in sourceDict:
                sourceDict[source[index]] += 1
            else:
                sourceDict[source[index]] = 1
        
        targetDict = {}
        for index in range(len(target)):
            if target[index] in targetDict:
                targetDict[target[index]] += 1
            else:
                targetDict[target[index]] = 1
        
        minRep = sys.maxsize
        
        for key in targetDict.keys():
            if key in sourceDict:
                minRep = min(minRep, int(sourceDict[key] / targetDict[key]))
            else:
                return 0
        
        return minRep

