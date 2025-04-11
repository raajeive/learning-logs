# O(N^3)
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    elif s == target:
                        res.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    else:
                        pass
        return list(res)
