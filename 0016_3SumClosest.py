class Solution:
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return -1
        nums.sort()
        sumClosest = nums[0] + nums[1] + nums[2]
        for index in range(len(nums) - 2):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                s = nums[index] + nums[left] + nums[right]
                if s == target:
                    return s
                if abs(s - target) < abs(sumClosest - target):
                    sumClosest = s
                if s < target:
                    left += 1
                else:
                    right -= 1
        return sumClosest
