class Solution:
    def removeElement(self, nums, val):
        index = pos = 0
        while index < len(nums):
            if nums[index] != val:
                nums[pos] = nums[index]
                pos += 1
            index += 1
        return pos
