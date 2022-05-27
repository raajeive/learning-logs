import sys

class Solution:
    def minWindow(self, source, target):
        if not source or not target or len(target) > len(source):
            return ""
        targetDict = {}
        for char in target:
            if char in targetDict:
                targetDict[char] += 1
            else:
                targetDict[char] = 1

        start = 0
        end = 0
        targetLength = len(target)
        first = 0
        last = sys.maxsize

        while end < len(source):
            if source[end] not in targetDict:
                targetDict[source[end]] = 0
            targetDict[source[end]] -= 1
            if targetDict[source[end]] >= 0:
                targetLength -= 1

            if targetLength == 0 and (end - start) < (last - first):
                first = start
                last = end

            while targetLength == 0:
                targetDict[source[start]] += 1
                if targetDict[source[start]] > 0:
                    targetLength += 1
                start += 1
            end += 1
            
            while True:
                if start < end and targetDict[source[start]] < 0:
                    targetDict[source[start]] += 1
                    start += 1
                else:
                    break
            
        return source[first:last + 1] if (last - first) != sys.maxsize else ""
