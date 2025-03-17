class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        currentpos = 0
        index = 1
        while index < len(nums):
            if nums[index] != nums[currentpos]:
                currentpos += 1
                nums[currentpos] = nums[index]
            index += 1
        return currentpos + 1
