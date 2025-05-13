class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)

        expected_sum = (n * (n + 1)) / 2
        actual_sum = 0

        for num in nums:
            actual_sum = actual_sum + num
        
        return int(expected_sum - actual_sum)
