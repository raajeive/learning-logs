class Solution:
    def getTimeMins(self, time):
        return ((int(time.split(":")[0]) * 60) + int(time.split(":")[1]))
        
    def convertTime(self, current, correct):
        diff = abs(self.getTimeMins(current) - self.getTimeMins(correct))
        count = 0
        for val in [60, 15, 5, 1]:
            count += int(diff / val)
            diff = diff % val
            if diff == 0:
                break
        return count
