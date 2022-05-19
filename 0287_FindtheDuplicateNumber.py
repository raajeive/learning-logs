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


class Solution:
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
