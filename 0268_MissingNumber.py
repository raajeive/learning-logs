class Solution:
    def missingNumber(self, nums: List[int]):
        n = len(nums)
        sums = (n * (n + 1)) // 2
        for num in nums:
            sums -= num
        return sums
