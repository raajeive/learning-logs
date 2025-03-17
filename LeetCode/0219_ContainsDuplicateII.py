class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dupSet = set()
        for index in range(len(nums)):
            if len(dupSet) == k + 1:
                dupSet.remove(nums[index - k - 1])
            if nums[index] in dupSet:
                return True
            dupSet.add(nums[index])
        return False
