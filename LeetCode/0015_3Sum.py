# O(N^2) Time and O(N) Space
class Solution:
    def threeSum(self, nums):
        dataDict = {}
        res = set()
        for index, num in enumerate(nums):
            dataDict[0 - num] = index
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] in dataDict and dataDict[nums[i] + nums[j]] != i and dataDict[nums[i] + nums[j]] != j:
                    out = [nums[i], nums[j], (0 - (nums[i] + nums[j]))]
                    out.sort()
                    res.add(tuple(out))
        return res


# O(N^2) Time and O(1) Space
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for index in range(len(nums) - 2):
            if index > 0 and nums[index] == nums[index -1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                s = nums[index] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append([nums[index], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res
