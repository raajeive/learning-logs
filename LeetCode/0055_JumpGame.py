class Solution:
    def canJump(self, nums):
        last = len(nums) - 1
        for index in range(len(nums) - 2, -1, -1):
            if index + nums[index] >= last:
                last = index
        return last == 0
