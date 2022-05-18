class Solution:
    def findDuplicate(self, nums):
        start = 1
        end = len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                start = mid + 1
            else:
                end = mid
        return start

