class Solution:
    def twoSum(self, nums, target: int):
        nums_index_dict = {}
        for index in range(0, len(nums)):
            if (target - nums[index] in nums_index_dict):
                return [nums_index_dict[target - nums[index]], index]
            nums_index_dict[nums[index]] = index
        return []
