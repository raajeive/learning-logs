class Solution:
    def numberOfWeakCharacters(self, p):
        p.sort(key = lambda x: (-x[0], x[1]))
        currentMax = 0
        count = 0
        for i in range(len(p)):
            if p[i][1] < currentMax:
                count += 1
            else:
                currentMax = p[i][1]
        return count
