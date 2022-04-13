class Solution:
    def twoSum(self, nums, target):
        diffDict = {}
        for index, num in enumerate(nums):
            if num in diffDict:
                return [index, diffDict[num]]
            diffDict[target - num] = index
